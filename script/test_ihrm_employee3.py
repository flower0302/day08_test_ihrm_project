# 如果能够把员工管理模块实现,n那么证明大家通过接口测试没太大问题


# 导包
import unittest
import logging
import requests
import app
from untils import assert_common


# 创建测试类,集成unittest.TestCase
class TestIHRMEmployee3(unittest.TestCase):

    # 初始化测试类
    def setUp(self):
        self.login_url = "http://ihrm-test.itheima.net" + "/api/sys/login"
        self.emp_url = "http://ihrm-test.itheima.net" + "/api/sys/user"
        from api.emmployee_api import TestEmployeeApi
        self.emp_api = TestEmployeeApi()  # 员工实例化
        from api.login_api import TestLoginApi
        self.login_api = TestLoginApi()  # 登录实例化

    # 编写测试函数
    def test01_login(self):
        # 实现员工的增删改查
        # 登录
        response = self.login_api.login({"mobile": "13800000002", "password": "123456"},
                                        {"Content-Type": "application/json"})
        # 打印登录的数据
        print("登录的结果为:{}".format(response.json()))
        # 提取令牌
        token = response.json().get("data")
        # 保存令牌到请求头当中
        headers = {"Content-Type": "application/json", 'Authorization': "Bearer " + token}
        app.HEADERS = headers
        # 打印令牌
        logging.info("保存到全局变量app中的其你去提为: {}".format(app.HEADERS))
    # 添加员工
    def test02_add_emp(self):
        response = self.emp_api.add_emp(app.HEADERS,
                                        "拿赢仑super0083", "17892789906")
        # 打印添加的结果
        logging.info("添加员工的结果为: {}".format(response.json()))
        # 提取添加员工中的id
        emp_id = response.json().get("data").get("id")
        app.EMPID = emp_id  # 保存emp_id到全局变量app.py中
        # 断言
        assert_common(200, True, 10000, "操作成功", response, self)

    # 查询员工
    def test03_query_emp(self):

        # 发送查询员工的请求
        response = self.emp_api.query_emp(app.EMPID,app.HEADERS)
        logging.info("查询员工的结果为:{}".format(response.json()))
        # 断言
        assert_common(200, True, 10000, "操作成功", response, self)
    # 修改员工
    def test04_modify_emp(self):
        response = self.emp_api.modify_emp(app.EMPID,
                                           app.HEADERS,
                                           "贝克汉姆")
        # 打印修改的结果
        # print("修改员工的结果为:", response.json())
        # 打印删除的结果
        logging.info("修改员工的结果为:{}".format(response.json()))
        # 断言
        assert_common(200, True, 10000, "操作成功", response, self)

    # 删除员工
    def test05_delete_emp(self):
        response = self.emp_api.delete_emp(app.EMPID, app.HEADERS)
        # 打印删除的结果
        # print("删除的结果为:", response.json())
        # 打印删除的结果
        logging.info("删除的结果为:{}".format(response.json()))
        # 断言
        assert_common(200, True, 10000, "操作成功", response, self)

