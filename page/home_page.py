import allure
from selenium.webdriver.common.by import By
from base.base_login import BaseLogin


class HomePage(BaseLogin):

    # 我
    me_button = By.ID, "com.yunmall.lc:id/tab_me"

    # 分类
    category_button = By.ID, "com.yunmall.lc:id/tab_category"

    # 购物车
    shop_cart_button = By.ID, "com.yunmall.lc:id/tab_shopping_cart"

    # 放大镜
    search_button = By.ID, "com.yunmall.lc:id/ymtitlebar_left_btn_image"

    # 首页
    home_button = By.ID, "com.yunmall.lc:id/tab_home"

    # 点击 我
    @allure.step(title='主页 点击 我')
    def click_me(self):
        self.base_click(self.me_button)

    # 点击 分类
    @allure.step(title='主页 点击 分类')
    def click_category(self):
        self.base_click(self.category_button)

    # 点击购物车
    @allure.step(title='主页 点击 购物车')
    def click_shop_cart(self):
        self.base_click(self.shop_cart_button)

    # 点击 首页
    @allure.step(title='主页 点击 首页')
    def click_home(self):
        self.base_click(self.home_button)

    @allure.step(title='主页 登录（如果没有登录的话）')
    # 判断是否登录
    def login_if_not(self, page):
        # 判断登录状态
        self.click_me()
        if self.driver.current_activity != "com.yunmall.ymctoc.ui.activity.LogonActivity":
            return
        # 没有登录 就去登录
        # 点击已有账号 去登录
        page.register.click_login()
        # 输入用户名
        page.login.input_username("itheima_test")
        # 输入密码
        page.login.input_password("itheima")
        # 点击登录
        page.login.click_login()

    # 点击放大镜
    @allure.step(title='主页 点击 放大镜')
    def click_search(self):
        self.base_click(self.search_button)

