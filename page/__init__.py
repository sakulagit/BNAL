from selenium.webdriver.common.by import By

# 我，已有账号，账号，密码，登录
click_me = By.ID, "com.yunmall.lc:id/tab_me"
click_link = By.ID, "com.yunmall.lc:id/textView1"
input_username = By.ID, "com.yunmall.lc:id/logon_account_textview"
input_pwd = By.ID, "com.yunmall.lc:id/logon_password_textview"
click_login = By.ID, "com.yunmall.lc:id/logon_button"
# 昵称
get_nickname = By.ID, "com.yunmall.lc:id/tv_user_nikename"
# 设置，退出，确认
click_setting = By.ID, "com.yunmall.lc:id/ymtitlebar_left_btn_image"
click_out = By.ID, "com.yunmall.lc:id/setting_logout"
click_assureout = By.ID, "com.yunmall.lc:id/ymdialog_right_button"

# 改密码，消息推送
modify_pwd = By.ID, "com.yunmall.lc:id/setting_modify_pwd"
send_msg = By.ID, "com.yunmall.lc:id/setting_notification"

# 地址管理的数据
address_manage = By.ID, "com.yunmall.lc:id/setting_address_manage"
# 新增地址
address_add_new = By.ID, "com.yunmall.lc:id/address_add_new_btn"
# 收件人
address_receipt_name = By.ID, "com.yunmall.lc:id/address_receipt_name"
# 电话
address_add_phone = By.ID, "com.yunmall.lc:id/address_add_phone"
# 所在区域
address_area = By.ID, "com.yunmall.lc:id/address_province"
# 省  id重复 只能使用text

# 市  class = "android.widget.RelativeLayout"
shi = By.ID, "com.yunmall.lc:id/area_title"
# 区 使用 text

# 输入详细地址
address_detail_addr_info = By.ID, "com.yunmall.lc:id/address_detail_addr_info"
# 输入邮编
address_post_code = By.ID, "com.yunmall.lc:id/address_post_code"
# 设为默认地址
address_default = By.ID, "com.yunmall.lc:id/address_default"
# 保存
address_save = By.ID, "com.yunmall.lc:id/button_send"

# 收件人列表
add_receive_list = By.ID, "com.yunmall.lc:id/receipt_name"
