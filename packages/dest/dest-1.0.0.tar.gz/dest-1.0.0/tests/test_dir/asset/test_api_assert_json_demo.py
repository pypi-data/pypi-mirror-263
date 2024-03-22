# !/usr/bin/python3
# -*- coding: utf-8 -*-

import weeeTest
from weeeTest import genson
import pytest


class TestApiAssertJson(weeeTest.TestCase):
    """
    测试4中请求方式，get、post、put、delete，以及带token的请求，以及断言
    """

    def test_login_asser_json(self):
        """
        登录获取token
        """

        # 接口参数
        json = {
            "username": "admin",
            "password": "password@123"
        }
        # 接口调用
        self.post('/api/v1/auth/login', json=json)
        # 断言数据
        assert_data = {
            "username": "admin"
        }
        self.assert_json(assert_data, self.response["data"]["user"])


class TestApiAssertPathJson(weeeTest.TestCase):
    """
    测试4中请求方式，get、post、put、delete，以及带token的请求，以及断言
    """

    def test_login_asser_path_json(self):
        """
        登录获取token
        """

        # 接口参数
        json = {
            "username": "admin",
            "password": "password@123"
        }
        # 接口调用
        self.post('/api/v1/auth/login', json=json)
        # 断言数据
        self.assert_json_path("data.user.username", "admin")


class TestApiAssertSchemaJson(weeeTest.TestCase):
    """
    测试4中请求方式，get、post、put、delete，以及带token的请求，以及断言
    """

    def test_login_asser_path_json(self):
        """
        登录获取token
        """

        # 接口参数
        json = {
            "username": "admin",
            "password": "password@123"
        }
        # 接口调用
        self.post('/api/v1/auth/login', json=json)

        # 生成数据结构和类型
        schema = genson(self.response["data"])
        print("json Schema: \n", schema)

        # 断言数据结构和类型
        assert_data = {
            "$schema": "http://json-schema.org/schema#",
            "type": "object",
            "properties": {
                "token": {
                    "type": "string"
                },
                "userId": {
                    "type": "integer"
                },
                "user": {
                    "type": "object",
                    "properties": {
                        "id": {
                            "type": "integer"
                        },
                        "username": {
                            "type": "string"
                        },
                        "email": {
                            "type": "string"
                        },
                        "nickname": {
                            "type": "string"
                        },
                        "fullname": {
                            "type": "string"
                        },
                        "role": {
                            "type": "integer"
                        },
                        "source": {
                            "type": "string"
                        },
                        "avatar": {
                            "type": "null"
                        },
                        "is_valid": {
                            "type": "boolean"
                        },
                        "phone": {
                            "type": "string"
                        },
                        "sex": {
                            "type": "string"
                        },
                        "status": {
                            "type": "boolean"
                        },
                        "desc": {
                            "type": "string"
                        },
                        "created_at": {
                            "type": "string"
                        },
                        "updated_at": {
                            "type": "string"
                        },
                        "is_deleted": {
                            "type": "integer"
                        },
                        "update_user": {
                            "type": "integer"
                        },
                        "last_login_at": {
                            "type": "string"
                        },
                        "client_host": {
                            "type": "null"
                        }
                    },
                    "required": [
                        "avatar",
                        "client_host",
                        "created_at",
                        "desc",
                        "email",
                        "fullname",
                        "id",
                        "is_deleted",
                        "is_valid",
                        "last_login_at",
                        "nickname",
                        "phone",
                        "role",
                        "sex",
                        "source",
                        "status",
                        "update_user",
                        "updated_at",
                        "username"
                    ]
                },
                "expire": {
                    "type": "integer"
                }
            },
            "required": [
                "expire",
                "token",
                "user",
                "userId"
            ]
        }

        # 断言数据
        self.assert_schema(assert_data, self.response["data"])


if __name__ == '__main__':
    pytest.main(base_url="https://papi.tb1.sayweee.net", debug=True)
