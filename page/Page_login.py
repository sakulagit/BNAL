import allure

import page
from base.base import Base


class PageLogin(Base):
    # base导包要正确
    # 我
    @allure.step("点击我")
    def page_click_me(self):
        self.base_click(page.click_me)

    # 点击有账号去登录链接
    @allure.step("已有账号去登录")
    def page_click_link(self):
        self.base_click(page.click_link)

    # 账号
    @allure.step("输入账号")
    def page_input_username(self, username):
        self.base_input(page.input_username, username)

    # 密码
    @allure.step("输入密码")
    def page_input_pwd(self, pwd):
        self.base_input(page.input_pwd, pwd)

    # 登录
    @allure.step("点击登录")
    def page_click_login(self):
        self.base_click(page.click_login)

    # 昵称
    @allure.step("获取昵称")
    def page_get_nickname(self):
        #
        return self.base_get_text(page.get_nickname)

    # 设置
    @allure.step("点击设置")
    def page_click_setting(self):
        self.base_click(page.click_setting)

    # 登录输入账号密码点击登录
    # @allure.step("输入账号密码并登录")都写太乱
    def page_login_all(self, username, pwd):
        self.page_input_username(username)
        self.page_input_pwd(pwd)
        self.page_click_login()

    # 失败截图
    @allure.step("失败截图")
    def page_get_screenshot(self):
        # 截图存放的文件夹需要自己创建
        self.base_get_screenshot()

    # 滑动到显示出退出的位置
    @allure.step("滑动到下面")
    def page_drag_drop(self):
        # 把1拖拽到2  所以1就是下面的
        send_message = self.base_find_element(page.send_msg)
        modify_password = self.base_find_element(page.modify_pwd)
        self.base_drag_and_drop(send_message, modify_password)

    # 退出
    @allure.step("退出")
    def page_click_out(self):
        self.base_click(page.click_out)

    # 确认退出
    @allure.step("确认退出")
    def page_click_assureout(self):
        self.base_click(page.click_assureout)

    # 封装以上三个方法，直接退出
    # @allure.step("滑动退出并确认")
    def page_out_all(self):
        self.page_drag_drop()
        self.page_click_out()
        self.page_click_assureout()
