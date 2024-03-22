import asyncio
import functools
import os

from weeeTest.config import weeeConfig
from weeeTest.testdata.common.file.yaml.ext.yamlUtil import YamlUtil
from weeeTest.testdata.common.redis.ext.redisUtil import RedisUtil


class RedisCommon:
    def redis(self, key: str, value=None, redis_conn_env: str = 'local', expire_time: int = -1,
              **redis_conn):
        """
        :param expire_time:  过期时间
        :param return_type:  返回数据类型
        :param key:  redis的key
        :param value: 不同类型
        :param redis_conn_env: 读取的是配置文件中的配置
        :param redis_conn: 需要自定义连接时使用
        :return: 返回装饰器
        """
        if key is None:
            raise FileExistsError("key不能为空")
        redis_conn = redis_conn['redis_conn']
        if 'host' in redis_conn:
            conn = RedisUtil(host=redis_conn.get('host'), user=redis_conn.get('user'),
                             password=redis_conn.get('password'),
                             port=redis_conn.get('port'), db=redis_conn.get('db'))
        else:
            base_dir = os.path.dirname(__file__).replace('\\', '/')
            db_configs = dict(asyncio.run(YamlUtil._read(file_path=base_dir, file_name="redis_config.yaml")))
            conf = db_configs['redis'][redis_conn_env]
            if conf is None:
                raise Exception(f'配置文件中无{redis_conn_env}配置')
            conn = RedisUtil(host=conf['host'], user=conf['user'], password=conf['password'], port=conf['port'],
                             db=conf['db'])
        with conn:
            return self._data(conn=conn, key=key, value=value, expire_time=expire_time)

    def _data(self, conn: RedisUtil, key: str, value, expire_time: int = -1):
        def redis_wrapper(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                # value为空时读取
                if value is None:
                    # 获取key类型
                    ret = conn.get_object(key)
                else:
                    # 写入
                    ret = conn.set_object(key=key, value=value, expire_time=expire_time)
                new_args = args + (ret,)
                return func(*new_args, **kwargs)

            return wrapper

        return redis_wrapper

    def redis_param(self, key: str):
        """
        key：查询的key(参数化的key=查询的key)
        select_data_type：查询数据的类型
        """
        if key is None:
            raise Exception("查询key不能为空")
        if weeeConfig.env is not None:
            base_dir = os.path.dirname(__file__).replace('\\', '/')
            db_configs = dict(asyncio.run(YamlUtil._read(base_dir, file_name="redis_config.yaml")))
            conf = db_configs.get('redis').get(weeeConfig.env)
            if conf is None:
                raise Exception(f'配置文件中无{weeeConfig.env}配置')

            with RedisUtil(host=conf['host'], user=conf['user'], password=conf['password'], port=conf['port'],
                           db=conf['db']) as conn:
                ret = conn.get_object(key)
                return [ret]
            # else:
            #     raise Exception('redis目前只支持str,list')
        else:
            raise Exception('weeeConfig.env配置项为None')

    # demo
    # @redis(key='test_list', return_type='list')
    # def test_01(*args):
    #     print('111执行test_01')
    #     print(args[0])
    #
    #
    # @redis(key='test2', return_type='str')
    # def test_02(*args):
    #     print('111执行test_01')
    #     print(args[0])

    # @redis(key='test_str_ex', value='test_str_content', expire_time=60)
    # def test_03(*args):
    #     print('111执行test_01')
    #     print(args[0])

    # @redis(key='test_list_ex', value=[1, 2, 3], expire_time=600)
    # def test_04(*args):
    #     print('111执行test_01')
    #     print(args[0])

    # @redis_param(key='test_str', select_data_type='str')
    # def test_10(test_str):
    #     '''
    #     读取redis-str参数化
    #     '''
    #     print('111执行test_01')
    #     print(test_str)

    # @redis_param(key='test_str')
    # def test_11(self, a):
    #     '''
    #     读取redis-list参数化：参数化的key=查询的key
    #     '''
    #     print('111执行test_01')
    #     print(a)
