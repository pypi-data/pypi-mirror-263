import asyncio
import json
from decimal import *

import pymysql
from pymysql.cursors import Cursor
from sshtunnel import SSHTunnelForwarder

from weeeTest.utils.logging import log


class MysqlUtil:
    """
    return_type==None时返回list,1返回json数组str
    """

    def __init__(self, host: str, user: str, password: str, db: str = "", port: int = 3306, return_type: str = None):
        self.host = host
        self.user = user
        self.password = str(password)
        self.db = db
        self.port = int(port)
        self.return_type = return_type

    def __enter__(self):
        try:
            self.ssh = None
            if 'tb1' in self.host:
                # ssh跳板机
                self.ssh = SSHTunnelForwarder(
                    ('18.216.15.90', 2222),
                    ssh_password='nSzcEyfSthSUdjPF',
                    ssh_username='weee_tmp',
                    remote_bind_address=(self.host, self.port),
                    local_bind_address=('127.0.0.1', 13307))
                self.ssh.start()
                log.debug("ssh建立成功")
                if self.return_type is None:
                    self.conn = pymysql.connect(host='127.0.0.1', user=self.user, password=self.password, db=self.db,
                                                port=13307, charset='utf8')
                elif "json" in self.return_type:
                    self.conn = pymysql.connect(host='127.0.0.1', user=self.user, password=self.password, db=self.db,
                                                port=13307, charset='utf8', cursorclass=pymysql.cursors.DictCursor)
                else:
                    raise Exception(f'不支持{self.return_type}类型')
            else:
                if self.return_type is None:
                    self.conn = pymysql.connect(host=self.host, user=self.user, password=self.password, db=self.db,
                                                port=self.port, charset='utf8')
                elif "json" in self.return_type:
                    self.conn = pymysql.connect(host=self.host, user=self.user, password=self.password, db=self.db,
                                                port=self.port, charset='utf8', cursorclass=pymysql.cursors.DictCursor)
                else:
                    raise Exception(f'不支持{self.return_type}类型')
            if self.conn is None:
                raise Exception("建立数据库连接失败,请确认连接信息")
            else:
                log.debug("成功建立数据库连接")
        except RuntimeError as e:
            raise '连接失败，请确认连接信息'
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn is not None:
            self.conn.close()
            log.debug("关闭数据库连接")
        if self.ssh is not None:
            self.ssh.close()
            log.debug("ssh关闭成功")

    # async def get_connect(self) -> Connection:
    #     try:
    #         if self.return_type is None:
    #             return pymysql.connect(host=self.host, user=self.user, password=self.password, db=self.db,
    #                                    port=self.port, charset='utf8')
    #         elif "json" in self.return_type:
    #             return pymysql.connect(host=self.host, user=self.user, password=self.password, db=self.db,
    #                                    port=self.port, charset='utf8', cursorclass=pymysql.cursors.DictCursor)
    #         else:
    #
    #             raise Exception(f'不支持{self.return_type}类型')
    #     except RuntimeError as e:
    #         raise '连接失败，请确认连接信息'

    async def execute_query(self, sql_str: str, is_return_columns: bool = False):
        # conn = await MysqlUtil.get_connect(self)
        cur = self.conn.cursor()
        cur.execute(sql_str)
        if self.return_type is None:
            select_result = list(cur.fetchall())
        elif "json" in self.return_type:
            select_result = json.dumps(list(cur.fetchall()), ensure_ascii=False, cls=DecimalEncoder)
        else:
            raise Exception(f'不支持{self.return_type}类型')
        if is_return_columns:
            columns = [desc[0] for desc in cur.description]
            cur.close()
            # conn.close()
            return select_result, columns
        else:
            cur.close()
            # conn.close()
            return select_result

    async def execute_update(self, sql_str: str) -> int:
        # conn = await MysqlUtil.get_connect(self)
        cur = self.conn.cursor()
        i = cur.execute(sql_str)
        self.conn.commit()
        cur.close()
        # conn.close()
        return i

    async def execute_update_data_sql(self, sql_str: str, data: tuple) -> int:
        """
        sql_str:str语句
        data:占位符数据
        """
        cur = self.conn.cursor()
        i = cur.execute(sql_str, data)
        self.conn.commit()
        cur.close()
        # conn.close()
        return i


class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        # 👇️ if passed in object is instance of Decimal
        # convert it to a string
        if isinstance(obj, Decimal):
            return str(obj)
        if isinstance(obj, bytes):
            return int(obj)
        # 👇️ otherwise use the default behavior
        return json.JSONEncoder.default(self, obj)


if __name__ == '__main__':
    # sql = "insert student(name,age,sum)value('test11',191,10010)"
    # ret = asyncio.run(MysqlUtil.execute_update(MysqlUtil('localhost', 'root', '123456', 'test_db', 3306), sql_str=sql))
    # print(ret, type(ret))

    sql = "insert student(name,age,sum)value(%s,%s,%s)"
    data = ("value1", 123, 222)
    with MysqlUtil('localhost', 'root', '123456', 'test_db', 3306) as conn:
        ret = asyncio.run(
            MysqlUtil.execute_update_data_sql(conn, sql_str=sql,
                                              data=data))
        print(ret, type(ret))

    # sql = "select id from student  ORDER BY id desc limit 2"
    # conn = MysqlUtil('localhost', 'root', '123456', 'test_db', 3306, 'json')
    # ret = asyncio.run(
    #     MysqlUtil.execute_query(conn, sql_str=sql))
    # print(ret, type(ret))

    # sql = "select userId from `user`  limit 10"
    # with MysqlUtil('weee.db.tb1.sayweee.net', 'yingqing.shan', 'VtXmZT^36stRk##E', 'weee', 3306, 'json') as conn:
    #     ret = asyncio.run(
    #         MysqlUtil.execute_query(conn, sql_str=sql))
    #     print(ret, type(ret))

    # sql = "select id from student  ORDER BY id desc limit 2"
    # with MysqlUtil('localhost', 'root', '123456', 'test_db', 3306, 'json') as conn:
    #     ret = asyncio.run(
    #         MysqlUtil.execute_query(conn, sql_str=sql))
    #     print(ret, type(ret))

    # sql = "select id from student  ORDER BY id desc limit 2"
    # conn = MysqlUtil('localhost', 'root', '123456', 'test_db', 3306, 'json')
    # ret = asyncio.run(
    #     MysqlUtil.execute_query(conn, sql_str=sql))
    # print(ret, type(ret))

    # sql = "select id,url from swagger_doc limit 2"
    # ret = asyncio.run(MysqlUtil.execute_query(MysqlUtil('dev2.qa.sayweee.net', 'root', 'Dev123#passwd', 'lest', 3306), sql_str=sql))

    # sql1 = "update swagger_doc set cover_status=1 where id=1"
    # ret = asyncio.run(MysqlUtil.execute_update(MysqlUtil('localhost', 'root', '123456', 'data', 3306), sql_str=sql1))
    # print(ret, type(ret))
