# !/usr/bin/python3
# -*- coding: utf-8 -*-
import pytest

import weeeTest


class TestRequest(weeeTest.TestCase):
    """
    测试4中请求方式，get、post、put、delete，以及带token的请求，以及断言
    """

    @weeeTest.mark.fixture(scope='class')
    def login(self):
        """
        登录获取token
        """

        self.post('/api/v1/auth/login', json={'username': 'admin', 'password': 'password@123'})
        return self.response['data']['token']

    def test_post_method(self, login):
        """
        测试post请求
        """
        json = {
            "username": "testuser",
            "nickname": "测试用户",
            "fullname": "Testuser",
            "password": "password@123",
            "email": "admin@123.com",
            "phone": "13800000001",
            "sex": "0",
            "status": True,
            "desc": "备注"
        }
        self.post('/api/v1/user/add', json=json, headers={'Authorization': 'Bearer ' + login})
        self.assert_status_code(200)
        assert self.response['code'] == 20000

    def test_put_method(self, login):
        """
        测试put请求
        """
        self.put('/api/v1/user/updateInfo', json={"desc": "测试2"}, headers={'Authorization': 'Bearer ' + login})
        self.assert_status_code(200)
        assert self.response['code'] == 20000

    def test_get_method(self, login):
        """
        测试get请求
        """
        self.get('/api/v1/user/list', params="username=testuser", headers={'Authorization': 'Bearer ' + login})
        self.assert_status_code(200)
        assert self.response['code'] == 20000
        user_id = self.response['data'][0]['id']
        return user_id

    def test_delete_method(self, login):
        """
        测试delete请求
        """
        res = self.delete('/api/v1/user/delete', params="user_id=" + str(self.test_get_method(login)),
                          headers={'Authorization': 'Bearer ' + login})
        self.assert_status_code(200)
        assert self.response['code'] == 20000


if __name__ == '__main__':
    pytest.main(base_url="https://papi.tb1.sayweee.net", debug=True)
