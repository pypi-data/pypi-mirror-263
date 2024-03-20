# -*- coding: utf-8 -*-
"""
Absfuyu: Path
-------------
Path related

Version: 1.6.2
Date updated: 20/03/2024 (dd/mm/yyyy)

Feature:
--------
- Directory
- SaveFileAs
"""


# Module level
###########################################################################
__all__ = [
    # "here_location", "location_wrap", "get_all_file_path",
    # Main
    "Directory",
    "SaveFileAs",
    # Support
    "FileOrFolderWithModificationTime",
    "DirectoryInfo",
]


# Library
###########################################################################
import os
import random
import re
import shutil
from datetime import datetime
from functools import partial
from itertools import product
from pathlib import Path
from typing import Any, List, Literal, Tuple, NamedTuple, Union

from deprecated import deprecated
from deprecated.sphinx import (
    versionadded,
    versionchanged,
    deprecated as sphinx_deprecated,
)

from absfuyu.logger import logger, LogLevel


# Function
###########################################################################
@sphinx_deprecated(reason="Not needed", version="3.0.0")
@deprecated(reason="Not needed", version="3.0.0")
def here_location():  # Deprecated
    """
    Return current file location

    If fail then return current working directory
    """
    try:
        return os.path.abspath(os.path.dirname(__file__))
    except:
        return os.getcwd()

    # return os.path.abspath(os.path.dirname(__file__))


@sphinx_deprecated(reason="Not needed", version="3.0.0")
@deprecated(reason="Not needed", version="3.0.0")
def location_wrap(file_location: str):  # Deprecated
    """
    This function fix some `current working directory` error and return `abspath`
    """
    assert isinstance(file_location, str), "Must be a string"
    try:
        here = here_location()
    except:
        here = ""
    return os.path.join(here, file_location)


@sphinx_deprecated(reason="Not needed", version="3.0.0")
@deprecated(reason="Not needed", version="3.0.0")
def get_all_file_path(folder: str, *file_type: str) -> list:  # Deprecated
    """
    Return a list of tuple: (path to choosen file type, filename)

    - ``folder``: Folder path to search in
    - ``file_type``: File type/extension without the ``"."`` symbol.

    Support multiple file type (separate with ``","`` (coma))
    (Example: ``jpg``, ``png``, ``npy``)
    """
    # Check file type
    # If no `file_type` entered then proceed to print available file type
    if len(file_type) < 1:
        available_file_type = []
        for _, _, files in os.walk(folder):
            for file in files:
                temp = re.search(r"\b.*[.](\w+$)\b", file)
                if temp is not None:
                    available_file_type.append(temp[1])
        # print(f"Available file type: {set(available_file_type)}")
        # return list(set(available_file_type))
        # return None
        raise ValueError(f"Available file type: {set(available_file_type)}")

    # Generate regex pattern
    temp_pattern = "|".join(f"[.]{x}" for x in file_type)
    pattern = f"\\b^([\w ]+)({temp_pattern}$)\\b"
    # print("Search pattern: ", pattern)

    # Iter through each folder to find file
    file_location = []
    # for root, dirs, files in os.walk(folder):
    for root, _, files in os.walk(folder):
        for file in files:
            result = re.search(pattern, file)
            if result is not None:
                file_location.append((os.path.join(root, file), result[1]))
    return file_location


# Support Class
###########################################################################
@versionadded(version="3.3.0")
class FileOrFolderWithModificationTime(NamedTuple):
    """
    File or Folder with modification time

    :param path: Original path
    :param modification_time: Modification time
    """

    path: Path
    modification_time: datetime


@versionadded(version="3.3.0")
class DirectoryInfo(NamedTuple):
    """Information of a directory"""

    files: int
    folders: int
    creation_time: datetime
    modification_time: datetime


class PathRenameCombo(NamedTuple):
    """
    Path rename combo
    """

    original_path: Path
    rename_path: Path


# Class
###########################################################################
class Directory:
    """
    Some shortcuts for directory

    - list_structure
    - delete, rename, copy, move
    - zip
    - quick_info
    """

    def __init__(
        self,
        source_path: Union[str, Path],
        create_if_not_exist: bool = False,
    ) -> None:
        """
        Parameters
        ----------
        source_path : str | Path
            Source folder

        create_if_not_exist : bool
            Create directory when not exist
            (Default: ``False``)
        """
        self.source_path = Path(source_path).absolute()
        if create_if_not_exist:
            if not self.source_path.exists():
                self.source_path.mkdir(exist_ok=True, parents=True)

    def __str__(self) -> str:
        return f"{self.__class__.__name__}({self.source_path})"

    def __repr__(self) -> str:
        return self.__str__()

    def __format__(self, __format_spec: str) -> str:
        """
        Change format of an object.
        Avaiable option: ``info``

        Usage
        -----
        >>> print(f"{<object>:<format_spec>}")
        >>> print(<object>.__format__(<format_spec>))
        >>> print(format(<object>, <format_spec>))
        """
        # Show quick info
        if __format_spec.lower().startswith("info"):
            return self.quick_info().__repr__()

        # No format spec
        return self.__repr__()

    # Rename
    def rename(self, new_name: str) -> None:
        """
        Rename directory

        Parameters
        ----------
        new_name : str
            Name only (not the entire path)
        """
        try:
            logger.debug(f"Renaming to {new_name}...")
            self.source_path.rename(self.source_path.parent.joinpath(new_name))
            logger.debug(f"Renaming to {new_name}...DONE")
        except Exception as e:
            logger.error(e)
        # return self.source_path

    # Copy
    def copy(self, dst: Path) -> None:
        """
        Copy entire directory

        Parameters
        ----------
        dst : Path
            Destination
        """
        logger.debug(f"Copying to {dst}...")
        try:
            try:
                shutil.copytree(self.source_path, Path(dst), dirs_exist_ok=True)
            except:
                shutil.copytree(self.source_path, Path(dst))
            logger.debug(f"Copying to {dst}...DONE")
        except Exception as e:
            logger.error(e)

    # Move
    def move(self, dst: Path) -> None:
        """
        Move entire directory

        Parameters
        ----------
        dst : Path
            Destination
        """
        try:
            logger.debug(f"Moving to {dst}...")
            shutil.move(self.source_path, Path(dst))
            logger.debug(f"Moving to {dst}...DONE")
        except Exception as e:
            logger.error(e)

    # Directory structure
    def _list_dir(self, *ignore: str) -> List[Path]:
        """
        List all directories and files

        Parameters
        ----------
        ignore : str
            List of pattern to ignore. Example: "__pycache__", ".pyc"
        """
        logger.debug(f"Base folder: {self.source_path.name}")

        list_of_path = self.source_path.glob("**/*")

        # No ignore rules
        if len(ignore) == 0:  # No ignore pattern
            return [path.relative_to(self.source_path) for path in list_of_path]

        # With ignore rules
        # ignore_pattern = "|".join(ignore)
        ignore_pattern = re.compile("|".join(ignore))
        logger.debug(f"Ignore pattern: {ignore_pattern}")
        return [
            path.relative_to(self.source_path)
            for path in list_of_path
            if re.search(ignore_pattern, path.name) is None
        ]

    @staticmethod
    @versionadded(version="3.3.0")
    def _split_dir(list_of_path: List[Path]) -> List[List[str]]:
        """
        Split pathname by ``"/"`` or ``"\\"``

        Parameters
        ----------
        list_of_path : list[Path]
            List of Path

        Returns
        -------
        list[list[str]]
            List of splitted dir


        Example:
        --------
        >>> test = [Path(test_root/test_not_root), ...]
        >>> Directory._split_dir(test)
        [[test_root, test_not_root], [...]...]
        """
        out: List[List[str]] = sorted(
            [str(path).split("/") for path in list_of_path]
        )  # Linux split
        # logger.debug(f"Linux split: {out}")

        if (
            max(map(len, out)) == 1
        ):  # Linux split ("/") returns list with len = 1 (no split)
            out: List[List[str]] = sorted(
                [str(path).split("\\") for path in list_of_path]
            )  # Windows split
        # logger.debug(f"Windows split: {out}")
        return out

    def _separate_dir_and_files(
        self,
        list_of_path: List[Path],
        *,
        tab_symbol: str = None,
        sub_dir_symbol: str = None,
    ) -> List[str]:
        """
        Separate dir and file and transform into folder structure

        Parameters
        ----------
        list_of_path : list[Path]
            List of paths

        tab_symbol : str | None
            Tab symbol
            (Default: "\\t")

        sub_dir_symbol : str | None
            Sub-directory symbol
            (Default: "|-- ")

        Returns
        -------
        list[str]
            Folder structure ready to print
        """
        # Check for tab and sub-dir symbol
        if not tab_symbol:
            tab_symbol = "\t"
        if not sub_dir_symbol:
            sub_dir_symbol = "|-- "

        temp: List[List[str]] = self._split_dir(list_of_path)

        return [  # Returns n-tab space with sub-dir-symbol for the last item in x
            f"{tab_symbol * (len(x) - 1)}{sub_dir_symbol}{x[-1]}" for x in temp
        ]

    def list_structure(self, *ignore: str) -> str:
        """
        List folder structure

        Parameters
        ----------
        ignore : str
            Tuple contains patterns to ignore

        Returns
        -------
        str
            Directory structure


        Example (For typical python library):
        -------------------------------------
        >>> test = Directory(<source path>)
        >>> test.list_structure(
                "__pycache__",
                ".pyc",
                "__init__",
                "__main__",
            )
        ...
        """
        temp: List[Path] = self._list_dir(*ignore)
        out: List[str] = self._separate_dir_and_files(temp)
        return "\n".join(out)  # Join the list

    def list_structure_pkg(self) -> str:
        """
        List folder structure of a typical python package

        Returns
        -------
        str
            Directory structure
        """
        return self.list_structure("__pycache__", ".pyc")

    # Delete folder
    # def _mtime_folder(self) -> List[Tuple[Path, datetime]]:
    def _mtime_folder(self) -> List[FileOrFolderWithModificationTime]:
        """
        Get modification time of file/folder (first level only)
        """
        return [
            FileOrFolderWithModificationTime(
                path, datetime.fromtimestamp(path.stat().st_mtime)
            )
            for path in self.source_path.glob("*")
        ]

    @staticmethod
    def _delete_files(list_of_files: List[Path]) -> None:
        """
        Delete files/folders
        """
        for x in list_of_files:
            x = Path(x).absolute()
            logger.debug(f"Removing {x}...")
            try:
                if x.is_dir():
                    shutil.rmtree(x)
                else:
                    x.unlink()
                logger.debug(f"Removing {x}...SUCCEED")
            except:
                logger.error(f"Removing {x}...FAILED")

    @staticmethod
    def _date_filter(
        # value: Tuple[Path, datetime],
        # value: Union[FileOrFolderWithModificationTime, Tuple[Path, datetime]],
        value: FileOrFolderWithModificationTime,
        period: Literal["Y", "M", "D"] = "Y",
    ) -> bool:
        """
        Filter out file with current Year|Month|Day
        """
        period = period.upper().strip()
        # data = {
        #     "Y": value[1].year,
        #     "M": value[1].month,
        #     "D": value[1].day
        # }
        data = {
            "Y": value.modification_time.year,
            "M": value.modification_time.month,
            "D": value.modification_time.day,
        }
        now = datetime.now()
        ntime = {"Y": now.year, "M": now.month, "D": now.day}
        return data[period] != ntime[period]

    def delete(
        self,
        entire: bool = False,
        *,
        based_on_time: bool = False,
        keep: Literal["Y", "M", "D"] = "Y",
    ) -> None:
        """
        Deletes everything

        Parameters
        ----------
        entire : bool
            | ``True``: Deletes the folder itself
            | ``False``: Deletes content inside only
            | (Default: ``False``)

        based_on_time : bool
            | ``True``: Deletes everything except ``keep`` period
            | ``False``: Works normal
            | (Default: ``False``)

        keep : Literal["Y", "M", "D"]
            Delete all file except current ``Year`` | ``Month`` | ``Day``
        """
        try:
            logger.info(f"Removing {self.source_path}...")

            if entire:
                shutil.rmtree(self.source_path)
            else:
                if based_on_time:
                    filter_func = partial(self._date_filter, period=keep)
                    # self._delete_files([x[0] for x in filter(filter_func, self._mtime_folder())])
                    self._delete_files(
                        [x.path for x in filter(filter_func, self._mtime_folder())]
                    )
                else:
                    self._delete_files(map(lambda x: x.path, self._mtime_folder()))

            logger.info(f"Removing {self.source_path}...SUCCEED")
        except Exception as e:
            logger.error(f"Removing {self.source_path}...FAILED\n{e}")

    # Zip
    def compress(self, *, format: str = "zip") -> None:
        """
        Compress the directory (Default: Create ``.zip`` file)

        Parameters
        ----------
        format : Literal["zip", "tar", "gztar", "bztar", "xztar"]
            - ``zip``: ZIP file (if the ``zlib`` module is available).
            - ``tar``: Uncompressed tar file. Uses POSIX.1-2001 pax format for new archives.
            - ``gztar``: gzip'ed tar-file (if the ``zlib`` module is available).
            - ``bztar``: bzip2'ed tar-file (if the ``bz2`` module is available).
            - ``xztar``: xz'ed tar-file (if the ``lzma`` module is available).
        """
        logger.debug(f"Zipping {self.source_path}...")
        try:
            zip_name = self.source_path.parent.joinpath(self.source_path.name)
            shutil.make_archive(zip_name, format=format, root_dir=self.source_path)
            logger.debug(f"Zipping {self.source_path}...DONE")
        except Exception as e:
            logger.error(f"Zipping {self.source_path}...FAILED\n{e}")

    # Everything
    @property
    @versionadded(version="3.3.0")
    def everything(self) -> List[Path]:
        """
        Every folders and files in this Directory
        """
        return list(x for x in self.source_path.glob("**/*"))

    @versionadded(version="3.3.0")
    def _every_folder(self) -> List[Path]:
        """
        Every folders in this Directory
        """
        return list(x for x in self.source_path.glob("**/*") if x.is_dir())

    @versionadded(version="3.3.0")
    def _every_file(self) -> List[Path]:
        """
        Every folders in this Directory
        """
        return list(x for x in self.source_path.glob("**/*") if x.is_file())

    # Quick information
    @versionadded(version="3.3.0")
    def quick_info(self) -> DirectoryInfo:
        """
        Quick information about this Directory

        :rtype: DirectoryInfo
        """
        source_stat: os.stat_result = self.source_path.stat()
        out = DirectoryInfo(
            files=len(self._every_file()),
            folders=len(self._every_folder()),
            creation_time=datetime.fromtimestamp(source_stat.st_ctime),
            modification_time=datetime.fromtimestamp(source_stat.st_mtime),
        )
        return out


class SaveFileAs:
    """File as multiple file type"""

    def __init__(self, data: Any, *, encoding: Union[str, None] = "utf-8") -> None:
        """
        :param encoding: Default: utf-8
        """
        self.data = data
        self.encoding = encoding

    def __str__(self) -> str:
        return f"{self.__class__.__name__}()"

    def __repr__(self) -> str:
        return self.__str__()

    def to_txt(self, path: Union[str, Path]) -> None:
        """
        Save as ``.txt`` file

        Parameters
        ----------
        path : Path
            Save location
        """
        with open(path, "w", encoding=self.encoding) as file:
            file.writelines(self.data)

    # def to_pickle(self, path: Union[str, Path]) -> None:
    #     """
    #     Save as .pickle file

    #     :param path: Save location
    #     """
    #     from absfuyu.util.pkl import Pickler
    #     Pickler.save(path, self.data)

    # def to_json(self, path: Union[str, Path]) -> None:
    #     """
    #     Save as .json file

    #     :param path: Save location
    #     """
    #     from absfuyu.util.json_method import JsonFile
    #     temp = JsonFile(path, sort_keys=False)
    #     temp.save_json()


# Dev and Test new feature before get added to the main class
###########################################################################
class _NewDirFeature(Directory):
    @staticmethod
    def generate_test_folder(destination: Path, safe_switch: bool = True):
        """
        Generate test folder to test (duh)

        Mainly test ``rename_month_folder`` function
        """
        num_of_year: int = 3
        years: List[str] = [
            str(random.randint(1980, datetime.now().year)) for _ in range(num_of_year)
        ]
        # logger.debug(f"Year: {years}")

        months_: List[str] = [str(x).rjust(2, "0") for x in range(1, 13)]
        # logger.debug(f"Month: {months_}")

        list_to_add: List[Tuple[str, str]] = list(product(years, months_))
        # logger.debug(list_to_add)

        convert = [destination.joinpath(*x) for x in list_to_add]
        # logger.debug(convert)
        logger.debug(f"{len(convert)} folders in queue")

        if not safe_switch:
            for x in convert:
                x.mkdir(exist_ok=True, parents=True)
            logger.debug("Folder generated")

        # TODO: create .txt file in each folder

    def rename_month_folder(self):
        """
        Rename month folder

        Must rename the child item of the folder too
        """
        # List of folder relative to source path
        folders: List[Path] = [
            x.relative_to(self.source_path)
            for x in self._every_folder()
            if re.search(r"^\d{4}", str(x.relative_to(self.source_path)))
            and len(str(x.relative_to(self.source_path))) in range(5, 8)
        ]  # only takes the folder which name startwiths year (eg. 2020)
        logger.debug(f"List of folder (filtered):\n{folders}")

        # Split into list
        splitted: List[List[str]] = self._split_dir(folders)
        if len(set(map(len, splitted))) != 1:  # Check if item in format [year, month]
            raise ValueError("Something wrong")

        # Make new name
        convert: List[List[str]] = [[x[0], f"{x[0]}-{x[1]}"] for x in splitted]

        # Zip original name and new name
        join_combo: zip[Tuple[Path, Path]] = zip(
            [self.source_path.joinpath(*x) for x in splitted],
            [self.source_path.joinpath(*x) for x in convert],
        )

        rename_combo = [PathRenameCombo._make(x) for x in join_combo]
        return rename_combo


# Run
###########################################################################
if __name__ == "__main__":
    logger.setLevel(LogLevel.DEBUG)
