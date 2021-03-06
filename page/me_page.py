import time

import allure
from selenium.webdriver.common.by import By
from base.base_login import BaseLogin


class MePage(BaseLogin):

    # 昵称
    nick_name_text_view = By.ID, "com.yunmall.lc:id/tv_user_nikename"
    # 设置按钮
    setting_button = By.ID, "com.yunmall.lc:id/ymtitlebar_left_btn_image"
    # 加入超级VIP
    be_vip_button = By.XPATH, "//*[@text='加入超级VIP']"

    @allure.step(title='我 获取 昵称')
    def get_nick_name_text(self):
        return self.base_find_element(self.nick_name_text_view).text

    @allure.step(title='我 点击 设置')
    def click_setting(self):
        self.base_find_element_with_scroll(self.setting_button).click()

    @allure.step(title='我 点击 加入')
    def click_be_vip(self):
        self.base_find_element_with_scroll(self.be_vip_button).click()
        time.sleep(3)