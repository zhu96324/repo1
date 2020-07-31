import time
import allure
from base.base_driver import init_drvier
from page.page import Page


@allure.epic("此项测试模块为针对‘百年奥莱项目’，‘购物车模块’功能的系统测试")
@allure.feature("购物车模块")
class TestShopCart:

    def setup(self):
        self.driver = init_drvier()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(2)
        self.driver.quit()

    @allure.title("购物车功能")
    @allure.story("与2020年05月14日，湖北武穴创建此项目，目前处于移动端测试学习阶段，加油！！！")
    @allure.description("针对 购物车功能 内部各项功能进行测试")
    @allure.severity("blocker")
    def test_add_shop_cart(self):
        # 首页，如果没有登录就登录
        self.page.home.login_if_not(self.page)
        # 首页 -- 分类
        self.page.home.click_category()
        # 分类 -- 商品列表
        self.page.category.click_goods_list()
        # 商品列表 -- 商品详情
        self.page.goods_list.click_goods()
        # 记录一下 当前商品的标题
        goods_title = self.page.goods_detail.get_goods_title()
        # 商品详情 -- 加入购物车
        self.page.goods_detail.click_add_shop_cart()
        # 商品详情 -- 选择规格
        self.page.goods_detail.click_spec()
        # 商品详情 -- 购物车
        self.page.goods_detail.click_shop_cart()
        time.sleep(2)
        # 根据添加完成之后的页面，是否否有相同商品标题进行判断
        assert self.page.goods_detail.is_goods_title_exist(goods_title)

    @allure.title("购物车价格变化准确度")
    @allure.story("与2020年05月14日，湖北武穴创建此项目，目前处于移动端测试学习阶段，加油！！！")
    @allure.description("针对 购物车价格变化 内部各项功能进行测试")
    @allure.severity("blocker")
    def test_shop_cart_price(self):
        # 首页，如果没有登录就登录
        self.page.home.login_if_not(self.page)
        # 首页 - 点击购物车
        self.page.home.click_shop_cart()
        # 购物车 - 点击全选
        self.page.shop_cart.click_select_all()
        # 购物车 - 记录总价
        all_price = self.page.shop_cart.get_all_price()
        # 购物车 - 点击编辑
        self.page.shop_cart.click_edit()
        # 购物车 - 点击加号
        self.page.shop_cart.click_add()
        # 购物车 - 点击完成
        self.page.shop_cart.click_commit()
        # 断言 当前总价 = 记录总价 + 单价
        assert self.page.shop_cart.get_all_price() == all_price + self.page.shop_cart.get_price()

    @allure.title("购物车商品删除功能")
    @allure.story("与2020年05月14日，湖北武穴创建此项目，目前处于移动端测试学习阶段，加油！！！")
    @allure.description("针对 购物车商品删除 内部各项功能进行测试")
    @allure.severity("blocker")
    def test_del_shop_cart(self):
        # 首页，如果没有登录就登录
        self.page.home.login_if_not(self.page)
        # 首页 - 点击购物车
        self.page.home.click_shop_cart()
        # 购物车 - 判断是否有商品，如果没有则添加
        if self.page.shop_cart.is_shop_cart_empty():
            # 首页 -- 分类
            self.page.home.click_category()
            # 分类 -- 商品列表
            self.page.category.click_goods_list()
            # 商品列表 -- 商品详情
            self.page.goods_list.click_goods()
            # 记录一下 当前商品的标题
            goods_title = self.page.goods_detail.get_goods_title()
            # 商品详情 -- 加入购物车
            self.page.goods_detail.click_add_shop_cart()
            # 商品详情 -- 选择规格
            self.page.goods_detail.click_spec()
            # 两次返回
            self.page.goods_detail.press_back()
            time.sleep(2)
            self.page.goods_detail.press_back()
            # 首页 - 点击购物车
            self.page.home.click_shop_cart()
        # 购物车 - 点击全选
        self.page.shop_cart.click_select_all()
        # 购物车 - 点击编辑
        self.page.shop_cart.click_edit()
        # 购物车 - 点击删除
        self.page.shop_cart.click_delete()
        # 购物车 - 点击确认
        self.page.shop_cart.click_yes()

        # 断言， toast 是不是叫做 删除成功
        assert self.page.shop_cart.base_is_toast_text('删除成功')
        # 断言 当前页面是不是有一个叫做 “购物车还是空的”
        assert self.page.shop_cart.is_shop_cart_empty()