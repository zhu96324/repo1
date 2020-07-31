import time
import allure
from base.base_driver import init_drvier
from page.page import Page


@allure.epic("此项测试模块为针对‘百年奥莱项目’，‘版本更新更新’功能的系统测试")
@allure.feature("版本更新模块")
class TestUpdate():

    def setup(self):
        self.driver = init_drvier()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(2)
        self.driver.quit()

    @allure.title("版本更新功能")
    @allure.story("与2020年05月14日，湖北武穴创建此项目，目前处于移动端测试学习阶段，加油！！！")
    @allure.description("针对 版本更新 内部各项功能进行测试")
    @allure.severity("blocker")
    def test_update(self):
        # 如果没有登录 先登录
        self.page.home.login_if_not(self.page)
        # 我 -- 点击 设置
        self.page.me.click_setting()
        # 设置 -- 点击关于
        self.page.setting.click_about()
        # 关于 -- 点击 版本更新
        self.page.about.click_update()
        # 断言 toast提示
        assert self.page.about.base_is_toast_text("当前已是最新版本")

