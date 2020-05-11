from appium import webdriver


def init_drvier():
    # 创建一个字典，包装相应的启动参数
    desired_caps = dict()
    # 需要连接的手机的平台（不限制大小写）
    desired_caps['platformName'] = 'Android'
    # 需要连接手机的系统版本号（5.2.1 的版本可以填写 5.2.1或5.2或5）
    desired_caps['platformVersion'] = '5.1'
    # 需要连接的手机设备号（android下可以随便写，但是不能不写 可用过 adb devices 在命令行查询）
    desired_caps['deviceName'] = '192.168.172.102:5555'
    # 需要启动的程序报名
    desired_caps['appPackage'] = 'com.yunmall.lc'
    # 需要启动的程序的界面名
    desired_caps['appActivity'] = 'com.yunmall.ymctoc.ui.activity.MainActivity'
    # 输入中文 需添加代码
    desired_caps['unicodeKeyboard'] = True
    desired_caps['reseKeyboard'] = True
    # 连接appium服务器
    return webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)