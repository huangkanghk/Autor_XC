from selenium import webdriver
import unittest
import time
from time import sleep

class TestBadidu(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://www.baidu.com")

    def test_Baidu(self):
        """测试百度搜索一下"""
        self.driver.find_element_by_id("kw").click()
        self.driver.find_element_by_id("kw").send_keys("okchem")
        self.driver.find_element_by_id("su").click()
        sleep(2)
        self.assertEqual(self.driver.title,"test")

    def tearDown(self):
        result = self.defaultTestResult()
        self._feedErrorsToResult(result, self._outcome.errors)
        error = self.list2reason(result.errors)
        failure = self.list2reason(result.failures)
        ok = not error and not failure
        if not ok:
            now = time.strftime("%Y-%m-%d %H%M%S")  # 获取当前时间
            screen_path = "C:\\Python37\\AutoRunFrame\\Public\\Screenshot"  # 图片路径地址
            screenname = screen_path + '\\' + 'screenpicture' + now + '.png'
            print(screenname)
            self.driver.get_screenshot_as_file(screenname)
        self.driver.quit()

    def list2reason(self, exc_list):
        if exc_list and exc_list[-1][0] is self:
            return exc_list[-1][1]

if __name__=="__main__":
    unittest.main()