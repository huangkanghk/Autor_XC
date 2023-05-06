import unittest,time,os,platform
from Public.common import TestCaseInfo,DoExcel,CommonConfig as cc
from Public.pages import ChembnbLoginPage
from time import sleep
from config import globalconfig
from BeautifulReport import BeautifulReport
from Public.common import send_mail as dd

url=DoExcel.File_Location().get_parameter("Chembnb地址",User_Table ="ChembnbLogin")
buyerLoginSuccess=DoExcel.File_Location().get_parameter("买家登录成功页面",User_Table ="ChembnbLogin")
buyerMail=DoExcel.File_Location().get_parameter("买家邮箱",User_Table ="ChembnbLogin")
buyerPW=DoExcel.File_Location().get_parameter("买家密码",User_Table ="ChembnbLogin")
registerPage=DoExcel.File_Location().get_parameter("注册页面",User_Table ="ChembnbLogin")
forgotpwPage=DoExcel.File_Location().get_parameter("忘记密码界面",User_Table ="ChembnbLogin")
okchemHome=DoExcel.File_Location().get_parameter("回到OKCHEMS首页",User_Table ="ChembnbLogin")
num=0

class ChembnbLogin(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.url=url
        self.buyerLoginSuccess=buyerLoginSuccess
        self.buyerMail=buyerMail
        self.buyerPW=buyerPW
        self.registerPage=registerPage
        self.forgotpwPage=forgotpwPage
        self.okchemHome=okchemHome
        self.BL=ChembnbLoginPage.ChembnbLoginPage()
        self.BL.open(self.url)

    def save_img(self, img_name):
        img_path=globalconfig.picture_path1
        self.BL.driver.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(img_path), img_name))

    @BeautifulReport.add_test_img("testChembnbLogin_001")
    def testChembnbLogin_001(self):
        """测试Chembnb平台注册界面"""
        ele=self.BL.findElement(ChembnbLoginPage.ChembnbLoginPage.Register)
        self.BL.click(ele)
        sleep(2)
        actual = self.BL.getText(ChembnbLoginPage.ChembnbLoginPage.Register_exp)
        self.assertIn(self.registerPage, actual)

    @BeautifulReport.add_test_img("testChembnbLogin_002")
    def testChembnbLogin_002(self):
        """测试Chembnb平台忘记密码界面"""
        ele=self.BL.findElement(ChembnbLoginPage.ChembnbLoginPage.SignIn_LinkText)
        self.BL.click(ele)
        ele1=self.BL.findElement(ChembnbLoginPage.ChembnbLoginPage.Forgotpasswd)
        self.BL.click(ele1)
        sleep(2)
        actual = self.BL.getText(ChembnbLoginPage.ChembnbLoginPage.Forgotpasswd_exp)
        self.assertEqual(self.forgotpwPage, actual)

    @BeautifulReport.add_test_img("testChembnbLogin_003")
    def testChembnbLogin_003(self):
        """测试Chembnb平台登录界面回到首页"""
        ele=self.BL.findElement(ChembnbLoginPage.ChembnbLoginPage.SignIn_LinkText)
        self.BL.click(ele)
        ele1=self.BL.findElement(ChembnbLoginPage.ChembnbLoginPage.Logo)
        self.BL.click(ele1)
        sleep(2)
        actual = self.BL.getText(ChembnbLoginPage.ChembnbLoginPage.Logo_exp)
        self.assertIn(actual, self.okchemHome)

    @BeautifulReport.add_test_img("testChembnbLogin_004")
    def testChembnbLogin_004(self):
        """测试Chembnb平台买家登录"""
        ele=self.BL.findElement(ChembnbLoginPage.ChembnbLoginPage.SignIn_LinkText)
        self.BL.click(ele)
        usrname=self.BL.findElement(ChembnbLoginPage.ChembnbLoginPage.Username_Id)
        self.BL.type(usrname,self.buyerMail)
        password=self.BL.findElement(ChembnbLoginPage.ChembnbLoginPage.Password_Id)
        self.BL.type(password,self.buyerPW)
        ele1 = self.BL.findElement(ChembnbLoginPage.ChembnbLoginPage.SignIn_Btn)
        self.BL.click(ele1)
        sleep(2)
        actual=self.BL.getText(ChembnbLoginPage.ChembnbLoginPage.BuyerLogin_exp)
        self.assertEqual(self.buyerLoginSuccess,actual)

    def tearDown(self):
        global num
        num=num+1
        if num>=10:
            fangfa='testChembnbLogin_0'+str(num)
            xx=getattr(ChembnbLogin(),fangfa)
            self.log =xx.__doc__
        elif num<10:
            fangfa='testChembnbLogin_00'+str(num)
            xx = getattr(ChembnbLogin(), fangfa)
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
                screenname = screen_path + pattern + 'screenpicture' + now + '.png'
                print(screenname)
                self.BL.getPicture(screenname)  #进行截图处理
                sendEmail = dd.Email() #实例化类
                new_pic = sendEmail.newReport(screen_path) #获取最新的截图
                content1=result.errors[0][-1]
                content=content1.replace('File','<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;File').replace('During','<br/><br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;During')
                sendEmail.email_Text(new_pic,"注意！测试用例执行失败了！！！",self.log,content)  #发送邮件
                self.BL.driver.refresh()
        handles=self.BL.getAllHandles()
        if len(handles)>1:
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