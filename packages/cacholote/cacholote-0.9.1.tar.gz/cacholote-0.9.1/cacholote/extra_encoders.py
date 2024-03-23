"""Additional encoders that need optional dependencies."""

# Copyright 2019, B-Open Solutions srl.
# Copyright 2022, European Union.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from __future__ import annotations

import contextlib
import functools
import hashlib
import inspect
import io
import mimetypes
import pathlib
import posixpath
import tempfile
import time
from collections.abc import Generator
from typing import (
    Any,
    Callable,
    Literal,
    TypeVar,
    Union,
    cast,
    overload,
)

import fsspec
import fsspec.implementations.local
import pydantic

from . import config, encode, utils

try:
    import dask
    import xarray as xr

    _HAS_XARRAY_AND_DASK = True
except ImportError:
    _HAS_XARRAY_AND_DASK = False

try:
    import magic

    _HAS_MAGIC = True
except ImportError:
    _HAS_MAGIC = False

F = TypeVar("F", bound=Callable[..., Any])

_UNION_IO_TYPES = Union[
    io.RawIOBase,
    io.BufferedIOBase,
    io.TextIOBase,
    fsspec.spec.AbstractBufferedFile,
    fsspec.implementations.local.LocalFileOpener,
]


def _add_ext_to_mimetypes() -> None:
    """Add netcdf, grib, and zarr to mimetypes."""
    mimetypes.add_type("application/netcdf", ".nc", strict=True)
    for ext in (".grib", ".grb", ".grb1", ".grb2"):
        mimetypes.add_type("application/x-grib", ext, strict=False)
    mimetypes.add_type("application/vnd+zarr", ".zarr", strict=False)


_add_ext_to_mimetypes()


def _guess_type(
    fs: fsspec.AbstractFileSystem,
    local_path: str,
    default: str = "application/octet-stream",
) -> str:
    content_type: str = fs.info(local_path).get("ContentType", "")
    if content_type:
        return content_type

    filetype, *_ = mimetypes.guess_type(local_path, strict=False)
    if filetype is None and _HAS_MAGIC:
        with fs.open(local_path, "rb") as f:
            filetype = magic.from_buffer(f.read(), mime=True)
    return filetype or default


def _requires_xarray_and_dask(func: F) -> F:
    """Raise an error if `xarray` or `dask` are not installed."""

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        if not _HAS_XARRAY_AND_DASK:
            raise ValueError("please install 'xarray' and 'dask'")
        return func(*args, **kwargs)

    return cast(F, wrapper)


def _filesystem_is_local(fs: fsspec.AbstractFileSystem) -> bool:
    return isinstance(fs, fsspec.get_filesystem_class("file"))


@contextlib.contextmanager
def _logging_timer(event: str, **kwargs: Any) -> Generator[float, None, None]:
    logger = config.get().logger
    logger.info(f"start {event}", **kwargs)
    tic = time.perf_counter()
    yield tic
    toc = time.perf_counter()
    kwargs["_".join(event.split() + ["time"])] = toc - tic  # elapsed time
    logger.info(f"end {event}", **kwargs)


class FileInfoModel(pydantic.BaseModel):
    type: str
    href: str
    file_checksum: str = pydantic.Field(..., alias="file:checksum")
    file_size: int = pydantic.Field(..., alias="file:size")
    file_local_path: str = pydantic.Field(..., alias="file:local_path")


def _dictify_file(fs: fsspec.AbstractFileSystem, local_path: str) -> dict[str, Any]:
    href = posixpath.join(
        config.get().cache_files_urlpath_readonly or config.get().cache_files_urlpath,
        posixpath.basename(local_path),
    )
    file_dict = {
        "type": _guess_type(fs, local_path),
        "href": href,
        "file:checksum": f"{fs.checksum(local_path):x}",
        "file:size": fs.size(local_path),
        "file:local_path": local_path,
    }

    return FileInfoModel(**file_dict).model_dump(by_alias=True)


def _get_fs_and_urlpath(
    file_json: dict[str, Any],
    storage_options: dict[str, Any] | None = None,
    validate: bool = False,
) -> tuple[fsspec.AbstractFileSystem, str]:
    urlpath = file_json["file:local_path"]
    if storage_options is None:
        storage_options = config.get().cache_files_storage_options

    if not validate:
        fs, *_ = fsspec.get_fs_token_paths(urlpath, storage_options=storage_options)
        return (fs, urlpath)

    # Attempt to read from local_path
    try:
        fs, *_ = fsspec.get_fs_token_paths(urlpath, storage_options=storage_options)
    except:  # noqa: E722
        pass
    else:
        if fs.exists(urlpath):
            expected = file_json["file:checksum"]
            actual = (
                fs.checksum(urlpath)  # Just for backward compatibility.
                if isinstance(expected, int)
                else f"{fs.checksum(urlpath):x}"
            )
            if expected != actual:
                raise ValueError(f"checksum mismatch: {urlpath=} {expected=} {actual=}")
            config.get().logger.info(
                "retrieve cache file", urlpath=fs.unstrip_protocol(urlpath)
            )
            return (fs, urlpath)

    # Attempt to read from href
    urlpath = file_json["href"]
    fs, *_ = fsspec.get_fs_token_paths(urlpath)
    if fs.exists(urlpath):
        return (fs, urlpath)

    # Nothing worked
    raise ValueError(
        f"No such file or directory: {file_json['file:local_path']!r} nor {file_json['href']!r}"
    )


@overload
def decode_xr_object(
    file_json: dict[str, Any],
    storage_options: dict[str, Any],
    xr_type: Literal["DataArray"],
    **kwargs: Any,
) -> xr.DataArray: ...


@overload
def decode_xr_object(
    file_json: dict[str, Any],
    storage_options: dict[str, Any],
    xr_type: Literal["Dataset"],
    **kwargs: Any,
) -> xr.Dataset: ...


@_requires_xarray_and_dask
def decode_xr_object(
    file_json: dict[str, Any],
    storage_options: dict[str, Any],
    xr_type: Literal["Dataset", "DataArray"],
    **kwargs: Any,
) -> xr.Dataset | xr.DataArray:
    fs, urlpath = _get_fs_and_urlpath(
        file_json, storage_options=storage_options, validate=True
    )

    if file_json["type"] == "application/vnd+zarr":
        filename_or_obj = fs.get_mapper(urlpath)
    else:
        if _filesystem_is_local(fs):
            filename_or_obj = urlpath
        else:
            # Download local copy
            protocols = (fs.protocol,) if isinstance(fs.protocol, str) else fs.protocol
            with fsspec.open(
                f"filecache::{urlpath}",
                filecache={"same_names": True},
                **{protocol: fs.storage_options for protocol in protocols},
            ) as of:
                filename_or_obj = of.name
    if xr_type == "Dataset":
        return xr.open_dataset(filename_or_obj, **kwargs)
    return xr.open_dataarray(filename_or_obj, **kwargs)


def decode_xr_dataset(
    file_json: dict[str, Any], storage_options: dict[str, Any], **kwargs: Any
) -> xr.Dataset:
    return decode_xr_object(file_json, storage_options, "Dataset", **kwargs)


def decode_xr_dataarray(
    file_json: dict[str, Any], storage_options: dict[str, Any], **kwargs: Any
) -> xr.DataArray:
    return decode_xr_object(file_json, storage_options, "DataArray", **kwargs)


def decode_io_object(
    file_json: dict[str, Any], storage_options: dict[str, Any], **kwargs: Any
) -> _UNION_IO_TYPES:
    fs, urlpath = _get_fs_and_urlpath(
        file_json, storage_options=storage_options, validate=True
    )
    return fs.open(urlpath, **kwargs)


@_requires_xarray_and_dask
def _maybe_store_xr_object(
    obj: xr.Dataset | xr.DataArray,
    fs: fsspec.AbstractFileSystem,
    urlpath: str,
    filetype: str,
) -> None:
    if filetype == "application/vnd+zarr":
        with utils.FileLock(
            fs, urlpath, timeout=config.get().lock_timeout
        ) as file_exists:
            if not file_exists:
                # Write directly on any filesystem
                mapper = fs.get_mapper(urlpath)
                with _logging_timer("upload", urlpath=fs.unstrip_protocol(urlpath)):
                    obj.to_zarr(mapper, consolidated=True)
    elif not fs.exists(urlpath):
        # Need a tmp local copy to write on a different filesystem
        with tempfile.TemporaryDirectory() as tmpdirname:
            tmpfilename = str(pathlib.Path(tmpdirname) / pathlib.Path(urlpath).name)

            with _logging_timer("write tmp file", urlpath=tmpfilename):
                if filetype == "application/netcdf":
                    obj.to_netcdf(tmpfilename)
                elif filetype == "application/x-grib":
                    import cfgrib.xarray_to_grib

                    cfgrib.xarray_to_grib.to_grib(obj, tmpfilename)
                else:
                    # Should never get here! xarray_cache_type is checked in config.py
                    raise ValueError(f"type {filetype!r} is NOT supported.")

            _maybe_store_file_object(
                fs if _filesystem_is_local(fs) else fsspec.filesystem("file"),
                tmpfilename,
                fs,
                urlpath,
                io_delete_original=True,
            )


@_requires_xarray_and_dask
def dictify_xr_object(obj: xr.Dataset | xr.DataArray) -> dict[str, Any]:
    """Encode a ``xr.Dataset`` to JSON deserialized data (``dict``)."""
    with dask.config.set({"tokenize.ensure-deterministic": True}):
        root = dask.base.tokenize(obj)

    filetype = config.get().xarray_cache_type
    ext = mimetypes.guess_extension(filetype, strict=False)
    urlpath_out = posixpath.join(config.get().cache_files_urlpath, f"{root}{ext}")

    fs_out, *_ = fsspec.get_fs_token_paths(
        urlpath_out,
        storage_options=config.get().cache_files_storage_options,
    )
    _maybe_store_xr_object(obj, fs_out, urlpath_out, filetype)

    file_json = _dictify_file(fs_out, urlpath_out)
    kwargs: dict[str, Any] = {"chunks": {}}
    if filetype == "application/vnd+zarr":
        kwargs.update({"engine": "zarr", "consolidated": True})

    return encode.dictify_python_call(
        decode_xr_dataset if isinstance(obj, xr.Dataset) else decode_xr_dataarray,
        file_json,
        storage_options=config.get().cache_files_storage_options,
        **kwargs,
    )


def _maybe_store_file_object(
    fs_in: fsspec.AbstractFileSystem,
    urlpath_in: str,
    fs_out: fsspec.AbstractFileSystem,
    urlpath_out: str,
    io_delete_original: bool | None = None,
) -> None:
    if io_delete_original is None:
        io_delete_original = config.get().io_delete_original
    with utils.FileLock(
        fs_out, urlpath_out, timeout=config.get().lock_timeout
    ) as file_exists:
        if not file_exists:
            kwargs = {}
            content_type = _guess_type(fs_in, urlpath_in)
            if content_type:
                kwargs["ContentType"] = content_type
            with _logging_timer(
                "upload",
                urlpath=fs_out.unstrip_protocol(urlpath_out),
                size=fs_in.size(urlpath_in),
            ):
                if fs_in == fs_out:
                    if io_delete_original:
                        fs_in.mv(urlpath_in, urlpath_out, **kwargs)
                    else:
                        fs_in.cp(urlpath_in, urlpath_out, **kwargs)
                elif _filesystem_is_local(fs_in):
                    fs_out.put(urlpath_in, urlpath_out, **kwargs)
                else:
                    with fs_in.open(urlpath_in, "rb") as f_in:
                        with fs_out.open(urlpath_out, "wb") as f_out:
                            utils.copy_buffered_file(f_in, f_out)
    if io_delete_original and fs_in.exists(urlpath_in):
        with _logging_timer(
            "remove",
            urlpath=fs_in.unstrip_protocol(urlpath_in),
            size=fs_in.size(urlpath_in),
        ):
            fs_in.rm(urlpath_in)


def _maybe_store_io_object(
    f_in: _UNION_IO_TYPES,
    fs_out: fsspec.AbstractFileSystem,
    urlpath_out: str,
) -> None:
    with utils.FileLock(
        fs_out, urlpath_out, timeout=config.get().lock_timeout
    ) as file_exists:
        if not file_exists:
            f_out = fs_out.open(urlpath_out, "wb")
            with _logging_timer("upload", urlpath=fs_out.unstrip_protocol(urlpath_out)):
                utils.copy_buffered_file(f_in, f_out)


def dictify_io_object(obj: _UNION_IO_TYPES) -> dict[str, Any]:
    """Encode a file object to JSON deserialized data (``dict``)."""
    cache_files_urlpath = config.get().cache_files_urlpath
    fs_out, *_ = fsspec.get_fs_token_paths(
        cache_files_urlpath,
        storage_options=config.get().cache_files_storage_options,
    )

    if hasattr(obj, "path") or hasattr(obj, "name"):
        urlpath_in = obj.path if hasattr(obj, "path") else obj.name  # type: ignore[union-attr]
        fs_in = getattr(obj, "fs", fsspec.filesystem("file"))
        root = f"{fs_in.checksum(urlpath_in):x}"
        ext = pathlib.Path(urlpath_in).suffix
        urlpath_out = posixpath.join(cache_files_urlpath, f"{root}{ext}")
        _maybe_store_file_object(fs_in, urlpath_in, fs_out, urlpath_out)
    else:
        root = hashlib.md5(f"{hash(obj)}".encode()).hexdigest()  # fsspec uses md5
        urlpath_out = posixpath.join(cache_files_urlpath, root)
        _maybe_store_io_object(obj, fs_out, urlpath_out)

    file_json = _dictify_file(fs_out, urlpath_out)
    params = inspect.signature(open).parameters
    kwargs = {k: getattr(obj, k) for k in params.keys() if hasattr(obj, k)}

    return encode.dictify_python_call(
        decode_io_object,
        file_json,
        storage_options=config.get().cache_files_storage_options,
        **kwargs,
    )


def register_all() -> None:
    """Register extra encoders if optional dependencies are installed."""
    for type_ in (
        io.RawIOBase,
        io.BufferedIOBase,
        io.TextIOBase,
        fsspec.spec.AbstractBufferedFile,
        fsspec.implementations.local.LocalFileOpener,
    ):
        encode.FILECACHE_ENCODERS.append((type_, dictify_io_object))
    if _HAS_XARRAY_AND_DASK:
        for type_ in (xr.Dataset, xr.DataArray):
            encode.FILECACHE_ENCODERS.append((type_, dictify_xr_object))
