from time import sleep

import allure
from selenium.webdriver.common.by import By

from base.base_login import BaseLogin


class VipPage(BaseLogin):

    # 邀请码 输入框
    invite_eddit_text = By.XPATH, "//*[@type='tel']"
    # 立即成为会员
    be_vip_button = By.XPATH, "//*[@value='立即成为会员']"

    @allure.step(title='vip页面 输入 邀请码')
    def input_invite(self, text):
        self.base_input(self.invite_eddit_text, text)

    @allure.step(title='vip页面 点击 立即成为会员')
    def click_be_vip(self):
        self.base_click(self.be_vip_button)