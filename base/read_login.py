import os

import yaml

class ReadLogin():
    def __init__(self, filename):
        # 定义一个全局参数，使用self，把传入的参数赋值给全局参数
        # 使用的时候必传就定义在初始化方法中
        self.filename = os.getcwd() + os.sep + "data" + os.sep + filename

    def get_login_data(self):
        with open(self.filename, encoding="utf-8") as f:
            return yaml.load(f)

    # # 只适合右键调试，配合下面的方法,如果再配合ini使用，只需要ini参数传空即可
    # def getdata1(self):
    #     with open("../data/login.yaml", "r", encoding="utf-8") as f:
    #         for data in yaml.load(f).values():
    #             arra.append((data.get("username"),
    #                          data.get("password"),
    #                          data.get("expect_result"),
    #                          data.get("expect_toast")))
    #         print(arra)

# if __name__ == '__main__':
#     ReadLogin("").getdata1()
