# 导包
from time import sleep
from appium import webdriver

# 创建一个字典，包装相应的启动参数
from selenium.webdriver.common.by import By

desired_caps = dict()
# 需要连接的手机的平台（不限制大小写）
desired_caps['platformName'] = 'Android'
# 需要连接手机的系统版本号（5.2.1 的版本可以填写 5.2.1或5.2或5）
desired_caps['platformVersion'] = '5.1'
# 需要连接的手机设备号（android下可以随便写，但是不能不写 可用过 adb devices 在命令行查询）
desired_caps['deviceName'] = '192.168.172.102:5555'
# 需要启动的程序报名
desired_caps['appPackage'] = 'com.android.settings'
# 需要启动的程序的界面名
desired_caps['appActivity'] = '.Settings'
# 输入中文 需添加代码
desired_caps['unicodeKeyboard'] = True
desired_caps['reseKeyboard'] = True
#
# 连接appium服务器
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


def scroll_page_one_time(direction='up'):
    """
    滑动一次屏幕
    :param direction:方向
        "up": 从下往上
        "down": 从上往下
        "right"：从左往右
        "left"： 从右往左
    :return:
    """
    width = driver.get_window_size()["width"]
    height = driver.get_window_size()["height"]

    center_x = width / 2
    center_y = height / 2
    left_x = width / 4 * 1
    left_y = center_y
    right_x = width / 4 * 3
    right_y = center_y

    top_x = center_x
    top_y = height / 4 * 1
    bottom_x = center_x
    bottom_y = height / 4 * 3

    if direction == "up":
        driver.swipe(bottom_x, bottom_y, top_x, top_y, 3000)
    elif direction == "down":
        driver.swipe(top_x, top_y, bottom_x, bottom_y, 3000)
    elif direction == "left":
        driver.swipe(right_x, right_y, left_x, left_y, 3000)
    elif direction == "right":
        driver.swipe(left_x, left_y, right_x, right_y, 3000)
    else:
        raise Exception("请检查参数是否正确， up/down/left/right")


def find_element_with_scroll(feature, direction="up"):
    """
    边滑边找 某个元素的特征， 并且点击
    :param feature: 元素的特征
    :param direction: 方向
        "up": 从下往上
        "down": 从上往下
        "right"：从左往右
        "left"： 从右往左
    :return:
    """
    page_source = ""
    while True:
        try:
            return driver.find_element(*feature)
        except Exception:
            scroll_page_one_time(direction)
            if driver.page_source == page_source:
                print("到底了")
                break
            page_source = driver.page_source


find_element_with_scroll((By.XPATH, "//*[@text='关于手机']"))

driver.quit()