import allure
from selenium.webdriver.common.by import By

from base.base_login import BaseLogin


class AddressListPage(BaseLogin):

    # 新增地址 按钮
    add_address_button = By.ID, "com.yunmall.lc:id/address_add_new_btn"

    # 获取默认的姓名和电话信息的特征
    dafault_receipt_name_text_view = By.ID, "com.yunmall.lc:id/receipt_name"

    # 默认标记 特征
    is_default_feature = By.ID, "com.yunmall.lc:id/address_is_default"

    # 编辑 按钮
    edit_button = By.XPATH, "//*[@text='编辑']"

    # 删除 按钮
    delete_button = By.XPATH, "//*[@text='删除']"

    # 确定 按钮
    commit_button = By.XPATH, "//*[@text='确认']"

    @allure.step(title='地址列表 点击 添加地址')
    # 点击新增地址
    def click_add_address(self):
        self.base_find_element_with_scroll(self.add_address_button).click()

    @allure.step(title='地址列表 获取 收件人和电话的标题')
    # 获取 默认的姓名和电话的文字信息
    def get_default_receipt_name_text(self):
        return self.base_get_text(self.dafault_receipt_name_text_view)

    @allure.step(title='判断默认标记是否存在')
    # 判断  默认标志  是否存在
    def is_default_feature_exist(self):
        return self.base_is_feature_exist(self.is_default_feature)

    @allure.step(title='判断删除按钮是否存在')
    # 判断  删除按钮  是否存在
    def is_delete_exist(self):
        return self.base_is_feature_exist(self.delete_button)

    @allure.step(title='地址列表 点击 默认地址')
    # 点击 默认地址
    def click_default_address(self):
        self.base_click(self.is_default_feature)

    @allure.step(title='地址列表 点击 编辑')
    # 点击 编辑
    def click_edit(self):
        self.base_click(self.edit_button)

    @allure.step(title='地址列表 点击 删除')
    # 点击 删除
    def click_delete(self):
        self.base_click(self.delete_button)

    @allure.step(title='地址列表 点击 确定')
    # 点击 确定
    def click_commit(self):
        self.base_click(self.commit_button)