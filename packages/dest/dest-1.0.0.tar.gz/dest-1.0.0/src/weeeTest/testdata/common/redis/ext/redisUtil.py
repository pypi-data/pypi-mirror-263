import redis

from weeeTest.utils.logging import log


class RedisUtil:
    def __init__(self, host: str, user: str = None, password: str = None, port: int = 6379, db: int = 0):
        self.host = host
        self.user = user
        self.password = str(password)
        self.db = db
        self.port = port

    def __enter__(self):
        self.conn = redis.StrictRedis(host=self.host, username=self.user, password=self.password, port=self.port,
                                      db=self.db,
                                      decode_responses=True)
        if self.conn is None:
            raise Exception("redis连接建立失败,请确认连接信息")
        else:
            log.debug("redis连接建立成功")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn is not None:
            self.conn.close()
            log.debug('关闭连接成功')

    def get_object(self, key: str, start: int = 0, end: int = -1) -> any:
        """
        获取str格式的value
        :param key: 需要获取的key
        :param start:开始下标
        :param end:结束下标
        :return: 返回str、list
        """
        key_type = str(self.conn.type(key))
        # print("key_type::", key_type)
        if 'string' == key_type.lower():
            return self.conn.get(key)
        elif 'list' == key_type.lower():
            return self.conn.lrange(key, start, end)
        else:
            raise Exception(f'获取的数据类型是{key_type}, 目前支持str,list')

    def set_object(self, key: str, value: any, expire_time: int = -1) -> bool:
        """
        写入str格式的数据
        :param key: key
        :param value: 值
        :param expire_time: 超时时间，秒；默认-1永久有效
        :return: 是否成功
        """
        if isinstance(value, str):
            if expire_time == -1:
                return self.conn.set(key, value)
            else:
                return self.conn.setex(key, expire_time, value)
        elif isinstance(value, list):
            result = self.conn.lpush(key, *[str(x) for x in list(value)])
            if expire_time != -1:
                self.conn.expire(name=key, time=expire_time)
            return result


if __name__ == '__main__':
    # str
    # conn = RedisUtil(host='localhost', password='123456', port=6379, db=0)
    # # result = asyncio.run(RedisUtil.set_str(conn, 'test2', 'helloworld2'))
    # result_word = RedisUtil.get_object(conn, key='test_list', start=0, end=1)
    # print(type(result_word), result_word)

    # r = RedisUtil(host='localhost', password='123456', port=6379, db=0)
    with RedisUtil(host='localhost', password='123456', port=6379, db=0) as r:
        result_word = r.get_object(key='test_list', start=0, end=1)
        print(type(result_word), result_word)

    # list
    # list_values=['1111helloworld1', '2222helloworld2']
    # result = asyncio.run(
    #     RedisUtil.set_list(conn, 'test_list22', *list_values, expire_time=1000))
    # result_word = asyncio.run(RedisUtil.get_list(conn, 'test_list'))
    # print(type(result_word), result_word)
