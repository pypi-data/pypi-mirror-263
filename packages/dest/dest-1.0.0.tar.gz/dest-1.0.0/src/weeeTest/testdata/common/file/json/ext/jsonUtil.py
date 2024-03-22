import asyncio
import json
import os
import time

import aiofiles

from weeeTest.utils.json import jmespath
from weeeTest.utils.logging import log


class JsonUtil:

    @staticmethod
    async def _read(file_path: str = None, file_name: str = None, return_type: str = None, json_path: str = None):
        path = os.path.join(file_path, file_name)

        try:
            if file_name is None:
                raise Exception('文件名不能为空')
            else:
                is_contain = file_name.endswith('.json')
                if not is_contain:
                    file_name += '.json'

                async with aiofiles.open(path, "r", encoding="utf-8") as json_file:
                    if json_path is None:
                        if return_type is None or 'json' in return_type.lower():
                            # json_file.read()返回的是json字符串
                            data = await json_file.read()
                        elif 'dict' in return_type.lower():
                            # data = dict(json.load(await json_file.read()))
                            s = await json_file.read()
                            print(type(s), s)
                            data = json.loads(s)
                        else:
                            raise Exception(f"不支持{return_type}类型")
                        return data
                    else:
                        # 参数化的时候会用到param_list
                        data = json.loads(await json_file.read())
                        param_list = jmespath(data, json_path)
                        # param_list = list(data.get(key))
                        if param_list is None or len(param_list) == 0:
                            raise Exception('jmespath:' + json_path + ",取数据为空")
                        else:
                            return param_list
        except FileNotFoundError:
            raise Exception(f"文件不存在，请确认file_path:{os.path.abspath(path)}")
        except RuntimeError as e:
            raise Exception(str(e))

    @staticmethod
    async def _write(file_path: str = None, file_name: str = None, context=None):
        try:
            if file_name is None:
                raise Exception('文件名不能为空')
            if context is None:
                raise Exception('写入json不能为空')
            if not isinstance(context, dict) and not JsonUtil._is_json(context):
                raise Exception('context只允许字典，json字符串')

            is_contain = file_name.endswith('.json')
            if not is_contain:
                file_name += '.json'
            async with aiofiles.open(file_path + file_name, "a", encoding="utf-8") as json_file:
                # json.dump(context, json_file, ensure_ascii=False)
                await json_file.write(json.dumps(context, ensure_ascii=False) + '\n')
                log.info('写入成功')
        except FileNotFoundError:
            raise Exception("文件不存在，请确认file_path")
        except RuntimeError as e:
            raise Exception(str(e))

    @staticmethod
    def _is_json(context):
        try:
            json.loads(context)
        except ValueError:
            return False
        return True


if __name__ == '__main__':
    d = asyncio.run(JsonUtil._read(file_path="D:\\py_project_company\\qa-weeetest-sdk\\weeeTest\\demo\\test_data",
                                   file_name='json_data.json', return_type='dict'))
    print(type(d), d)
    #
    # d = JsonUtil._read(file_path='../../../testData/', file_name='json_data.json', return_type='dict')
    # print(type(d), d)
    # d1 = {
    #     'name': '张',
    #     'age': 10
    # }
    # # json_str = "{\"subject\":\"语文\",\"score\":80}"
    #
    # asyncio.run(JsonUtil._write(file_path='D:\\py_project_company\\qa-weeetest-sdk\\weeeTest\\demo\\test_data',
    #                             file_name='json_data_write.json', context=d1))
