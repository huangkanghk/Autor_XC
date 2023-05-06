import unittest,time,os,sys
from Public.common import DoExcel
from Public.pages import ChembnbLoginPage,ChembnbBuyerCenterPage
from time import sleep
from config import globalconfig
from BeautifulReport import BeautifulReport
from Public.common import send_mail as dd
from selenium.webdriver.common.action_chains import ActionChains
import platform

url=DoExcel.File_Location().get_parameter("Chembnb地址",User_Table ="ChembnbLogin")
usrname=DoExcel.File_Location().get_parameter("买家账号",User_Table ="ChembnbBuyerCenter")
password=DoExcel.File_Location().get_parameter("买家密码",User_Table ="ChembnbBuyerCenter")
MyIndependentApp=DoExcel.File_Location().get_parameter("My Independent Applications",User_Table ="ChembnbBuyerCenter")
MyGroupApplications=DoExcel.File_Location().get_parameter("My Group Applications",User_Table ="ChembnbBuyerCenter")
MyWishlist=DoExcel.File_Location().get_parameter("我的愿望清单",User_Table ="ChembnbBuyerCenter")
MyPoints=DoExcel.File_Location().get_parameter("我的积分",User_Table ="ChembnbBuyerCenter")
EditProfile=DoExcel.File_Location().get_parameter("修改资料",User_Table ="ChembnbBuyerCenter")
ChangePassword=DoExcel.File_Location().get_parameter("修改密码",User_Table ="ChembnbBuyerCenter")
ChembnbHomeTitle=DoExcel.File_Location().get_parameter("集采首页title",User_Table ="ChembnbBuyerCenter")
num = 0

class ChembnbBuyerCenter(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.url=url
        self.usrname=usrname
        self.password=password
        self.MyIndependentApp=MyIndependentApp
        self.MyGroupApplications=MyGroupApplications
        self.MyWishlist=MyWishlist
        self.MyPoints=MyPoints
        self.EditProfile=EditProfile
        self.ChangePassword=ChangePassword
        self.ChembnbHomeTitle=ChembnbHomeTitle
        self.BL = ChembnbLoginPage.ChembnbLoginPage()
        self.BL.ChembnbBuyerLogin(self.usrname,self.password)

    def save_img(self, img_name):
        img_path=globalconfig.picture_path1
        self.BL.driver.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(img_path), img_name))

    @BeautifulReport.add_test_img("testChembnbBuyerCenter_001")
    def testChembnbBuyerCenter_001(self):
        """测试Chembnb平台在买家中心点击My Independent Applications"""
        ele = self.BL.findElement(ChembnbBuyerCenterPage.ChembnbBuyerCenterPage.BuyerCenter)
        self.BL.click(ele)
        self.BL.waitText(ChembnbBuyerCenterPage.ChembnbBuyerCenterPage.MyIndependentApplication)
        ele1=self.BL.findElement(ChembnbBuyerCenterPage.ChembnbBuyerCenterPage.MyIndependentApplication)
        self.BL.click(ele1)
        actual=self.BL.getText(ChembnbBuyerCenterPage.ChembnbBuyerCenterPage.MyIndependentApplication_exp)
        self.assertIn(self.MyIndependentApp,actual)

    @BeautifulReport.add_test_img("testChembnbBuyerCenter_002")
    def testChembnbBuyerCenter_002(self):
        """测试Chembnb平台在买家中心点击My Group Applications"""
        ele1=self.BL.findElement(ChembnbBuyerCenterPage.ChembnbBuyerCenterPage.MyGroupApplications)
        self.BL.click(ele1)
        actual=self.BL.getText(ChembnbBuyerCenterPage.ChembnbBuyerCenterPage.MyGroupApplications_exp)
        self.assertIn(self.MyGroupApplications,actual)

    @BeautifulReport.add_test_img("testChembnbBuyerCenter_003")
    def testChembnbBuyerCenter_003(self):
        """测试Chembnb平台在买家中心点击My Wish List"""
        ele1=self.BL.findElement(ChembnbBuyerCenterPage.ChembnbBuyerCenterPage.MyWishList)
        self.BL.click(ele1)
        actual=self.BL.getText(ChembnbBuyerCenterPage.ChembnbBuyerCenterPage.MyWishList_exp)
        self.assertIn(self.MyWishlist,actual)

    @BeautifulReport.add_test_img("testChembnbBuyerCenter_004")
    def testChembnbBuyerCenter_004(self):
        """测试Chembnb平台在买家中心点击My Points"""
        ele1=self.BL.findElement(ChembnbBuyerCenterPage.ChembnbBuyerCenterPage.MyPoints)
        self.BL.click(ele1)
        actual=self.BL.getText(ChembnbBuyerCenterPage.ChembnbBuyerCenterPage.MyPoints_exp)
        self.assertIn(self.MyWishlist,actual)

    @BeautifulReport.add_test_img("testChembnbBuyerCenter_005")
    def testChembnbBuyerCenter_005(self):
        """测试Chembnb平台在买家中心点击Edit Profile"""
        ele1=self.BL.findElement(ChembnbBuyerCenterPage.ChembnbBuyerCenterPage.EditProfile)
        self.BL.click(ele1)
        actual=self.BL.getText(ChembnbBuyerCenterPage.ChembnbBuyerCenterPage.EditProfile_exp)
        self.assertIn(self.EditProfile,actual)

    @BeautifulReport.add_test_img("testChembnbBuyerCenter_006")
    def testChembnbBuyerCenter_006(self):
        """测试Chembnb平台在买家中心点击ChangePassword"""
        ele1=self.BL.findElement(ChembnbBuyerCenterPage.ChembnbBuyerCenterPage.ChangePassword)
        self.BL.click(ele1)
        actual=self.BL.getText(ChembnbBuyerCenterPage.ChembnbBuyerCenterPage.ChangePassword_exp)
        self.assertIn(self.ChangePassword,actual)

    @BeautifulReport.add_test_img("testChembnbBuyerCenter_007")
    def testChembnbBuyerCenter_007(self):
        """测试Chembnb平台在买家中心点击Log Out"""
        ele1=self.BL.findElement(ChembnbBuyerCenterPage.ChembnbBuyerCenterPage.ChangePassword)
        self.BL.click(ele1)
        sleep(5)
        actual=self.BL.driver.title
        self.assertIn(self.ChembnbHomeTitle,actual)

    def tearDown(self):
        global num
        num=num+1
        print(num)
        if num>=10:
            fangfa='testChembnbBuyerCenter_0'+str(num)
            xx=getattr(ChembnbBuyerCenter(),fangfa)
            self.log =xx.__doc__
        elif num<10:
            fangfa='testChembnbBuyerCenter_00'+str(num)
            xx = getattr(ChembnbBuyerCenter(), fangfa)
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
                screenname = screen_path + pattern + 'screenpicture' + now + '.png'
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
                screenname = screen_path +pattern + 'screenpicture' + now + '.png'
                print(screenname)
                self.BL.getPicture(screenname)  #进行截图处理
                sendEmail = dd.Email() #实例化类
                new_pic = sendEmail.newReport(screen_path) #获取最新的截图
                content1=result.errors[0][-1]
                content=content1.replace('File','<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;File').replace('During','<br/><br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;During')
                sendEmail.email_Text(new_pic,"注意！测试用例执行失败了！！！",self.log,content)  #发送邮件
                self.BL.driver.refresh()

    def list2reason(self, exc_list):
        if exc_list and exc_list[-1][0] is self:
            return exc_list[-1][1]

    @classmethod
    def tearDownClass(self):
        self.BL.driver.quit()