import unittest,time,os,platform
from time import sleep
import logging
from log import log
from Public.common import TestCaseInfo,DoExcel,CommonConfig as cc
from Public.pages import OkchemLoginPage
from config import globalconfig
from BeautifulReport import BeautifulReport
from run import *
from Public.common import send_mail as dd

url=DoExcel.File_Location().get_parameter("PRE地址")
buyer_un=DoExcel.File_Location().get_parameter("OKCHEM买家账号")
buyer_pw=DoExcel.File_Location().get_parameter("OKCHEM买家密码")
seller_un=DoExcel.File_Location().get_parameter("OKCHEM卖家账号")
seller_pw=DoExcel.File_Location().get_parameter("OKCHEM卖家密码")
buyer_nc=DoExcel.File_Location().get_parameter("OKCHEM买家昵称")
seller_nc=DoExcel.File_Location().get_parameter("OKCHEM卖家昵称")
fogotpw_bt=DoExcel.File_Location().get_parameter("忘记密码页面标题")
register_bt=DoExcel.File_Location().get_parameter("注册界面标题")
home_title=DoExcel.File_Location().get_parameter("首页title")
num=0

class TestOkchemLogin(unittest.TestCase):

    def setUp(self):
        self.url=url
        self.buyer_un=buyer_un
        self.buyer_pw=buyer_pw
        self.seller_un=seller_un
        self.seller_pw=seller_pw
        self.buyer_nc=buyer_nc
        self.seller_nc=seller_nc
        self.fogotpw_bt=fogotpw_bt
        self.register_bt=register_bt
        self.home_title=home_title
        self.testcaseInfo=TestCaseInfo.TestCaseInfo(id=1,name="OKCHEM买家登录",owner="Kang")
        self.BL=OkchemLoginPage.OkchemLoginPage()
        self.BL.open(self.url)

    def save_img(self, img_name):
        img_path=globalconfig.picture_path1
        self.BL.driver.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(img_path), img_name))

    @BeautifulReport.add_test_img("testOkchemLogin_001")
    def testOkchemLogin_001(self):
        """测试OKCHEM平台买家登录"""
        self.BL.OkchemLogin(self.buyer_un,self.buyer_pw)
        nicheng1=self.BL.findElement(self.BL.Nicheng_mem).text
        self.assertEqual(self.buyer_nc,nicheng1)
            # logger=log.Logger("FOX",CmdLevel=logging.INFO,FileLevel=logging.ERROR)
            # logger.info("this is a successful message!")
            # logger.debug("this is a successful message!")
        #     # self.testcaseInfo.result="successful! "
        # except Exception as err:
        #     self.testcaseInfo.erroinfo=str(err)
        #     logger=log.Logger("FOX",CmdLevel=logging.DEBUG,FileLevel=logging.ERROR)
        #     logger.info("this is a fail message!")
        #     logger.debug("this is a fail message!")
        #     self.testcaseInfo.result="fail！"

    @BeautifulReport.add_test_img("testOkchemLogin_002")
    def testOkchemLogin_002(self):
        """测试OKCHEM平台卖家登录"""
        self.BL.OkchemLogin(self.seller_un,self.seller_pw)
        nicheng1=self.BL.findElement(self.BL.Nicheng).text
        self.assertEqual(self.seller_nc,nicheng1)

    @BeautifulReport.add_test_img("testOkchemLogin_003")
    def testOkchemLogin_003(self):
        """测试OKCHEM平台忘记密码界面是否正常打开"""
        self.BL.ClickFogotPassword()
        fp_title=self.BL.findElement(OkchemLoginPage.OkchemLoginPage.Forgotpw_title).text
        self.assertEqual(self.fogotpw_bt,fp_title)

    @BeautifulReport.add_test_img("testOkchemLogin_004")
    def testOkchemLogin_004(self):
        """测试OKCHEM平台注册界面是否正常打开"""
        self.BL.ClickRegister()
        Register_title=self.BL.findElement(OkchemLoginPage.OkchemLoginPage.Register_title).text
        self.assertEqual(self.register_bt,Register_title)

    @BeautifulReport.add_test_img("testOkchemLogin_005")
    def testOkchemLogin_005(self):
        """测试OKCHEM平台登录界面返回Home页"""
        self.BL.ClickOkchemLogo()
        Home_title=self.BL.getTitle(OkchemLoginPage.OkchemLoginPage.Home_category)
        self.assertEqual(self.home_title,Home_title)

    def tearDown(self):
        global num
        num=num+1
        if num>=10:
            fangfa='testOkchemLogin_0'+str(num)
            xx=getattr(TestOkchemLogin(),fangfa)
            self.log =xx.__doc__
        elif num<10:
            fangfa='testOkchemLogin_00'+str(num)
            xx = getattr(TestOkchemLogin(), fangfa)
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
                screenname = screen_path + pattern + 'screenpicture' + now + '.png'
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
                screenname = screen_path + pattern + 'screenpicture' + now + '.png'
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
                self.BL.getPicture(screenname)  #进行截图处理
                sendEmail = dd.Email() #实例化类
                new_pic = sendEmail.newReport(screen_path) #获取最新的截图
                content1=result.errors[0][-1]
                content=content1.replace('File','<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;File').replace('During','<br/><br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;During')
                sendEmail.email_Text(new_pic,"注意！测试用例执行失败了！！！",self.log,content)  #发送邮件
                self.BL.driver.refresh()
        self.BL.quit()

    def list2reason(self, exc_list):
        if exc_list and exc_list[-1][0] is self:
            return exc_list[-1][1]



