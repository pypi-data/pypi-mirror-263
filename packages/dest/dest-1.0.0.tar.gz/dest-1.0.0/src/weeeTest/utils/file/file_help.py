# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Yingqing Shan
@Version        :  V1.0.0
------------------------------------
@File           :  file_help.py
@Description    :  
@CreateTime     :  2023/3/31 11:24
@Software       :  PyCharm
------------------------------------
@ModifyTime     :  2023/3/31 11:24
"""
import inspect
import os
import sys


class FindFilePath:
    """find file path"""

    def __new__(cls, name: str = None) -> str:
        if name is None:
            raise NameError("Please specify filename")
        stack_t = inspect.stack()
        ins = inspect.getframeinfo(stack_t[1][0])
        this_file_dir = os.path.dirname(os.path.dirname(os.path.abspath(ins.filename)))

        _file_path = None
        for root, _, files in os.walk(this_file_dir, topdown=False):
            for _file in files:
                if _file == name:
                    _file_path = os.path.join(root, _file)
                    break
            else:
                continue
            break
        return _file_path


find_file_path = FindFilePath


class File:
    """file class"""

    @property
    def file_path(self) -> str:
        """
        Returns the absolute path to the directory where the current file resides
        For example:
            "/User/tech/you/test_dir/test_sample.py"
            return "/User/tech/you/test_dir/test_sample.py"
        """
        stack_t = inspect.stack()
        ins = inspect.getframeinfo(stack_t[1][0])
        return os.path.abspath(ins.filename)

    @property
    def dir(self) -> str:
        """
        Returns the absolute path to the directory where the current file resides
        For example:
            "/User/tech/you/test_dir/test_sample.py"
            return "/User/tech/you/test_dir/"
        """
        stack_t = inspect.stack()
        ins = inspect.getframeinfo(stack_t[1][0])
        return os.path.dirname(os.path.abspath(ins.filename))

    @staticmethod
    def add_to_path(path: str = None) -> None:
        """
        add path to environment variable path.
        """
        if path is None:
            raise FileNotFoundError("Please setting the File Path")

        sys.path.insert(1, path)

    @staticmethod
    def join(a, *paths):
        """
        Connect two or more path names
        """
        return os.path.join(a, *paths)

    @staticmethod
    def remove(path) -> None:
        """
        del file
        :param path:
        :return:
        """
        if os.path.isfile(path):
            os.remove(path)
        else:
            raise FileNotFoundError("file does not exist")

    @staticmethod
    def find_file_num(file_name: str, file_path: str = '.'):
        """
        在file_path下搜索文件(file_name与ext_name都为空时，表示路径下所有的文件)
        :param file_name:
        :param file_path:
        :return:
        """
        find_file_num = 0
        return_file_dict = {}
        for dirpath, dirnames, filenames in os.walk(file_path):
            for filename in filenames:
                if file_name in filename and '__pycache__' not in dirpath:
                    return_file_dict[filename] = dirpath
                    find_file_num += 1
        return return_file_dict, find_file_num


file = File()
