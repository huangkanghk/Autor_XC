import unittest,time,os,platform
from Public.common import TestCaseInfo,DoExcel,CommonConfig as cc
from Public.pages import ChinaHomePage
from time import sleep
from config import globalconfig
from BeautifulReport import BeautifulReport
from Public.common import send_mail as dd

url=DoExcel.File_Location().get_parameter("中国站地址",User_Table ="Login")
chinahome_title=DoExcel.File_Location().get_parameter("首页title",User_Table ="China")
platformservice_ele=DoExcel.File_Location().get_parameter("平台服务",User_Table ="China")
customercase_ele=DoExcel.File_Location().get_parameter("客户案例",User_Table ="China")
memberbenefits_ele=DoExcel.File_Location().get_parameter("会员权益",User_Table ="China")
exbition_ele=DoExcel.File_Location().get_parameter("展会资讯",User_Table ="China")
news_ele=DoExcel.File_Location().get_parameter("行业新闻",User_Table ="China")
aboutus_title=DoExcel.File_Location().get_parameter("关于我们",User_Table ="China")
username=DoExcel.File_Location().get_parameter("卖家账号",User_Table ="China")
password=DoExcel.File_Location().get_parameter("卖家密码",User_Table ="China")
nicheng=DoExcel.File_Location().get_parameter("卖家昵称",User_Table ="China")
num=0

class ChinaHome(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.url=url
        self.chinahome_title=chinahome_title
        self.platformservice_ele=platformservice_ele
        self.customercase_ele=customercase_ele
        self.memberbenefits_ele=memberbenefits_ele
        self.exbition_ele=exbition_ele
        self.news_ele=news_ele
        self.aboutus_title=aboutus_title
        self.username=username
        self.password=password
        self.nicheng=nicheng
        self.BL=ChinaHomePage.ChinaHomePage()
        self.BL.open(self.url)
        self.BL.driver.delete_all_cookies()

    def save_img(self, img_name):
        img_path=globalconfig.picture_path1
        self.BL.driver.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(img_path), img_name))

    @BeautifulReport.add_test_img("testChinaHome_001")
    def testChinaHome_001(self):
        """测试中国站首页"""
        ele=self.BL.findElement(ChinaHomePage.ChinaHomePage.home)
        self.BL.click(ele)
        actual=self.BL.getTitle(ChinaHomePage.ChinaHomePage.home_ele)
        self.assertEqual(self.chinahome_title,actual)

    @BeautifulReport.add_test_img("testChinaHome_002")
    def testChinaHome_002(self):
        """测试中国站平台服务页"""
        ele=self.BL.findElement(ChinaHomePage.ChinaHomePage.platformservice)
        self.BL.click(ele)
        actual=self.BL.getText(ChinaHomePage.ChinaHomePage.platformservice_exp)
        self.assertIn(self.platformservice_ele,actual)

    @BeautifulReport.add_test_img("testChinaHome_003")
    def testChinaHome_003(self):
        """测试中国站客户案例页"""
        ele=self.BL.findElement(ChinaHomePage.ChinaHomePage.customercase)
        self.BL.click(ele)
        actual=self.BL.getText(ChinaHomePage.ChinaHomePage.customercase_exp)
        self.assertIn(self.customercase_ele,actual)

    @BeautifulReport.add_test_img("testChinaHome_004")
    def testChinaHome_004(self):
        """测试中国站会员权益页"""
        ele=self.BL.findElement(ChinaHomePage.ChinaHomePage.memberbenefits)
        self.BL.click(ele)
        actual=self.BL.getText(ChinaHomePage.ChinaHomePage.memberbenefits_exp)
        self.assertEqual(self.memberbenefits_ele,actual)

    @BeautifulReport.add_test_img("testChinaHome_005")
    def testChinaHome_005(self):
        """测试中国站展会资讯页"""
        ele = self.BL.findElement(ChinaHomePage.ChinaHomePage.exhibition)
        self.BL.click(ele)
        actual = self.BL.getText(ChinaHomePage.ChinaHomePage.exhibition_exp)
        self.assertEqual(self.exbition_ele, actual)

    @BeautifulReport.add_test_img("testChinaHome_006")
    def testChinaHome_006(self):
        """测试中国站行业新闻页"""
        ele = self.BL.findElement(ChinaHomePage.ChinaHomePage.news)
        self.BL.click(ele)
        actual = self.BL.getText(ChinaHomePage.ChinaHomePage.news_exp)
        self.assertEqual(self.news_ele, actual)

    @BeautifulReport.add_test_img("testChinaHome_007")
    def testChinaHome_007(self):
        """测试中国站关于我们"""
        ele = self.BL.findElement(ChinaHomePage.ChinaHomePage.aboutus)
        allhandes = self.BL.driver.window_handles
        self.BL.click(ele)
        self.BL.waitWindow(allhandes)
        self.BL.switchHandle(1)
        actual = self.BL.getTitle(ChinaHomePage.ChinaHomePage.aboutus_ele)
        self.assertEqual(self.aboutus_title, actual)

    def tearDown(self):
        global num
        num=num+1
        if num>=10:
            fangfa='testChinaHome_0'+str(num)
            xx=getattr(ChinaHome(),fangfa)
            self.log =xx.__doc__
        elif num<10:
            fangfa='testChinaHome_00'+str(num)
            xx = getattr(ChinaHome(), fangfa)
            self.log= xx.__doc__
        result = self.defaultTestResult()
        self._feedErrorsToResult(result, self._outcome.errors)
        error = self.list2reason(result.errors)
        failure = self.list2reason(result.failures)
        ok = not error and not failure
        html=self.BL.driver.title
        if not ok:
            pattern = '/' if platform != 'Windows' else '\\'
            if '500 Internal Server Error' in html:
                now = time.strftime("%Y-%m-%d %H_%M_%S")  # 获取当前时间
                screen_path=globalconfig.picture_path  # 图片路径地址
                screenname = screen_path +pattern + 'screenpicture' + now + '.png'
                print(screenname)
                self.BL.getPicture(screenname)  #进行截图处理
                sendEmail = dd.Email() #实例化类
                new_pic = sendEmail.newReport(screen_path) #获取最新的截图
                content1=result.errors[0][-1]
                content=content1.replace('File','<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;File').replace('During','<br/><br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;During')
                sendEmail.email_Text_All(new_pic,"致命！系统报500错误了！！！",self.log,content)  #发送邮件
                self.BL.driver.refresh()
            elif 'Site Maintenance' in html:
                now = time.strftime("%Y-%m-%d %H_%M_%S")  # 获取当前时间
                screen_path=globalconfig.picture_path  # 图片路径地址
                screenname = screen_path +pattern + 'screenpicture' + now + '.png'
                print(screenname)
                self.BL.getPicture(screenname)  #进行截图处理
                sendEmail = dd.Email() #实例化类
                new_pic = sendEmail.newReport(screen_path) #获取最新的截图
                content1=result.errors[0][-1]
                content=content1.replace('File','<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;File').replace('During','<br/><br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;During')
                sendEmail.email_Text(new_pic,"警告！页面显示正在维护中！！！",self.log,content)  #发送邮件
                self.BL.driver.refresh()
            else:
                now = time.strftime("%Y-%m-%d %H_%M_%S")  # 获取当前时间
                screen_path=globalconfig.picture_path  # 图片路径地址
                screenname = screen_path + pattern + 'screenpicture' + now + '.png'
                print(screenname)
                self.BL.getPicture(screenname)  #进行截图处理
                sendEmail = dd.Email() #实例化类
                new_pic = sendEmail.newReport(screen_path) #获取最新的截图
                content1=result.errors[0][-1]
                content=content1.replace('File','<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;File').replace('During','<br/><br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;During')
                sendEmail.email_Text(new_pic,"注意！测试用例执行失败了！！！",self.log,content)  #发送邮件
                self.BL.driver.refresh()
        list=self.BL.getAllHandles()
        if len(list)>1:
            self.BL.driver.close()
            self.BL.switchHandle(0)
        else:
            self.BL.driver.back()

    def list2reason(self, exc_list):
        if exc_list and exc_list[-1][0] is self:
            return exc_list[-1][1]

    @classmethod
    def tearDownClass(self):
        self.BL.driver.quit()
