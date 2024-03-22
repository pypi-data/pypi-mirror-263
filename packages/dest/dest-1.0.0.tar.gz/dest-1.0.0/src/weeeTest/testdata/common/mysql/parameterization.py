import asyncio
import functools
import os

from weeeTest.config import weeeConfig
from weeeTest.testdata.common.file.yaml.ext.yamlUtil import YamlUtil
from weeeTest.testdata.common.mysql.ext.mysqlUtil import MysqlUtil
from weeeTest.utils.logging import log


class MysqlCommon:
    def mysql(self, sql: str, return_type: str = None, **db_conn):
        """
        :param sql:需要执行的sql
        :param db_conn_env: db连接环境：local,tb1
        :param return_type: 需要返回的类型，默认是list,可以给json
        :param db_conn:  db_conn_env满足不了时，可以配置连接信息（host，user,password,db,port）
        return :返回装饰器
        """
        if sql is None:
            raise FileExistsError("sql不能为空")
        db_conn = db_conn['db_conn']
        if 'host' in db_conn:
            conn = MysqlUtil(host=db_conn.get('host'), user=db_conn.get('user'), password=db_conn.get('password'),
                             db=db_conn.get('db'), port=db_conn.get('port'), return_type=return_type)
        else:
            # base_dir = os.path.dirname(__file__).replace('\\', '/')
            # db_configs = dict(asyncio.run(YamlUtil._read(file_path=base_dir, file_name="db_config.yaml")))
            # conf = db_configs['mysql'][db_conn_env]
            # if conf is None:
            #     raise Exception(f'配置文件中无{db_conn_env}配置')
            # conn = MysqlUtil(host=conf['host'], user=conf['user'], password=conf['password'], db=conf['db'],
            #                  port=conf['port'],
            #                  return_type=return_type)

            # 使用springcloud config
            if weeeConfig.project.lower().strip() in ('ec', "erp"):
                db_config_dict = weeeConfig.db_config.get(weeeConfig.DB_CONFIG_EC_KEY)

            elif weeeConfig.project.lower().strip() == 'wms':
                db_config_dict = weeeConfig.db_config.get(weeeConfig.DB_CONFIG_WMS_KEY)
            else:
                raise Exception(f"不支持project:{weeeConfig.project.lower().strip()}")

            if db_config_dict:
                conn = MysqlUtil(host=db_config_dict['host'], user=db_config_dict['username'],
                                 password=db_config_dict['password'],
                                 port=db_config_dict['port'],
                                 return_type=return_type)
            else:
                raise Exception(f"db_config未获取到{weeeConfig.project.lower().strip()}")

        return self._data(conn=conn, sql=sql)

    @classmethod
    def _data(cls, conn: MysqlUtil, sql: str):
        """
        装饰器
        :param conn:
        :param sql:
        :return:
        """

        def mysql_wrapper(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                log.debug(f'执行sql:{sql}')
                with conn:
                    if sql.lower().startswith("select"):
                        ret = asyncio.run(MysqlUtil.execute_query(conn, sql_str=sql))
                    else:
                        ret = asyncio.run(MysqlUtil.execute_update(conn, sql_str=sql))

                new_args = args + (ret,)
                return func(*new_args, **kwargs)

            return wrapper

        return mysql_wrapper

    @classmethod
    def mysql_param(cls, sql: str):
        if sql is None:
            raise Exception("sql不能为空")
        if weeeConfig.env is not None:
            #     base_dir = os.path.dirname(__file__).replace('\\', '/')
            #     db_configs = dict(asyncio.run(YamlUtil._read(base_dir, file_name="db_config.yaml")))
            #     # conf = db_configs['mysql'][weeeConfig.env]
            #     conf = db_configs.get('mysql').get(weeeConfig.env)
            #     if conf is None:
            #         raise Exception(f'配置文件中无{weeeConfig.env}配置')
            #     # conn = MysqlUtil(host=conf['host'], user=conf['user'], password=conf['password'], db=conf['db'],
            #     #                  port=conf['port'])
            #     with MysqlUtil(host=conf['host'], user=conf['user'], password=conf['password'], db=conf['db'],
            #                    port=conf['port']) as conn:
            #         # 执行查询
            #         if sql.lower().startswith("select"):
            #             ret, columns = asyncio.run(MysqlUtil.execute_query(conn, sql_str=sql, is_return_columns=True))
            #             column_str = ','.join(columns)
            #             if len(ret) == 0:
            #                 raise Exception('mysql_param未查询到任何结果集')
            #             return ret
            #         else:
            #             raise Exception('mysql_param只支持select')
            # else:
            #     raise Exception('weeeConfig.env配置项为None')
            # 使用springcloud config
            if weeeConfig.project.lower().strip() in ('ec', "erp"):
                db_config_dict = weeeConfig.db_config.get(weeeConfig.DB_CONFIG_EC_KEY)

            elif weeeConfig.project.lower().strip() == 'wms':
                db_config_dict = weeeConfig.db_config.get(weeeConfig.DB_CONFIG_WMS_KEY)
            else:
                raise Exception(f"不支持project:{weeeConfig.project.lower().strip()}")

            if db_config_dict:
                with MysqlUtil(host=db_config_dict['host'], user=db_config_dict['username'],
                               password=db_config_dict['password'],
                               port=db_config_dict['port']) as conn:
                    ret = asyncio.run(MysqlUtil.execute_query(conn, sql_str=sql))
                    return ret
            else:
                raise Exception(f"db_config未获取到{weeeConfig.project.lower().strip()}")

# demo
# @mysql_param(sql='select name,age from student ORDER BY id desc limit 2')
# def test_01(name,age):
#     print('111执行test_01')
#     print('返回name', name, 'age', age)
#     # print(args[0])

# @MysqlCommon().mysql(sql='select userId,username from user limit 2', db_conn_env='tb1', return_type='json')
# def test_02(*args):
#     print('111执行test_02')
#     print(args[0])

# @mysql(sql="update student set name='haha' where id>10")
# def test_03(*args):
#     print('111执行test_01')
#     print(args[0])
