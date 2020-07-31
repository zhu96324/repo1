import time
import allure
import pytest

from base.base_data import base_data_text
from base.base_driver import init_drvier
from page.page import Page


@allure.epic("此项测试模块为针对‘百年奥莱项目’，‘VIP模块’功能的系统测试")
@allure.feature("VIP模块")
class TestVip:

    def setup(self):
        self.driver = init_drvier()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(2)
        self.driver.quit()

    @allure.title("VIP功能")
    @allure.story("与2020年05月14日，湖北武穴创建此项目，目前处于移动端测试学习阶段，加油！！！")
    @allure.description("针对 VIP功能 内部各项功能进行测试")
    @allure.severity("blocker")
    @pytest.mark.parametrize(("keyword", "expect"), base_data_text("vip_data", "test_vip"))
    def test_vip(self, keyword, expect):
        # 如果没登录 就去登录
        self.page.home.login_if_not(self.page)
        # 我 点击 加入vip
        self.page.me.click_be_vip()
        # 切换web环境
        self.driver.switch_to.context("WEBVIEW_com.yunmall.lc")
        # vip 输入 邀请码
        self.page.vip.input_invite(keyword)
        # vip 点击 加入会员
        self.page.vip.click_be_vip()
        # 断言， “邀请码输入不正确” 是否在 page_source中
        assert self.page.vip.base_is_keyword_in_page_source(expect), "%s不在page_source中" % expect
        # 切换 原生环境
        self.driver.switch_to.context("NATIVE_APP")



