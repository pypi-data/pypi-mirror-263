import asyncio
import functools
import os

from weeeTest.config import weeeConfig
from weeeTest.testdata.common.file.excel.ext.excelUtil import ExcelUtil
from weeeTest.testdata.common.file.json.ext.jsonUtil import JsonUtil
from weeeTest.testdata.common.file.yaml.ext.yamlUtil import YamlUtil
from weeeTest.utils import file
from weeeTest.utils.logging import log


class FileData:
    def file_data(self, file_name: str, do_type: str = 'read', return_type: str = None,
                  sheet: str = "Sheet1", line: int = 1, end_line: int = None, test_data_dir_name: str = 'test_data'):
        if file_name is None:
            raise Exception("file_name不能为空")
        # 寻找文件
        file_dict = self._find_test_data(file_name=file_name, test_data_dir_name=test_data_dir_name)
        if 'read' in do_type:
            suffix = file_name.split(".")[-1]
            if suffix is None or len(suffix) == 0:
                raise Exception("file_name没有文件后缀")

            if suffix == "xlsx":
                return self.excel_data(file_path=file_dict[file_name], file_name=file_name, do_type=do_type,
                                       return_type=return_type, sheet=sheet, line=line, end_line=end_line)
            elif suffix == "csv":
                return self.csv_data(file_path=file_dict[file_name], file_name=file_name, do_type=do_type,
                                     return_type=return_type, line=line, end_line=end_line)
            elif suffix == "json":
                return self.json_data(file_path=file_dict[file_name], file_name=file_name, do_type=do_type,
                                      return_type=return_type)
            elif suffix in ["yaml", "yml"]:
                return self.yaml_data(file_path=file_dict[file_name], file_name=file_name, do_type=do_type,
                                      return_type=return_type)
            else:
                raise Exception("不支持" + suffix + "格式")

    def file_data_param(self, file_name: str, sheet: str = "Sheet1", line: int = 1, end_line: int = None,
                        jmespath_search: str = None, test_data_dir_name: str = 'test_data'):
        if file_name is None:
            raise Exception("file_name不能为空")
        # 寻找文件
        file_dict = self._find_test_data(file_name=file_name, test_data_dir_name=test_data_dir_name)
        data_file_path = file_dict[file_name]

        suffix = file_name.split(".")[-1]
        if suffix is None or len(suffix) == 0:
            raise Exception("file_name没有文件后缀")
        if suffix == "xlsx":
            return self.excel_data_param(file_path=data_file_path, file_name=file_name, sheet=sheet, line=line,
                                         end_line=end_line)
        elif suffix == "csv":
            return self.csv_data_param(file_path=data_file_path, file_name=file_name, line=line, end_line=end_line)
        elif suffix == "json":
            if jmespath_search is None:
                raise Exception('json_path不能为空')
            return self.json_data_param(file_path=data_file_path, file_name=file_name, json_path=jmespath_search)
        elif suffix in ["yaml", "yml"]:
            if jmespath_search is None:
                raise Exception('json_path不能为空')
            return self.yaml_data_param(file_path=data_file_path, file_name=file_name, json_path=jmespath_search)
        else:
            raise Exception("不支持" + suffix + "格式")

    @staticmethod
    def excel_data(file_path: str, file_name: str, do_type: str = None, return_type: str = None,
                   sheet: str = "Sheet1", line: int = 1, end_line: int = None):
        def excel_wrapper(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                if 'read' in do_type:
                    ret = asyncio.run(ExcelUtil._excel_read(file_path, file_name, return_type, sheet, line, end_line))
                    new_args = args + (ret,)
                    return func(*new_args, **kwargs)
                else:
                    raise Exception('excel只支持读取')

            return wrapper

        return excel_wrapper

    @staticmethod
    def excel_data_param(file_path: str, file_name: str, sheet: str = "Sheet1", line: int = 1,
                         end_line: int = None):
        # file_dict = self._find_test_data(file_name=file_name, test_data_dir_name=test_data_dir_name)
        ret = asyncio.run(
            ExcelUtil._excel_read(file_path=file_path, file_name=file_name, sheet=sheet, line=line,
                                  end_line=end_line))
        ret_params = []
        for item in ret:
            ret_params.append(tuple(item))
        return ret_params

    @staticmethod
    def csv_data(file_path: str, file_name: str, do_type: str = None, return_type: str = None, line: int = 1,
                 end_line: int = None):
        """
        装饰器
        :param end_line:
        :param line:
        :param return_type:
        :param do_type:
        :param file_name:
        :param file_path:
        :return:
        """

        def excel_wrapper(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                if 'read' in do_type:
                    ret = asyncio.run(ExcelUtil._csv_read(file_path, file_name, return_type, line, end_line))
                    new_args = args + (ret,)
                    return func(*new_args, **kwargs)
                else:
                    raise Exception('csv只支持读取')

            return wrapper

        return excel_wrapper

    @staticmethod
    def csv_data_param(file_path: str, file_name: str, line: int = 1, end_line: int = None):
        # file_dict = self._find_test_data(file_name=file_name, test_data_dir_name=test_data_dir_name)
        ret = asyncio.run(
            ExcelUtil._csv_read(file_path=file_path, file_name=file_name, line=line, end_line=end_line))
        ret_params = []
        for item in ret:
            ret_params.append(tuple(item))
        return ret_params

    @staticmethod
    def json_data(file_path: str, file_name: str, do_type: str = None, return_type: str = None):
        def excel_wrapper(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                if 'read' in do_type:
                    ret = asyncio.run(JsonUtil._read(file_path, file_name, return_type))
                    new_args = args + (ret,)
                    return func(*new_args, **kwargs)
                else:
                    raise Exception('json只支持读取')

            return wrapper

        return excel_wrapper

    @staticmethod
    def json_data_param(file_path: str, file_name: str, json_path: str):
        # file_dict = self._find_test_data(file_name=file_name, test_data_dir_name=test_data_dir_name)
        ret = asyncio.run(JsonUtil._read(file_path=file_path, file_name=file_name, json_path=json_path))
        # 存在[[]]
        # if str(ret).startswith("[["):
        #     ret = ret[0]
        # ret_params = []
        # for item in ret:
        #     ret_params.append(tuple(dict(item).values()))
        return ret

    @staticmethod
    def yaml_data(file_path: str, file_name: str, do_type: str = None, return_type: str = None):
        def excel_wrapper(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                if 'read' in do_type:
                    ret = asyncio.run(YamlUtil._read(file_path, file_name, return_type))
                    new_args = args + (ret,)
                    return func(*new_args, **kwargs)
                else:
                    raise Exception('yaml只支持读取')

            return wrapper

        return excel_wrapper

    @staticmethod
    def yaml_data_param(file_path: str, file_name: str, json_path: str):
        # file_dict = self._find_test_data(file_name=file_name, test_data_dir_name=test_data_dir_name)
        ret = asyncio.run(YamlUtil._read(file_path=file_path, file_name=file_name, json_path=json_path))
        return ret

    @staticmethod
    def _find_test_data(file_name: str, test_data_dir_name: str) -> dict:
        """
        寻找，判断数据文件
        返回dict：key->文件名，value路径
        """
        # weeeConfig.project_root_dir = os.path.abspath(os.path.join(os.getcwd(), '../../../data/'))
        # weeeConfig.test_data_dir_name = 'testData'
        # 寻找文件

        if weeeConfig.project_root_dir is None:
            raise Exception('配置文件中project_root_dir为空')

        weeeConfig.project_root_dir = weeeConfig.project_root_dir
        # done-已完善从装饰器的调用者给到test_data_dir_name
        weeeConfig.test_data_dir_name = test_data_dir_name
        if weeeConfig.test_data_dir_name is None:
            raise Exception('配置文件中test_data_dir_name为空')

        file_path = os.path.join(weeeConfig.project_root_dir, weeeConfig.test_data_dir_name)
        file_dict, find_file_num = file.find_file_num(file_name=file_name, file_path=file_path)
        if find_file_num == 0:
            raise Exception(f'在{file_path}下没有找到{file_name}')
        if find_file_num > 1:
            raise Exception(f'在{file_path}下找到多个{file_name}文件')
        log.info(f'成功获取{file_name}文件，路径{file_dict[file_name]}')
        return file_dict

    # demo
    # @file_data(file_path='D:\\py_project_company\\weeeTest\\weeeTest\\data\\testData', file_name='excel_data.xlsx',
    #            return_type='list')
    # def test_excel(*args):
    #     print('111执行test_01')
    #
    #     # print(os.path.abspath(os.path.dirname('demo')))
    #     #
    #     #     # s=os.getcwd().join("testData/excel_data.xlsx")
    #     #     # print('绝对路径：',os.path.abspath(s))
    #     print('返回的：', args[0])

    # @file_data(file_path='../testData/', file_name='csv_data.csv', return_type='list')
    # def test_csv(*args):
    #     print('111执行test_02')
    #     print(args[0])

    # @file_data(file_path='../testData/', file_name='json_data.json',return_type='dict')
    # def test_json(*args):
    #     print('111执行test_01')
    #     print(type(args[0]),args[0])
    #
    #
    # @file_data(file_path='../testData/', file_name='testData.yaml', return_type='json')
    # def test_yaml(*args):
    #     print('111执行test_01')
    #     print(args[0])

    # @file_data_param(file_name='excel_data.xlsx')
    # def test_excel_param(*args):
    #     print('111执行test_01')
    #
    #     # print(os.path.abspath(os.path.dirname('demo')))
    #     #
    #     #     # s=os.getcwd().join("testData/excel_data.xlsx")
    #     #     # print('绝对路径：',os.path.abspath(s))
    #     print('返回的：', args)

    # @file_data_param(file_name='csv_data.csv')
    # def test_csv_param(*args):
    #     print('111执行test_01')
    #
    #     # print(os.path.abspath(os.path.dirname('demo')))
    #     #
    #     #     # s=os.getcwd().join("testData/excel_data.xlsx")
    #     #     # print('绝对路径：',os.path.abspath(s))
    #     print('返回的：', args)

    # @file_data_param(file_name='json_data.json', jmespath_search='$.login')
    # def test_json_param(*args):
    #     print('111执行test_01')
    #     print(type(args[0]), args[0])

    # @file_data_param(file_name='testData.yaml', jmespath_search='$.spring.datasource')
    # def test_yaml_param(*args):
    #     print('111执行test_01')
    #     print(type(args[0]), args[0])
