import unittest,time,os,platform
from time import sleep
import logging
from log import log
from Public.common import TestCaseInfo,DoExcel,CommonConfig as cc
from Public.pages import QutoHomePage
from TestCase import TC_QutoLogin
from config import globalconfig
from BeautifulReport import BeautifulReport
from run import *
from Public.common import send_mail as dd
from PIL import Image,ImageEnhance,ImageFilter,ImageDraw
import  pytesseract,cv2,sys,os
import  requests,json,redis,pymysql
import datetime
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

url = DoExcel.File_Location().get_parameter("首页地址",User_Table ="home")
homeName =DoExcel.File_Location().get_parameter("首页text",User_Table ="home")
qutoText =DoExcel.File_Location().get_parameter("我的报价单text",User_Table ="home")
createText =DoExcel.File_Location().get_parameter("创建报价单text",User_Table ="home")
shareText =DoExcel.File_Location().get_parameter("共享报价单text",User_Table ="home")

login_user = DoExcel.File_Location().get_parameter("账号",User_Table ="Login")
login_pw = DoExcel.File_Location().get_parameter("密码",User_Table ="Login")

qutonumUrl = DoExcel.File_Location().get_parameter("获取报价单数量URL",User_Table ="home")
sharenumUrl = DoExcel.File_Location().get_parameter("获取共享数量URL",User_Table ="home")

codeUrl = DoExcel.File_Location().get_parameter("获取验证码接口地址",User_Table ="Login")
loginUrl = DoExcel.File_Location().get_parameter("登录接口地址",User_Table ="Login")
redisIp = DoExcel.File_Location().get_parameter("redis地址",User_Table ="Login")
redisPort = DoExcel.File_Location().get_parameter("redis端口",User_Table ="Login")
redisPW = DoExcel.File_Location().get_parameter("redis密码",User_Table ="Login")

quotCountMsg = DoExcel.File_Location().get_parameter("报价单统计页签",User_Table ="home")
qutoTitle1 = DoExcel.File_Location().get_parameter("个人信息标题1",User_Table ="home")
qutoTitle2 = DoExcel.File_Location().get_parameter("个人信息标题2",User_Table ="home")
qutoTitle3 = DoExcel.File_Location().get_parameter("个人信息标题3",User_Table ="home")
qutoTitle4 = DoExcel.File_Location().get_parameter("个人信息标题4",User_Table ="home")
qutoTitle5 = DoExcel.File_Location().get_parameter("个人信息标题5",User_Table ="home")

num=0
BL =''
token =''
class TestQutoHome(unittest.TestCase):

    def setUp(self):
        self.url=url
        self.homeName=homeName
        self.qutoText = qutoText
        self.createText = createText
        self.shareText = shareText
        self.qutonumUrl = qutonumUrl
        self.sharenumUrl = sharenumUrl

        self.login_user = login_user
        self.login_pw = login_pw

        self.codeUrl = codeUrl
        self.loginUrl = loginUrl
        self.redisIp = redisIp
        self.redisPort = redisPort
        self.redisPW = redisPW

        self.quotCountMsg = quotCountMsg
        self.qutoTitle1 = qutoTitle1
        self.qutoTitle2 = qutoTitle2
        self.qutoTitle3 = qutoTitle3
        self.qutoTitle4 = qutoTitle4
        self.qutoTitle5 = qutoTitle5

        if BL == '':
            self.BL = QutoHomePage.QutoHomePage()
            self.BL.driver.delete_all_cookies()
            self.BL.open(self.url)
        else:
            self.BL = BL

    def save_img(self, img_name):
        img_path=globalconfig.picture_path1
        self.BL.driver.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(img_path), img_name))

    @BeautifulReport.add_test_img("testQutoHome_001")
    def testQutoHome_001(self):
        """测试首页页面是否正常展示"""
        url = self.codeUrl
        sleep(2)
        response = requests.get(url, params={})
        response = response.text
        response = json.loads(response)
        print(response)
        uuid = response["uuid"]

        ip = self.redisIp
        r = redis.Redis(host=ip, password=self.redisPW, port=self.redisPort, db=0)
        keys = r.keys()
        key = 'captcha_codes:' + uuid
        code = r.get(key)
        code = code.decode("utf-8")
        code = json.loads(code)

        # 模拟登录获取token
        loginUrl = self.loginUrl
        headers = {
            "Content-Type": "application/json;charset=UTF-8"
        }
        params = {"code": code, "password": self.login_pw, "username": self.login_user, "uuid": uuid}
        response = requests.post(loginUrl, headers=headers, data=json.dumps(params))
        response = response.text
        response = json.loads(response)
        global  token
        token = response["token"]

        global add_cookie
        add_cookie = {'name': 'Admin-Token', 'value': token, 'path': '/'}
        self.BL.driver.add_cookie(add_cookie)
        self.BL.driver.refresh()
        global BL
        BL = self.BL

        homeName=self.BL.findElement(self.BL.homeName).text
        self.assertEqual(self.homeName,homeName)

        qutoText = self.BL.findElement(self.BL.qutoText).text
        self.assertEqual(self.qutoText, qutoText)

        createText = self.BL.findElement(self.BL.createText).text
        self.assertEqual(self.createText, createText)

        shareText = self.BL.findElement(self.BL.shareText).text
        self.assertEqual(self.shareText, shareText)

    @BeautifulReport.add_test_img("testQutoHome_002")
    def testQutoHome_002(self):
        """测试报价单数量和共享报价单数量是否正确"""

        headers = {"Content-Type": "application/json;charset=UTF-8","Authorization":"Bearer "+token}
        params = {}
        response = requests.get(self.qutonumUrl, headers=headers, data=json.dumps(params))
        response = response.text
        response = json.loads(response)
        qutoCount = response["count"]
        qutoCount = int(qutoCount)

        self.sharenumUrl = self.sharenumUrl + self.login_user
        response = requests.get(self.sharenumUrl, headers=headers, data=json.dumps(params))
        response = response.json()
        shareCount = response["count"]
        shareCount = int(shareCount)

        qutoNum = self.BL.findElement(self.BL.qutoNum).text
        shareNum = self.BL.findElement(self.BL.shareNum).text
        qutoNum = int(str.replace(qutoNum,',',''))
        shareNum = int(str.replace(shareNum, ',', ''))


        self.assertEqual(qutoCount,qutoNum)
        self.assertEqual(shareCount, shareNum)

    @BeautifulReport.add_test_img("testQutoHome_003")
    def testQutoHome_003(self):
        """首页报价单统计页签内容是否展示正常"""
        quotCountMsg = self.BL.findElement(self.BL.quotCountMsg).text
        self.assertEqual(self.quotCountMsg, quotCountMsg)

        qutoTitle1 = self.BL.findElement(self.BL.qutoTitle1).text
        self.assertEqual(self.qutoTitle1, qutoTitle1)

        qutoTitle2 = self.BL.findElement(self.BL.qutoTitle2).text
        self.assertEqual(self.qutoTitle2, qutoTitle2)

        qutoTitle3 = self.BL.findElement(self.BL.qutoTitle3).text
        self.assertEqual(self.qutoTitle3, qutoTitle3)

        qutoTitle4 = self.BL.findElement(self.BL.qutoTitle4).text
        self.assertEqual(self.qutoTitle4, qutoTitle4)

        qutoTitle5 = self.BL.findElement(self.BL.qutoTitle5).text
        self.assertEqual(self.qutoTitle5, qutoTitle5)

    @BeautifulReport.add_test_img("testQutoHome_004")
    def testQutoHome_004(self):
        """首页 翻转操作页面是否正常展示"""
        title3Buttn = self.BL.findElement(self.BL.title3Buttn)
        self.BL.click(title3Buttn)
        qutoTitle33 = DoExcel.File_Location().get_parameter("个人信息标题33", User_Table="home")
        qutoTitle3 = self.BL.findElement(self.BL.qutoTitle3).text
        self.assertEqual(qutoTitle3, qutoTitle33)

        title4Buttn = self.BL.findElement(self.BL.title4Buttn)
        self.BL.click(title4Buttn)
        qutoTitle44 = DoExcel.File_Location().get_parameter("个人信息标题44", User_Table="home")
        qutoTitle4 = self.BL.findElement(self.BL.qutoTitle4).text
        self.assertEqual(qutoTitle4, qutoTitle44)

        title5Buttn = self.BL.findElement(self.BL.title5Buttn)
        self.BL.click(title5Buttn)
        qutoTitle55 = DoExcel.File_Location().get_parameter("个人信息标题55", User_Table="home")
        qutoTitle5 = self.BL.findElement(self.BL.qutoTitle5).text
        self.assertEqual(qutoTitle5, qutoTitle55)

    @BeautifulReport.add_test_img("testQutoHome_005")
    def testQutoHome_005(self):
        """首页 年份下拉数据是否展示正常"""
        year = self.BL.findElement(self.BL.year)
        self.BL.click(self.BL.findElement(self.BL.year))

        years = self.BL.findElement(self.BL.years).text
        thisYear = time.strftime("%Y", time.localtime())
        flag = thisYear in years

    @BeautifulReport.add_test_img("testQutoHome_006")
    def testQutoHome_006(self):
        """首页 正常加载下点击报价单是否跳转正常"""
        self.BL.open(self.url)
        myQuoted = self.BL.findElement(self.BL.myQuoted)
        self.BL.click(myQuoted)

        searchQuot = self.BL.findElement(self.BL.searchQuot).text
        self.assertEqual(searchQuot, "报价单查询")

    @BeautifulReport.add_test_img("testQutoHome_007")
    def testQutoHome_007(self):
        """首页 正常加载下点击共享报价单是否跳转正常"""
        self.BL.open(self.url)
        shareQuot = self.BL.findElement(self.BL.shareQuot)
        self.BL.click(shareQuot)

        shareQuot = self.BL.findElement(self.BL.reciveShare).text
        self.assertEqual(shareQuot, "收到的共享")

    @BeautifulReport.add_test_img("testQutoHome_008")
    def testQutoHome_008(self):
        """首页 正常加载下点击创建报价单是否跳转正常"""
        self.BL.open(self.url)
        createQu = self.BL.findElement(self.BL.createQu)
        self.BL.click(createQu)

        quotSure = self.BL.findElement(self.BL.quotSure)
        self.BL.click(quotSure);
        sleep(2)
        TimeText = self.BL.findElement(self.BL.TimeText).text

        self.assertEqual("新建报价单请选择交付时间", TimeText)

        createQuot = self.BL.findElement(self.BL.createQuot).text
        self.assertEqual(createQuot, "添加产品")

    def tearDown(self):
        global num
        num=num+1
        if num>=10:
            fangfa='testQutoHome_0'+str(num)
            xx=getattr(TestQutoHome(),fangfa)
            self.log =xx.__doc__
        elif num<10:
            fangfa='testQutoHome_00'+str(num)
            xx = getattr(TestQutoHome(), fangfa)
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
        TestCase = unittest.defaultTestLoader.getTestCaseNames(TestQutoHome)
        if num == len(TestCase):
            self.BL.quit()
        else:
            sleep(1)

    def list2reason(self, exc_list):
        if exc_list and exc_list[-1][0] is self:
            return exc_list[-1][1]

