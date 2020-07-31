import random
import time

import allure
from selenium.webdriver.common.by import By

from base.base_login import BaseLogin


class EditAddressPage(BaseLogin):

    # 收件人 输入框
    name_edit_text = By.ID, "com.yunmall.lc:id/address_receipt_name"

    # 手机号 输入框
    phone_edit_text = By.ID, "com.yunmall.lc:id/address_add_phone"

    # 详细地址 输入框
    info_edit_text = By.ID, "com.yunmall.lc:id/address_detail_addr_info"

    # 邮编 输入框
    post_code_edit_text = By.ID, "com.yunmall.lc:id/address_post_code"

    # 设为默认地址 按钮
    default_address_button = By.ID, "com.yunmall.lc:id/address_default"

    # 所在地区 按钮
    region_button = By.ID, "com.yunmall.lc:id/address_province"

    # 省市区的特征
    area_feature = By.ID, "com.yunmall.lc:id/area_title"

    # 保存 按钮
    save_button = By.ID, "com.yunmall.lc:id/button_send"

    @allure.step(title='编辑地址 输入 收件人')
    # 输入 收件人信息
    def input_name(self, text):
        allure.attach(text, "输入", allure.attachment_type.TEXT)
        self.base_input(self.name_edit_text, text)
        allure.attach(self.driver.get_screenshot_as_png(), "截图", allure.attachment_type.PNG)

    @allure.step(title='编辑地址 输入 手机号')
    # 输入 手机号
    def input_phone(self, text):
        allure.attach(text, "输入", allure.attachment_type.TEXT)
        self.base_input(self.phone_edit_text, text)
        allure.attach(self.driver.get_screenshot_as_png(), "截图", allure.attachment_type.PNG)

    @allure.step(title='编辑地址 输入 详细地址')
    # 输入 详细地址
    def input_info(self, text):
        allure.attach(text, "输入", allure.attachment_type.TEXT)
        self.base_input(self.info_edit_text, text)
        allure.attach(self.driver.get_screenshot_as_png(), "截图", allure.attachment_type.PNG)

    @allure.step(title='编辑地址 输入 邮编')
    # 输入 邮编
    def input_post_code(self, text):
        allure.attach(text, "输入", allure.attachment_type.TEXT)
        self.base_input(self.post_code_edit_text, text)
        allure.attach(self.driver.get_screenshot_as_png(), "截图", allure.attachment_type.PNG)

    @allure.step(title='编辑地址 点击 默认地址')
    # 点击 设为默认地址按钮
    def click_default_address(self):
        self.base_click(self.default_address_button)

    @allure.step(title='编辑地址 点击 所在地区')
    # 点击 所在地区 按钮
    def click_region_button(self):
        self.base_click(self.region_button)

    @allure.step(title='选择区域')
    # 进入 所在地区 并且选择一个随机的区域
    def choose_region(self):
        self.click_region_button()
        time.sleep(1)
        while True:
            if self.driver.current_activity != "com.yunmall.ymctoc.ui.activity.ProvinceActivity":
                return
            # 所有的可选的省市区
            areas = self.base_find_elements(self.area_feature)
            # 所有的可选个数
            areas_count = len(areas)
            # 随机数下标
            area_index = random.randint(0, areas_count-1)
            # 获取随机下标对应的城市
            areas[area_index].click()

            time.sleep(1)

    @allure.step(title='编辑地址 点击 保存')
    # 点击保存按钮
    def click_save_button(self):
        self.base_click(self.save_button)

