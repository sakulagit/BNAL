import allure

from base.get_driver import getDriver
from page.Page_login import PageLogin


class PageIn():
    @allure.step("实例化页面对象")
    def get_login(self):
        return PageLogin(getDriver())
