import unittest,time,os,platform
from time import sleep
import logging
from log import log
from Public.common import TestCaseInfo,DoExcel,CommonConfig as cc
from Public.pages import OkchemLoginPage
from Public.pages import QutoLoginPage
from config import globalconfig
from BeautifulReport import BeautifulReport
from run import *
from Public.common import send_mail as dd
from PIL import Image,ImageEnhance,ImageFilter,ImageDraw
import  pytesseract,cv2,sys,os
import  requests,json,redis

url = DoExcel.File_Location().get_parameter("登录地址",User_Table ="Login")
login_title = DoExcel.File_Location().get_parameter("登录页title",User_Table ="Login")
login_text = DoExcel.File_Location().get_parameter("登录文本信息",User_Table ="Login")
login_user = DoExcel.File_Location().get_parameter("账号",User_Table ="Login")
login_pw = DoExcel.File_Location().get_parameter("密码",User_Table ="Login")
login_tip = DoExcel.File_Location().get_parameter("提示信息",User_Table ="Login")
windowBL = ''
user_tip = DoExcel.File_Location().get_parameter("用户名必填提示",User_Table ="Login")
pw_tip = DoExcel.File_Location().get_parameter("密码必填提示",User_Table ="Login")
vcode_tip = DoExcel.File_Location().get_parameter("验证码必填提示",User_Table ="Login")
vcoedError = DoExcel.File_Location().get_parameter("验证码错误提示",User_Table ="Login")
userError = DoExcel.File_Location().get_parameter("账号错误提示",User_Table ="Login")
pwError = DoExcel.File_Location().get_parameter("密码错误提示",User_Table ="Login")
homeName = DoExcel.File_Location().get_parameter("首页text",User_Table ="home")

codeUrl = DoExcel.File_Location().get_parameter("获取验证码接口地址",User_Table ="Login")
loginUrl = DoExcel.File_Location().get_parameter("登录接口地址",User_Table ="Login")
redisIp = DoExcel.File_Location().get_parameter("redis地址",User_Table ="Login")
redisPort = DoExcel.File_Location().get_parameter("redis端口",User_Table ="Login")
redisPW = DoExcel.File_Location().get_parameter("redis密码",User_Table ="Login")
num=0
token =''
windowBL = ''

class TestQutoLogin(unittest.TestCase):

    def setUp(self):
        self.url = url
        self.login_title = login_title
        self.login_text = login_text
        self.login_user = login_user
        self.login_pw = login_pw
        self.login_tip = login_tip
        self.user_tip = user_tip
        self.pw_tip = pw_tip
        self.vcode_tip = vcode_tip
        self.vcoedError = vcoedError
        self.userError = userError
        self.pwError = pwError
        self.homeName = homeName
        self.codeUrl = codeUrl
        self.loginUrl = loginUrl
        self.redisIp = redisIp
        self.redisPort = redisPort
        self.redisPW = redisPW
        self.BL = windowBL
        if self.BL == '':
            self.BL = QutoLoginPage.QutoLoginPage()
            self.BL.driver.delete_all_cookies()
            self.BL.open(self.url)
        sleep(2)

    def save_img(self, img_name):
        img_path=globalconfig.picture_path1
        self.BL.driver.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(img_path), img_name))


    @BeautifulReport.add_test_img("testQutoLogin_001")
    def testQutoLogin_001(self):
        """测试登录页面UI---红色文字提示信息是否正确"""
        #self.BL = QutoLoginPage.QutoLoginPage()
        #self.BL.open(self.url)
        # title =self.BL.findElement(self.BL.title).text
        # self.assertEqual(self.login_title,title)
        global  windowBL
        windowBL = self.BL
        # 文本信息
        text = self.BL.findElement(self.BL.text).text
        self.assertEqual(self.login_text, text)

        # 提示信息
        tip = self.BL.findElement(self.BL.tip).text
        self.assertEqual(self.login_tip,tip)

    @BeautifulReport.add_test_img("testQutoLogin_002")
    def testQutoLogin_002(self):
        """测试登录页面UI---底部日期显示信息是否正确"""
        # self.BL = QutoLoginPage.QutoLoginPage()
        # self.BL.open(self.url)
        # title =self.BL.findElement(self.BL.title).text
        # self.assertEqual(self.login_title,title)
        global windowBL
        windowBL = self.BL
        year = time.strftime("%Y", time.localtime())
        # 文本信息
        tdatetext = self.BL.findElement(self.BL.tdate).text
        self.assertEqual("Copyright © 2018-"+year+" 信创业务集团 .", tdatetext)

    @BeautifulReport.add_test_img("testQutoLogin_003")
    def testQutoLogin_003(self):
        """测试不输入账号密码是否有提示信息"""
        Login = self.BL.findElement(self.BL.loginButton)
        self.BL.click(Login)

        # 用户名提示信息
        userTip = self.BL.findElement(self.BL.userTip).text
        self.assertEqual(self.user_tip, userTip)

        # 密码提示信息
        pwTip = self.BL.findElement(self.BL.pwTip).text
        self.assertEqual(self.pw_tip, pwTip)

        # 验证码提示信息
        vcode_tip = self.BL.findElement(self.BL.vcodeTip).text
        self.assertEqual(self.vcode_tip, vcode_tip)

    @BeautifulReport.add_test_img("testQutoLogin_004")
    def testQutoLogin_004(self):
        """测试输入账号密码但验证码错误是否有提示信息"""
        Username = self.BL.findElement(self.BL.loginName)
        self.BL.type(Username,self.login_user)

        pw = self.BL.findElement(self.BL.pw)
        self.BL.type(pw, self.login_pw)

        vcode = self.BL.findElement(self.BL.vcodeInput)
        self.BL.type(vcode,999)

        Login = self.BL.findElement(self.BL.loginButton)
        self.BL.click(Login)

        # 验证码提示信息
        vcoedError = self.BL.findElement(self.BL.vcoedError).text
        self.assertEqual(self.vcoedError, vcoedError)

    @BeautifulReport.add_test_img("testQutoLogin_005")
    def testQutoLogin_005(self):
        """测试正常登录首页是否正常打开"""
        response = requests.get(self.codeUrl, params={})
        response = response.text
        response = json.loads(response)
        uuid = response["uuid"]

        r = redis.Redis(host=self.redisIp, password=self.redisPW, port=self.redisPort, db=0)
        keys = r.keys()
        key = 'captcha_codes:' + uuid
        code = r.get(key)
        code = code.decode("utf-8")
        code = json.loads(code)

        # 模拟登录获取token
        headers = {
            "Content-Type": "application/json;charset=UTF-8"
        }
        params = {"code": code, "password": self.login_pw, "username": self.login_user, "uuid": uuid}
        response = requests.post(self.loginUrl, headers=headers, data=json.dumps(params))
        response = response.text
        response = json.loads(response)

        global token
        token = response["token"]
        add_cookie = {'name': 'Admin-Token', 'value': token, 'path': '/'}
        self.BL.driver.add_cookie(add_cookie)
        self.BL.driver.refresh()

        homeName = self.BL.findElement(self.BL.homeName).text
        self.assertEqual(self.homeName, homeName)

    def tearDown(self):
        global num
        num=num+1
        if num>=10:
            fangfa='testQutoLogin_0'+str(num)
            xx=getattr(TestQutoLogin(),fangfa)
            self.log =xx.__doc__
        elif num<10:
            fangfa='testQutoLogin_00'+str(num)
            xx = getattr(TestQutoLogin(), fangfa)
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
        #self.BL.quit()
        TestCase = unittest.defaultTestLoader.getTestCaseNames(TestQutoLogin)
        if num == len(TestCase):
            self.BL.quit()
        else:
            sleep(2)
            self.BL.driver.refresh()

    def list2reason(self, exc_list):
        if exc_list and exc_list[-1][0] is self:
            return exc_list[-1][1]
