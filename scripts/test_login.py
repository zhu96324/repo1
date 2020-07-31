import allure
import pytest
from time import sleep
from base.base_data import base_data_text
from base.base_driver import init_drvier
from page.page import Page


@allure.epic("此项测试模块为针对‘百年奥莱项目’，‘home--登录模块’功能的系统测试")
@allure.feature("home-登录模块")
class TestLogin:

    def setup(self):
        self.driver = init_drvier(no_reset=False)
        self.page = Page(self.driver)

    def teardown(self):
        sleep(3)
        self.driver.quit()

    @allure.title("home--登录功能")
    @allure.story("与2020年05月14日，湖北武穴创建此项目，目前处于移动端测试学习阶段，加油！！！")
    @allure.description("针对 home--登录功能 内部各项功能进行测试")
    @allure.severity("blocker")
    @pytest.mark.parametrize(("username", "password", "toast"), base_data_text("login_data", "test_login") )
    def test_login(self, username, password, toast):
        self.page.home.click_me()
        self.page.register.click_login()
        self.page.login.input_username(username)
        self.page.login.input_password(password)
        self.page.login.click_login()

        if toast is None:
            assert self.page.me.get_nick_name_text() == username
        else:
            # 找toast提示，找到参数内的toast提示是否能找到，如果能则通过，如果不能则不通过
            assert self.page.login.base_is_toast_text(toast)

