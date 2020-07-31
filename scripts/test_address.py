import time
from time import sleep
import allure
import pytest
from base.base_data import base_data_text
from base.base_driver import init_drvier
from page.page import Page


@allure.epic("此项测试模块为针对‘百年奥莱项目’，‘地址管理’ ‘地址修改’ ‘地址删除’功能的系统测试")
@allure.feature("地址管理-测试模块")
class TestAddress:

    def setup(self):
        self.driver = init_drvier()
        self.page = Page(self.driver)

    def tesrdown(self):
        time.sleep(2)
        self.driver.quit()

    @allure.title("地址管理--新建地址")
    @allure.story("与2020年05月14日，湖北武穴创建此项目，目前处于移动端测试学习阶段，加油！！！")
    @allure.description("针对 地址管理--新建地址 内部各项功能进行测试")
    @allure.severity("blocker")
    @pytest.mark.parametrize(("name", "phone", "info", "post_code", "toast"), base_data_text("address_data", "test_add_address"))
    def test_add_address(self, name, phone, info, post_code, toast):
        # 首页 没有登录就登录
        self.page.home.login_if_not(self.page)
        # 我 点击 设置
        self.page.me.click_setting()
        # 设置 点击 地址管理
        self.page.setting.click_address_list()
        # 地址管理 点击 新增地址
        self.page.address_list.click_add_address()
        # 新增地址 输入收件人
        self.page.edit_address.input_name(name)
        # 新增地址 输入电话
        self.page.edit_address.input_phone(phone)
        # 新增地址 输入详细地址
        self.page.edit_address.input_info(info)
        # 新增地址 输入邮编
        self.page.edit_address.input_post_code(post_code)
        # 新增地址 勾选 设为默认地址
        self.page.edit_address.click_default_address()
        # 新增地址 选择 随机区域
        self.page.edit_address.choose_region()
        # 点击保存按钮
        self.page.edit_address.click_save_button()
        # 断言 根据预期toast的值进行 判断
        if toast is None:
            assert self.page.address_list.get_default_receipt_name_text() == "%s  %s" % (name, phone), '保存成功， 默认的姓名和电话与输入的不符'
        else:
            assert self.page.edit_address.base_is_toast_text(toast),'保存不成功， toast内容与预期不符'

    @allure.title("地址管理--修改地址")
    @allure.story("与2020年05月14日，湖北武穴创建此项目，目前处于移动端测试学习阶段，加油！！！")
    @allure.description("针对 地址管理--修改地址 内部各项功能进行测试")
    @allure.severity("blocker")
    def test_edit_address(self):
        # 首页 没有登录就登录
        self.page.home.login_if_not(self.page)
        # 我 点击 设置
        self.page.me.click_setting()
        # 设置 点击 地址管理
        self.page.setting.click_address_list()

        if not self.page.address_list.is_default_feature_exist():
            # 地址管理 点击 新增地址
            self.page.address_list.click_add_address()
            # 新增地址 输入收件人
            self.page.edit_address.input_name("zhangsan")
            # 新增地址 输入电话
            self.page.edit_address.input_phone("18888888888")
            # 新增地址 输入详细地址
            self.page.edit_address.input_info("三单元 504")
            # 新增地址 输入邮编
            self.page.edit_address.input_post_code("100000")
            # 新增地址 勾选 设为默认地址
            self.page.edit_address.click_default_address()
            # 新增地址 选择 随机区域
            self.page.edit_address.choose_region()
            # 点击保存按钮
            self.page.edit_address.click_save_button()

        # 进入 默认地址 (进入了 edit_address界面)
        self.page.address_list.click_default_address()
        # 重新输入 收件人
        self.page.edit_address.input_name("李四")
        # 重新输入 电话
        self.page.edit_address.input_phone("16666666666")
        # 重新输入 详细地址
        self.page.edit_address.input_info("302 二单元")
        # 重新输入 邮编
        self.page.edit_address.input_post_code("222222")
        # 重新输入 所在地区
        self.page.edit_address.choose_region()
        # 保存信息
        self.page.edit_address.click_save_button()

        # 断言， 是否出现 “保存成功” 的toast信息
        assert self.page.address_list.base_is_toast_text("保存成功")

    @allure.title("地址管理--删除地址")
    @allure.story("与2020年05月14日，湖北武穴创建此项目，目前处于移动端测试学习阶段，加油！！！")
    @allure.description("针对 地址管理--删除地址 内部各项功能进行测试")
    @allure.severity("blocker")
    def test_delete_address(self):
        # 首页 没有登录就登录
        self.page.home.login_if_not(self.page)
        # 我 点击 设置
        self.page.me.click_setting()
        # 设置 点击 地址管理
        self.page.setting.click_address_list()

        # 断言 判断是否有地址可删除
        assert self.page.address_list.is_default_feature_exist(), "默认标记不存在，没有地址可删除"

        for i in range(10):
            self.page.address_list.click_edit()
            # 判断删除是否存在
            if not self.page.address_list.is_delete_exist():
                # 如果不存在， break
                break
            # 如果存在 则点击
            self.page.address_list.click_delete()
            self.page.address_list.click_commit()
            sleep(1)

        # 点击编辑
        self.page.address_list.click_edit()
        # 断言 删除按钮是否存在， 如果不存在则通过，如果存在则不通过
        assert not self.page.address_list.is_delete_exist(), "收货地址没有删除完毕"
