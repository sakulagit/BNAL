"""
    目标：完成po模式 base基类(工具类封装)
    操作：
        1. 根据业务逻辑梳理出，需要的公共方法
        2. 方法：
            1). 定位
            2). 输入
            3). 点击
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
class Base():
    def __init__(self, driver):
        self.driver = driver

    def base_find_element(self, ByMet, tm=30, poll=0.5):
        return WebDriverWait(self.driver, timeout=tm, poll_frequency=poll).until(lambda x: x.find_element(*ByMet))

    def base_input(self, ByMet, text):
        ele = self.base_find_element(ByMet)
        ele.clear()
        ele.send_keys(text)

    def base_click(self, ByMet):
        self.base_find_element(ByMet).click()

    # 获取元素文本
    def base_get_text(self, ByMet):
        #
        return self.base_find_element(ByMet).text

    # 截图
    def base_get_screenshot(self):
        # 与pytest.ini平级,写死,这个文件夹必须自己创建
        self.driver.get_screenshot_as_file("./image/faild.png")

    # 拖拽
    def base_drag_and_drop(self, ele1, ele2):
        # 从ele1拖拽到ele2
        self.driver.drag_and_drop(ele1, ele2)

    # 通过文本找元素  就是对Toast的封装，只可以使用Xpath,内容包含
    def base_findele_by_text(self, text):
        ByMet = By.XPATH, "//*[contains(@text,'" + text + "')]"
        self.base_find_element(ByMet, tm=3, poll=0.1)

    # 通过文本找到元素，并点击地区元素
    def base_click_area(self, text):
        self.base_findele_by_text(text).click()

    # 查找一组元素
    def base_receiver_elements(self, ByMet, tm=30, poll=0.5):
        return WebDriverWait(self.driver, timeout=tm, poll_frequency=poll).until(lambda x: x.find_elements(*ByMet))
