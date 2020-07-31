import allure
from selenium.webdriver.common.by import By

from base.base_login import BaseLogin

class AboutPage(BaseLogin):

    # 版本更新 按钮
    update_button = By.XPATH, "//*[@text='版本更新']"

    @allure.step(title='关于百年奥莱 点击 更新版本')
    # 点击 版本更新
    def click_update(self):
        self.base_click(self.update_button)
