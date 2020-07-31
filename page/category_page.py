import random

import allure
from selenium.webdriver.common.by import By

from base.base_login import BaseLogin


class CategoryPage(BaseLogin):

    # 商品分类列表 按钮
    goods_list_button = By.ID, "com.yunmall.lc:id/iv_img"

    @allure.step(title='分类 点击 商品列表')
    # 随机点击 商品分类列表
    def click_goods_list(self):
        goods_lists = self.base_find_elements(self.goods_list_button)
        goods_lists_count = len(goods_lists)
        goods_lists_index = random.randint(0, goods_lists_count-1)
        goods_lists[goods_lists_index].click()