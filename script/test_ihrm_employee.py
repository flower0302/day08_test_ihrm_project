# 如果能够把员工管理模块实现,n那么证明大家通过接口测试没太大问题


# 导包
import unittest
import logging
import requests
from untils import assert_common


# 创建测试类,集成unittest.TestCase
class TestIHRMEmployee(unittest.TestCase):
    # 初始化测试类
    def setUp(self):
        self.login_url = "http://ihrm-test.itheima.net" + "/api/sys/login"
        self.emp_url = "http://ihrm-test.itheima.net" + "/api/sys/user"
        from api.emmployee_api import TestEmployeeApi
        self.emp_api = TestEmployeeApi()  # 员工实例化
        from api.login_api import TestLoginApi  # 登录实例化
        self.login_api = TestLoginApi()

    def tearDown(self):
        pass

    # def add_emp(self, headers, username, mobile):
    #     # 添加员工
    #     response = requests.post(self.emp_url,
    #                              json={
    #                                  "username": username,
    #                                  "mobile": mobile,
    #                                  "timeOfEntry": "2020-05-05",
    #                                  "formOfEmployment": 1,
    #                                  "workNumber": "1234123",
    #                                  "departmentName": "测试部",
    #                                  "departmentId": "1063678149528784896",
    #                                  "correctionTime": "2020-05-17T16:00:00.000Z"
    #                              },
    #                              headers=headers)
    #     return response

    # 创建测试员工增删改查的函数
    def test01_employee_manage(self):
        # 实现员工的增删改查
        pass
        # 登录
        response = self.login_api.login({"mobile":"13800000002","password":"123456"},
                                            {"Content-Type": "application/json"})
        # 打印登录的数据
        print("登录的结果为:{}".format(response.json()))
        # 提取令牌
        token = response.json().get("data")
        # 保存令牌到请求头当中
        headers = {"Content-Type": "application/json", 'Authorization': "Bearer " + token}
        # 打印令牌
        print("请求头令牌:", headers)
        logging.info("请求头中令牌: {}".format(response.json()))
        # # 添加员工
        # response = requests.post(self.emp_url,
        #                          json={
        #                              "username": "兰生222235",
        #                              "mobile": "17556908872",
        #                              "timeOfEntry": "2020-05-05",
        #                              "formOfEmployment": 1,
        #                              "workNumber": "1234123",
        #                              "departmentName": "测试部",
        #                              "departmentId": "1063678149528784896",
        #                              "correctionTime": "2020-05-17T16:00:00.000Z"
        #                          },
        #                          headers=headers)
        response = self.emp_api.add_emp(headers,
                                        "拿过仑super0083", "17888789906")
        # 打印添加的结果
        # print("添加员工的结果为:", response.json())
        logging.info("添加员工的结果为: {}".format(response.json()))
        # 提取添加员工中的id
        emp_id = response.json().get("data").get("id")
        # 断言
        assert_common(200, True, 10000, "操作成功", response, self)

        # 查询员工
        # # query_url = self.emp_url + "/" + emp_id
        # print("查询员工的URL为:", query_url)
        # 发送查询员工的请求
        response = self.emp_api.query_emp(emp_id, headers)
        # print("查询员工的结果为:", response.json())
        logging.info("查询员工的结果为:{}".format(response.json()))
        # 断言
        assert_common(200, True, 10000, "操作成功", response, self)

        # 修改员工
        # modify_url = self.emp_url + "/" + emp_id
        # response = requests.put(url=modify_url, json={"username":"贝克汉姆"}, headers=headers)

        response =self.emp_api.modify_emp(emp_id,
                                          headers,
                                          "贝克汉姆")
        # 打印修改的结果
        # print("修改员工的结果为:", response.json())
        # 打印删除的结果
        logging.info("修改员工的结果为:{}".format(response.json()))
        # 断言
        assert_common(200, True, 10000, "操作成功", response, self)


        # 删除员工
        # delete_url = self.emp_url + "/" + emp_id
        # 发送删除员工的请求
        # response = requests.delete(url=delete_url, headers=headers)
        response = self.emp_api.delete_emp(emp_id,headers)
        # 打印删除的结果
        # print("删除的结果为:", response.json())
        # 打印删除的结果
        logging.info("删除的结果为:{}".format(response.json()))
        # 断言
        assert_common(200,True, 10000, "操作成功", response, self)