import asyncio
import json
import os
import time

import yaml

import aiofiles

from weeeTest.utils.json import jmespath
from weeeTest.utils.logging import log


class YamlUtil:

    @staticmethod
    async def _read(file_path: str, file_name: str, return_type: str = None, json_path: str = None):
        """
        读取yaml转换dict json格式
        :param file_path: 文件路径
        :param return_type: 读取转换类型，json:json字符串。其他:字典
        :return: 返回对于类型
        """
        path = os.path.join(file_path, file_name)
        try:
            if file_name is None:
                raise Exception('文件名不能为空')
            else:
                is_contain = file_name.endswith('.yaml')
                if not is_contain:
                    file_name += '.yaml'

                async with aiofiles.open(path, 'r', encoding='utf-8') as file:
                    if json_path is None:
                        load_dict = yaml.safe_load(await file.read())
                        if return_type is None:
                            return load_dict
                        # TODO: @jialing.chen 请确认之前的编写方法是否正确，我已优化报错的异常信息，请查看上一个git提交记录
                        elif "json" in return_type.lower():
                            return json.dumps(load_dict)
                        elif "dict" in return_type.lower():
                            return load_dict
                        else:
                            raise Exception(f'不支持{return_type}类型')
                    else:
                        # 参数化的时候会用
                        load_dict = yaml.safe_load(await file.read())
                        param_list = jmespath(load_dict, json_path)
                        if param_list is None or len(param_list) == 0:
                            raise Exception('jmespath:' + json_path + ",取数据为空")
                        else:
                            return param_list
        except FileNotFoundError:
            raise Exception(f"文件不存在，请确认file_path:{os.path.abspath(path)}")
        except RuntimeError as e:
            raise Exception(str(e))

    @staticmethod
    async def _write(file_path: str, file_name: str, content):
        """
        读取yaml转换dict json格式
        :param file_path: 文件路径
        :param file_name: 读取转换类型，1:json字符串。其他:字典
        :return: 返回对于类型
        """
        try:
            if file_name is None:
                raise Exception('文件名不能为空')
            else:
                is_contain = file_name.endswith('.yaml')
                if not is_contain:
                    file_name += '.yaml'

                #   读取文件
                # init_context = await YamlUtil.read(file_path, file_name)
                #  判断写入类型
                if isinstance(content, dict):
                    async with aiofiles.open(file_path + file_name, 'w', encoding='utf-8') as file:
                        # d = content.update(init_context)
                        # print("合并后",str(d))
                        await file.write(yaml.dump(content, allow_unicode=True))
                        log.info('写入成功')
        except Exception as e:
            raise Exception(str(e))

    # @staticmethod
    # async def _gather():
    #     tasks = [YamlUtil._read("D:\\py_project_company\\qa-weeetest-sdk\\weeeTest\\demo\\test_data", "yaml_data.yaml",
    #                             'json'),
    #              YamlUtil._read("D:\\py_project_company\\qa-weeetest-sdk\\weeeTest\\demo\\test_data", "yaml_data.yaml",
    #                             'dict')]
    #     results = await asyncio.gather(*tasks)  # 使用 * 解包任务列表
    #     print(results[0])
    #     print(results[1])


if __name__ == '__main__':
    # yaml转字典demo
    # word = asyncio.run(YamlUtil._read("../", 'yaml_data.yaml'))
    # print(type(word), word)
    #
    # # yaml转json字符串
    # word = asyncio.run(YamlUtil._read("../", "testData", 'json'))
    # print(type(word), word)
    #
    # #  dict写入yaml
    dic = {
        'server': {
            'age': 10,
            'name': 'zhangsan'
        }
    }
    word = asyncio.run(YamlUtil._write("../", "testData", dic))
    print(type(word), word)

    # asyncio.run(YamlUtil.gather())
    # pool = multiprocessing.Pool(processes=4)  # 4个进程
    # pool.map(YamlUtil.proce(), [1, 2])
    # YamlUtil.main()

    # result1 = asyncio.run(
    #     YamlUtil._read("D:\\py_project_company\\qa-weeetest-sdk\\weeeTest\\demo\\test_data", "yaml_data.yaml",
    #                    'json'))
    # print(result1)
