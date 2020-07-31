import time
import allure
from base.base_driver import init_drvier
from page.page import Page


@allure.epic("此项测试模块为针对‘百年奥莱项目’，‘设置--清理缓存’功能的系统测试")
@allure.feature("设置-清理缓存模块")
class TestClearCache:

    def setup(self):
        self.driver = init_drvier()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(2)
        self.driver.quit()

    @allure.title("设置--清理缓存")
    @allure.story("与2020年05月14日，湖北武穴创建此项目，目前处于移动端测试学习阶段，加油！！！")
    @allure.description("针对 设置--清理缓存 内部各项功能进行测试")
    @allure.severity("blocker")
    def test_clear_cache(self):
        # 如果没有登录 先登录
        self.page.home.login_if_not(self.page)
        # 我 -- 点击 设置
        self.page.me.click_setting()
        # 设置 -- 点击清理缓存
        self.page.setting.click_clear_cache()
        # 断言 toast提示
        assert self.page.setting.base_is_toast_text("清理成功")
