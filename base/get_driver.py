from appium import webdriver


def getDriver():
    # server 启动参数
    desired_caps = {}
    # 设备信息
    desired_caps['platformName'] = 'Android'
    # 模拟器信息
    desired_caps['platformVersion'] = '5.1.1'
    desired_caps['deviceName'] = '172.16.2.15:5554'

    # 以下两条是小米的数据
    # desired_caps['platformVersion'] = '6.0.1'
    # desired_caps['deviceName'] = '192.168.0.101:5555'
    # 指定appium库
    desired_caps['automationName'] = 'uiautomator2'
    # app信息百年奥莱
    desired_caps['appPackage'] = 'com.yunmall.lc'
    desired_caps['appActivity'] = 'com.yunmall.ymctoc.ui.activity.MainActivity'
    # 输入中文
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    # 获取driver
    return webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
