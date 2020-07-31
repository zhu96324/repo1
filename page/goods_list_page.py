import random

import allure
from selenium.webdriver.common.by import By

from base.base_login import BaseLogin


class GoodListPage(BaseLogin):

    # 商品列表 按钮
    goods_button = By.ID, "com.yunmall.lc:id/iv_element_1"

    @allure.step(title='商品列表 随机点击 商品')
    # 随机点击 商品列表
    def click_goods(self):
        goods = self.base_find_elements(self.goods_button)
        goods_count = len(goods)
        goods_index = random.randint(0, goods_count - 1)
        goods[goods_index].click()