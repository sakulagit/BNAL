import os
import sys

from base.read_login import ReadLogin

sys.path.append(os.getcwd())
import allure
from time import sleep
import pytest
from page.page_in import PageIn

arra = []


def get_login_data():
    # 好像直接在读数据里面是有yaml.load(f).values 会出现没有该属性的错误
    for data in ReadLogin("login.yaml").get_login_data().values():
        arra.append((data.get("username"),
                     data.get("password"),
                     data.get("expect_result"),
                     data.get("expect_toast")))
        # 返回的要是参数化需要的列表套元组的形式
    print(arra)
    return arra


class TestLogin():
    def setup_class(self):
        self.login = PageIn().get_login()
        # 无论登录成功还是失败，都需要点击这个，成功之后退出是到首页，需要再次点击我-连接，失败之后还是在原来的页面，直接清空输入
        self.login.page_click_me()
        self.login.page_click_link()

    def teardown_class(self):
        sleep(2)
        self.login.driver.quit()

    # allure.attach("标记描述语法，使用在方法体上")，，step使用在方法上，是描述测试步骤
    # 将图片写入报告allure.attach("描述"，图片流，图片指定格式)

    @allure.step("开始执行测试用例")
    @pytest.mark.parametrize("username,pwd,except_result,expect_toast", get_login_data())
    def test_login(self, username, pwd, except_result, expect_toast):
        print(username, pwd, except_result, expect_toast)
        login = self.login
        # 如果except_result有值就是登陆成功，
        # 如果没有值就是None(除了None,0,False,空，这些是错之外，其他都是True)
        if except_result:
            # 整个登录方法
            login.page_login_all(username, pwd)
            try:
                # 如果登录成功就有昵称，断言正确，断言失败，就是没有登录成功
                assert except_result in login.page_get_nickname()
                # 登录成功之后,---做断言才-----然后才可以点击设置，否则断言的时候已经点过，找不到昵称
                # 也可以在这里使用allure.attach("这个可以标出步骤中的动态数据")
                # 这个不如使用.step(),需要在page里面标出
                login.page_click_setting()
                login.page_out_all()
                # 除了上面的点击我-连接，还需要正确登录后再次点击，失败的则不需要
                login.page_click_me()
                login.page_click_link()
            except:
                # 需要捕获所有异常，如果捕获断言异常会无法获取截图
                # print("登录失败截图,抓取的是所有异常的时候才会截图，&&&&截图存放的文件夹需要自己创建image")
                login.page_get_screenshot()
                # 这里如果raise就会导致之后的代码不再运行
        else:
            login.page_login_all(username, pwd)
            try:
                # 之前没有截图是因为修改了数据里面的toast的值,根本无法获取toast,更无法断言
                assert "登录密码错误a" in login.base_findele_by_text(expect_toast)
                # 上面是为了断言截图的,调试
                # assert expect_toast in login.base_findele_by_text(expect_toast)
            except:
                login.page_get_screenshot()
                # 图片是不指定encoding的
                with open("./image/faild.png", "rb") as f:
                    allure.attach("这里可以写失败原因", f.read(), allure.attach_type.PNG)