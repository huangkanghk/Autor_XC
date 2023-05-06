import unittest,time,os,platform
from time import sleep
import logging
from log import log
from Public.common import TestCaseInfo,DoExcel,CommonConfig as cc
from Public.pages import QutoManagePage
from config import globalconfig
from BeautifulReport import BeautifulReport
from run import *
from Public.common import send_mail as dd
from PIL import Image,ImageEnhance,ImageFilter,ImageDraw
import  pytesseract,cv2,sys,os
import  requests,json,redis,pymysql,re
import datetime
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

url = DoExcel.File_Location().get_parameter("地址",User_Table ="quot")
qutoText = DoExcel.File_Location().get_parameter("报价单查询",User_Table ="quot")
searchButton = DoExcel.File_Location().get_parameter("搜索",User_Table ="quot")
resetButton = DoExcel.File_Location().get_parameter("重置",User_Table ="quot")
quotSearchT = DoExcel.File_Location().get_parameter("报价单单号",User_Table ="quot")
quotSearchUrl = DoExcel.File_Location().get_parameter("查询报价单",User_Table ="quot")

codeUrl = DoExcel.File_Location().get_parameter("获取验证码接口地址",User_Table ="Login")
loginUrl = DoExcel.File_Location().get_parameter("登录接口地址",User_Table ="Login")
redisIp = DoExcel.File_Location().get_parameter("redis地址",User_Table ="Login")
redisPort = DoExcel.File_Location().get_parameter("redis端口",User_Table ="Login")
redisPW = DoExcel.File_Location().get_parameter("redis密码",User_Table ="Login")
login_user = DoExcel.File_Location().get_parameter("账号",User_Table ="Login")
login_pw = DoExcel.File_Location().get_parameter("密码",User_Table ="Login")

num=0
BL =''
token =''

class TestQutoManage(unittest.TestCase):

    def setUp(self):
        self.url=url
        self.qutoText=qutoText
        self.qutoText = qutoText
        self.searchButton = searchButton
        self.resetButton = resetButton
        self.quotSearchT = quotSearchT
        self.quotSearchUrl = quotSearchUrl

        self.codeUrl = codeUrl
        self.loginUrl = loginUrl
        self.redisIp = redisIp
        self.redisPort = redisPort
        self.redisPW = redisPW
        self.login_user = login_user
        self.login_pw = login_pw

        if token == '':
            self.BL = QutoManagePage.QutoManagePage()
            self.BL.open(self.url)
        else:
            self.BL = BL

    def save_img(self, img_name):
        img_path=globalconfig.picture_path1
        self.BL.driver.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(img_path), img_name))

    @BeautifulReport.add_test_img("testQutoManage_001")
    def testQutoManage_001(self):
        """测试我的报价单页面是否正常展示"""
        sleep(2)
        codeUrl = self.codeUrl
        response = requests.get(codeUrl, params={})
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
        global token
        token = response["token"]

        global add_cookie
        add_cookie = {'name': 'Admin-Token', 'value': token, 'path': '/'}
        self.BL.driver.add_cookie(add_cookie)
        self.BL.driver.refresh()
        global BL
        BL = self.BL
        self.BL.open(self.url)
        sleep(2)
        homeName=self.BL.findElement(self.BL.homeName).text
        self.assertEqual("我的报价单",homeName)

        qutoText = self.BL.findElement(self.BL.qutoText).text
        self.assertEqual(self.qutoText, qutoText)

        searchButton = self.BL.findElement(self.BL.searchButton).text
        self.assertEqual(self.searchButton, searchButton)

        resetButton = self.BL.findElement(self.BL.resetButton).text
        self.assertEqual(self.resetButton, resetButton)

    @BeautifulReport.add_test_img("testQutoManage_002")
    def testQutoManage_002(self):
        """测试我的报价单页面查询条件是否有效"""
        quotSearchText = self.BL.findElement(self.BL.quotSearchT)
        self.BL.type(quotSearchText, self.quotSearchT)
        searchButton  =  self.BL.findElement(self.BL.searchButton)
        self.BL.click(searchButton);
        sleep(2)
        quotCount = self.BL.findElement(self.BL.quotCount).text
        quotCount = re.findall(r'\d+', quotCount)
        if len(quotCount) > 0:
            quotCount = quotCount[0]
            quotCount = int(quotCount)

        headers = {"Content-Type": "application/json;charset=UTF-8","Authorization":"Bearer "+token}
        params = {}
        self.quotSearchUrl = self.quotSearchUrl + "quotName=" + quotSearchT
        response = requests.get(self.quotSearchUrl, headers=headers, data=json.dumps(params))
        response = response.text
        response = json.loads(response)
        qutoCountT = response["total"]

        self.assertEqual(quotCount,qutoCountT)

    @BeautifulReport.add_test_img("testQutoManage_003")
    def testQutoManage_003(self):
        """测试我的报价单页面重置按钮是否有效"""
        resetButton = self.BL.findElement(self.BL.resetButton)
        self.BL.click(resetButton);
        sleep(2)
        quotCount = self.BL.findElement(self.BL.quotCount).text
        quotCount = re.findall(r'\d+', quotCount)
        if len(quotCount) > 0:
            quotCount = quotCount[0]
            quotCount = int(quotCount)

        headers = {"Content-Type": "application/json;charset=UTF-8", "Authorization": "Bearer " + token}
        params = {}
        self.quotSearchUrl = self.quotSearchUrl + "pageNum=1&pageSize=20"
        response = requests.get(self.quotSearchUrl, headers=headers, data=json.dumps(params))
        response = response.text
        response = json.loads(response)
        qutoCountT = response["total"]
        self.assertEqual(quotCount, qutoCountT)

    @BeautifulReport.add_test_img("testQutoManage_004")
    def testQutoManage_004(self):
        """测试我的报价单页面创建按钮是否有效"""
        qutoCreate = self.BL.findElement(self.BL.qutoCreate)
        self.BL.click(qutoCreate);
        sleep(2)
        TimeText = self.BL.findElement(self.BL.TimeText).text

        self.assertEqual("新建报价单请选择交付时间", TimeText)

    @BeautifulReport.add_test_img("testQutoManage_005")
    def testQutoManage_005(self):
        """测试我的报价单页面新建页面未输入数据是否有效"""
        quotSure = self.BL.findElement(self.BL.quotSure)
        self.BL.click(quotSure);
        sleep(2)
        TimeText = self.BL.findElement(self.BL.TimeText).text

        self.assertEqual("新建报价单请选择交付时间", TimeText)

    @BeautifulReport.add_test_img("testQutoManage_006")
    def testQutoManage_006(self):
        """测试我的报价单页面新建页面输入数据是否跳转"""
        quotData = self.BL.findElement(self.BL.quotData)
        year = datetime.datetime.now().year
        month = datetime.datetime.now().month
        day = datetime.datetime.now().day
        date = str(year) + "-" + str(month) + "-" + str(day)
        self.BL.type(quotData,date)

        quotSure = self.BL.findElement(self.BL.quotSure)
        TimeText = self.BL.findElement(self.BL.TimeText)
        self.BL.click(TimeText)
        self.BL.click(quotSure)
        sleep(2)
        createQuot = self.BL.findElement(self.BL.createQu).text
        self.assertEqual(createQuot, "添加产品")

    @BeautifulReport.add_test_img("testQutoManage_007")
    def testQutoManage_007(self):
        """测试我的报价单页面新建页面未输入数据取消是否跳转"""
        self.BL.open(self.url)
        qutoCreate = self.BL.findElement(self.BL.qutoCreate)
        self.BL.click(qutoCreate);

        quotCancle = self.BL.findElement(self.BL.quotCancle)
        self.BL.click(quotCancle)

        homeName = self.BL.findElement(self.BL.homeName).text
        self.assertEqual("我的报价单", homeName)
        qutoText = self.BL.findElement(self.BL.qutoText).text
        self.assertEqual(self.qutoText, qutoText)

    @BeautifulReport.add_test_img("testQutoManage_008")
    def testQutoManage_008(self):
        """测试我的报价单页面新建页面输入数据取消是否跳转"""
        self.BL.open(self.url)
        qutoCreate = self.BL.findElement(self.BL.qutoCreate)
        self.BL.click(qutoCreate);

        quotData = self.BL.findElement(self.BL.quotData)
        year = datetime.datetime.now().year
        month = datetime.datetime.now().month
        day = datetime.datetime.now().day
        date = str(year) + "-" + str(month) + "-" + str(day)
        self.BL.type(quotData, date)

        quotSure = self.BL.findElement(self.BL.quotSure)
        TimeText = self.BL.findElement(self.BL.TimeText)
        self.BL.click(TimeText)

        quotCancle = self.BL.findElement(self.BL.quotCancle)
        self.BL.click(quotCancle)

        homeName = self.BL.findElement(self.BL.homeName).text
        self.assertEqual("我的报价单", homeName)
        qutoText = self.BL.findElement(self.BL.qutoText).text
        self.assertEqual(self.qutoText, qutoText)

    def tearDown(self):
        global num
        num=num+1
        if num>=10:
            fangfa='testQutoManage_0'+str(num)
            xx=getattr(TestQutoManage(),fangfa)
            self.log =xx.__doc__
        elif num<10:
            fangfa='testQutoManage_00'+str(num)
            xx = getattr(TestQutoManage(), fangfa)
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
        TestCase = unittest.defaultTestLoader.getTestCaseNames(TestQutoManage)
        if num == len(TestCase):
            self.BL.quit()
        else:
            sleep(1)

    def list2reason(self, exc_list):
        if exc_list and exc_list[-1][0] is self:
            return exc_list[-1][1]

