import allure
from selenium.webdriver.common.by import By
from base.base_login import BaseLogin


class ShopCartPage(BaseLogin):

    # 全选 按钮
    select_all_button = By.ID, "com.yunmall.lc:id/iv_select_all"

    # 编辑 按钮
    edit_button = By.XPATH, "//*[@text='编辑']"

    # 完成 按钮
    commit_button = By.XPATH, "//*[@text='完成']"

    # 加号 按钮
    add_button = By.ID, "com.yunmall.lc:id/iv_add"

    # 单价 特征
    price_feature = By.ID, "com.yunmall.lc:id/tv_price"

    # 总价 特征
    all_price_feature = By.ID, "com.yunmall.lc:id/tv_count_money"

    # 删除 按钮
    delete_button = By.XPATH, "//*[@text='删除']"

    # 确认 按钮
    yes_button = By.XPATH, "//*[@text='确认']"

    @allure.step(title='购物车 点击 全选')
    # 点击 全选
    def click_select_all(self):
        self.base_click(self.select_all_button)

    @allure.step(title='购物车 点击 编辑')
    # 点击 编辑
    def click_edit(self):
        self.base_click(self.edit_button)

    @allure.step(title='购物车 点击 完成')
    # 点击 完成
    def click_commit(self):
        self.base_click(self.commit_button)

    @allure.step(title='购物车 点击 加号')
    # 点击 加号
    def click_add(self):
        self.base_click(self.add_button)

    @allure.step(title='购物车 价格格式转换')
    # 价格格式转化为float类型
    def deal_with_price(self, price):
        allure.attach(price, "价格原形", allure.attachment_type.TEXT)
        return float(price[2:])

    @allure.step(title='购物车 获取转换过后的产品单价')
    # 获取转换过后的产品单价
    def get_price(self):
        # 获取单价的文字
        price_text = self.base_get_text(self.price_feature)
        # 通过 deal_with_price 去掉前面的人民币符号， 并且转化为float类型
        return self.deal_with_price(price_text)

    @allure.step(title='购物车 获取转换过后的产品总价')
    # 获取转换过后的产品总价
    def get_all_price(self):
        # 获取单价的文字
        all_price_text = self.base_get_text(self.all_price_feature)
        # 通过 deal_with_price 去掉前面的人民币符号， 并且转化为float类型
        return self.deal_with_price(all_price_text)

    @allure.step(title='购物车 点击 删除')
    # 点击 删除
    def click_delete(self):
        self.base_click(self.delete_button)

    @allure.step(title='购物车 点击 确认')
    # 点击 确认
    def click_yes(self):
        self.base_click(self.yes_button)

    @allure.step(title='判断购物车是不是为空')
    # 判断 购物车是否为空
    def is_shop_cart_empty(self):
        xpath = By.XPATH, "//*[contains(@text,'购物车还是空的')]"
        return self.base_is_feature_exist(xpath)


