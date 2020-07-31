import allure
from selenium.webdriver.common.by import By

from base.base_login import BaseLogin


class GoodsDetailPage(BaseLogin):

    # 加入 购物车 按钮
    add_shop_cart_button = By.ID, "com.yunmall.lc:id/btn_add_to_shopping_cart"

    # 确认 按钮
    commit_button = By.XPATH, "//*[@text='确认']"

    # 商品标题 特征
    goods_title_text_view = By.ID, "com.yunmall.lc:id/tv_product_title"

    # 购物车 按钮
    shop_cart_button = By.ID, "com.yunmall.lc:id/btn_shopping_cart"

    @allure.step(title='商品详情 点击 添加购物车')
    # 点击 加入购物车
    def click_add_shop_cart(self):
        self.base_click(self.add_shop_cart_button)

    @allure.step(title='商品详情 点击 确认')
    # 点击 确认
    def click_commit(self):
        self.base_click(self.commit_button)

    @allure.step(title='商品详情 获取第一个规格的名字')
    # 根据 “请选择 分类 规格” 获取 请选择后面的第一个规格的名字
    def get_choose_spec(self, text):
        return text.split(" ")[1]

    @allure.step(title='商品详情 选择规格')
    # 选择 规格
    def click_spec(self):
        while True:
            self.click_commit()
            if self.base_is_toast_text("请选择"):
                spec_name = self.get_choose_spec(self.base_get_toast_text("请选择"))
                spec_feature = By.XPATH, "//*[@text='%s']/../*[2]/*[1]" % spec_name
                self.base_click(spec_feature)
            else:
                break

    @allure.step(title='商品详情 获取商品标题')
    # 获取商品的标题
    def get_goods_title(self):
        return self.base_get_text(self.goods_title_text_view)

    @allure.step(title='商品详情 点击 购物车')
    # 点击 购物车
    def click_shop_cart(self):
        self.base_click(self.shop_cart_button)

    @allure.step(title='商品详情 判断 商品标题是否存在')
    # 根据商品的标题， 判断是否存在这个页面上
    def is_goods_title_exist(self, title):
        title_xpath = By.XPATH, "//*[@text='%s']" % title
        return self.base_is_feature_exist(title_xpath)