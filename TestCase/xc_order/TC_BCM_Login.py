from builtins import str
from TestCase.xc_order.page import TC_BCM_loginPage
import platform
from time import sleep
from Public.common import DoExcel
from run import *
from Public.common import send_mail as dd
import xc_common

url = DoExcel.File_Location().get_parameter("登录地址",User_Table ="登录信息")
itcode = DoExcel.File_Location().get_parameter("账号",User_Table ="登录信息")
itpw = DoExcel.File_Location().get_parameter("密码",User_Table ="登录信息")
num =0

class TestBCMLogin(unittest.TestCase):

    def setUp(self):
        self.url = url
        self.itcode = itcode
        self.itpw = itpw
        self.BL = xc_common.WindowsBL
        if self.BL == '':
            self.BL = TC_BCM_loginPage.BCMLoginPage()
            self.BL.driver.delete_all_cookies()
            self.BL.open(self.url)
        sleep(2)


    def save_img(self, img_name):
        img_path=globalconfig.picture_path1
        self.BL.driver.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(img_path), img_name))
        sleep(2)


    @BeautifulReport.add_test_img("testBCMLogin_001")
    def testBCMLogin_001(self):
        """ odoo登录 """
        xc_common.set_WindowsBL(self.BL)
        itcode = self.BL.findElement(self.BL.itcode)
        self.BL.type(itcode, self.itcode)

        pw = self.BL.findElement(self.BL.itpw)
        self.BL.type(pw, self.itpw)

        loginButton = self.BL.findElement(self.BL.loginButton)
        self.BL.click(loginButton)

        cookie_lists = self.BL.driver.get_cookies()
        cookies =''
        for cookie_list in cookie_lists:
            for cookie_tab in cookie_list:
                if cookie_list[cookie_tab] == "session_id":
                    cookies = cookie_list["value"]
                    xc_common.set_Cookies(cookies)
                    break
            if cookies != '':
                break
        if cookies =="":
            raise Exception("获取登录信息异常")

    def tearDown(self):
        global num
        num=num+1
        if num>=10:
            fangfa='testBCMLogin_0'+str(num)
            xx=getattr(TestBCMLogin(),fangfa)
            self.log =xx.__doc__
        elif num<10:
            fangfa='testBCMLogin_00'+str(num)
            xx = getattr(TestBCMLogin(), fangfa)
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
                content = content1.replace('File', '<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;File').replace('During','<br/><br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;During')
                sendEmail.email_Text_All(new_pic, "致命！系统报500错误了！！！", self.log, content)  # 发送邮件
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
                content1 = result.errors[0][-1]
                content = content1.replace('File', '<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;File').replace('During','<br/><br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;During')
                sendEmail.email_Text(new_pic, "注意！测试用例执行失败了！！！", self.log, content)  # 发送邮件
                self.BL.driver.refresh()
        #self.BL.quit()
        TestCase = unittest.defaultTestLoader.getTestCaseNames(TestBCMLogin)
        # if num == len(TestCase):
        #     self.BL.quit()
        # else:
        #     sleep(2)
        #     self.BL.driver.refresh()

    def list2reason(self, exc_list):
        if exc_list and exc_list[-1][0] is self:
            return exc_list[-1][1]

