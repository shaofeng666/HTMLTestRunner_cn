"""HTMLTestRunner 截图版示例 selenium 版"""
from framework.base_page import BasePage
from selenium import webdriver
import unittest
import time
from HTMLTestRunner_cn import HTMLTestRunner
import sys


class case_01(unittest.TestCase):
    """
    def setUp(cls):
        cls.driver = webdriver.Chrome()

    def tearDown(cls):
        cls.driver.quit()

        """

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def add_img(self):
        self.imgs.append(self.driver.get_screenshot_as_base64())
        return True

    def setUp(self):
        # 在是python3.x 中，如果在这里初始化driver ，因为3.x版本 unittest 运行机制不同，会导致用力失败时截图失败
        self.imgs = []
        self.addCleanup(self.cleanup)

    def cleanup(self):
        pass

    def test_case1(self):
        print("登陆~~~")
        self.driver.get("http://117.169.87.75:8009/")
        self.driver.find_element_by_name("Phone").send_keys("15607241351")
        self.driver.find_element_by_name("PassWord").send_keys("88888888")
        self.driver.find_element_by_name("ValidateCode").send_keys("269c545f-8934-4011-a888-ef41c94b40ac")
        self.driver.find_element_by_id("btn_login").click();
        time.sleep(3)
        self.add_img()
        result = self.driver.find_element_by_xpath('//*[@id="page-wrapper"]/div[1]/a').text
        print("______________________",result)

        self.add_img()


    def test_case2(self):
        print("退出~~~")
        self.driver.find_element_by_xpath('//*[@id="page-wrapper"]/div[1]/a').click()
        self.add_img()



# 添加Suite
def Suite():
    # 定义一个单元测试容器
    suiteTest = unittest.TestSuite()
    # 将测试用例加入到容器
    suiteTest.addTest(case_01("test_case1"))
    suiteTest.addTest(case_01("test_case2"))


    return suiteTest


if __name__ == "__main__":
    # suite = unittest.TestLoader().loadTestsFromTestCase(case_01)
    runer = HTMLTestRunner(
        title="带截图的测试报告",
        description="用例测试情况",
        tester='Shaofeng Wu',
        stream=BasePage.get_report_path(),
        verbosity=2, retry=1, save_last_try=True)
    runer.run(Suite())
