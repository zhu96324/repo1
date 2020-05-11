from time import sleep

from base.base_driver import init_drvier


class TestLogin:
    def setup(self):
        self.driver = init_drvier()

    def teardown(self):
        sleep(3)
        self.driver.quit()

    def test_login(self):
        pass