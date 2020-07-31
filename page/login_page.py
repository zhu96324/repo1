import allure
from selenium.webdriver.common.by import By

from base.base_login import BaseLogin


class LoginPage(BaseLogin):

    # 用户名
    username_edit_text = By.ID, "com.yunmall.lc:id/logon_account_textview"

    # 密码
    password_eddit_text = By.ID, "com.yunmall.lc:id/logon_password_textview"

    # 登录按钮
    login_button = By.ID, "com.yunmall.lc:id/logon_button"

    # 输入用户名
    @allure.step(title='登录页面 输入 用户名')
    def input_username(self, text):
        allure.attach(text, "输入", allure.attachment_type.TEXT)
        self.base_input(self.username_edit_text, text)

    @allure.step(title='登录页面 输入 密码')
    # 输入密码
    def input_password(self, text):
        allure.attach(text, "输入", allure.attachment_type.TEXT)
        self.base_input(self.password_eddit_text, text)

    @allure.step(title='登录页面 点击 登录')
    # 点击登录
    def click_login(self):
        self.base_click(self.login_button)
