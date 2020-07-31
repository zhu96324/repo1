import allure
from selenium.webdriver.common.by import By
from base.base_login import BaseLogin


class RegisterPage(BaseLogin):

    # 已有账号，去登录
    login_button = By.XPATH, "//*[@text='已有账号，去登录']"

    @allure.step(title='注册 点击 登录页面')
    # 点击 已有账号，去登录
    def click_login(self):
        self.base_click(self.login_button)