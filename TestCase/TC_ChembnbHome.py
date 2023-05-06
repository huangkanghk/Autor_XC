import unittest,time,os,platform
from Public.common import DoExcel
from Public.pages import ChembnbHomePage
from time import sleep
from config import globalconfig
from BeautifulReport import BeautifulReport
from Public.common import send_mail as dd

url=DoExcel.File_Location().get_parameter("Chembnb地址",User_Table ="ChembnbLogin")
ProductSearchPage=DoExcel.File_Location().get_parameter("搜索产品结果页",User_Table ="ChembnbHome")
PostBuyingRequest=DoExcel.File_Location().get_parameter("采购需求提交页",User_Table ="ChembnbHome")
IncreaseSales=DoExcel.File_Location().get_parameter("IncreaseSales页",User_Table ="ChembnbHome")
BecomeOurParner=DoExcel.File_Location().get_parameter("成为合作伙伴",User_Table ="ChembnbHome")
GroupBuyingDetail=DoExcel.File_Location().get_parameter("集采详情界面",User_Table ="ChembnbHome")
Minioffice=DoExcel.File_Location().get_parameter("Minioffice详情页",User_Table ="ChembnbHome")
CreditLoan=DoExcel.File_Location().get_parameter("CreditLoan详情页",User_Table ="ChembnbHome")
ContactUs=DoExcel.File_Location().get_parameter("ContactUs页面",User_Table ="ChembnbHome")
num=0

class ChembnbHome(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.url=url
        self.ProductSearchPage=ProductSearchPage
        self.PostBuyingRequest=PostBuyingRequest
        self.IncreaseSales=IncreaseSales
        self.BecomeOurParner=BecomeOurParner
        self.GroupBuyingDetail=GroupBuyingDetail
        self.Minioffice=Minioffice
        self.CreditLoan=CreditLoan
        self.ContactUs=ContactUs
        self.BL=ChembnbHomePage.ChembnbHomePage()
        self.BL.open(self.url)

    def save_img(self, img_name):
        img_path=globalconfig.picture_path1
        self.BL.driver.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(img_path), img_name))

    @BeautifulReport.add_test_img("testChembnbHome_001")
    def testChembnbHome_001(self):
        """测试Chembnb平台在首页搜索热搜产品"""
        ele=self.BL.findElement(ChembnbHomePage.ChembnbHomePage.HotSearchKey)
        self.BL.click(ele)
        actual=self.BL.getText(ChembnbHomePage.ChembnbHomePage.HotSearchKey_exp)
        self.assertIn(self.ProductSearchPage,actual)

    @BeautifulReport.add_test_img("testChembnbHome_002")
    def testChembnbHome_002(self):
        """测试Chembnb平台在首页点击PostBuyingRequest"""
        ele=self.BL.findElement(ChembnbHomePage.ChembnbHomePage.PostBuyingRequest)
        self.BL.click(ele)
        actual=self.BL.getText(ChembnbHomePage.ChembnbHomePage.PostBuyingRequest_exp)
        self.assertEqual(self.PostBuyingRequest,actual)

    @BeautifulReport.add_test_img("testChembnbHome_003")
    def testChembnbHome_003(self):
        """测试Chembnb平台在首页点击IncreaseSales"""
        ele=self.BL.findElement(ChembnbHomePage.ChembnbHomePage.IncreaseSales)
        self.BL.click(ele)
        actual=self.BL.getText(ChembnbHomePage.ChembnbHomePage.IncreaseSales_exp)
        self.assertEqual(self.IncreaseSales,actual)

    @BeautifulReport.add_test_img("testChembnbHome_004")
    def testChembnbHome_004(self):
        """测试Chembnb平台在首页点击Become Our Partner"""
        ele=self.BL.findElement(ChembnbHomePage.ChembnbHomePage.BecomeOurPartner)
        self.BL.click(ele)
        sleep(5)
        actual=self.BL.driver.title
        self.assertEqual(self.BecomeOurParner,actual)

    @BeautifulReport.add_test_img("testChembnbHome_005")
    def testChembnbHome_005(self):
        """测试Chembnb平台在首页点击第一个集采图片"""
        ele=self.BL.findElement(ChembnbHomePage.ChembnbHomePage.GroupBuyingImage)
        self.BL.click(ele)
        actual = self.BL.getText(ChembnbHomePage.ChembnbHomePage.GroupBuyingImage_exp)
        self.assertIn(self.GroupBuyingDetail,actual)

    @BeautifulReport.add_test_img("testChembnbHome_006")
    def testChembnbHome_006(self):
        """测试Chembnb平台在首页点击底部Minioffice"""
        self.BL.scrollTo(ChembnbHomePage.ChembnbHomePage.MiniOffice)
        ele=self.BL.findElement(ChembnbHomePage.ChembnbHomePage.MiniOffice)
        self.BL.click(ele)
        actual = self.BL.getText(ChembnbHomePage.ChembnbHomePage.MiniOffice_exp)
        self.assertIn(self.Minioffice,actual)

    @BeautifulReport.add_test_img("testChembnbHome_007")
    def testChembnbHome_007(self):
        """测试Chembnb平台在首页点击底部Credit Loan"""
        self.BL.scrollTo(ChembnbHomePage.ChembnbHomePage.CreditLoan)
        ele=self.BL.findElement(ChembnbHomePage.ChembnbHomePage.CreditLoan)
        self.BL.click(ele)
        actual = self.BL.getText(ChembnbHomePage.ChembnbHomePage.CreditLoan_exp)
        self.assertIn(self.CreditLoan,actual)

    @BeautifulReport.add_test_img("testChembnbHome_008")
    def testChembnbHome_008(self):
        """测试Chembnb平台在首页点击底部Go to contact us"""
        self.BL.scrollTo(ChembnbHomePage.ChembnbHomePage.ContactUs)
        ele=self.BL.findElement(ChembnbHomePage.ChembnbHomePage.ContactUs)
        self.BL.click(ele)
        actual = self.BL.getText(ChembnbHomePage.ChembnbHomePage.ContactUs_exp)
        self.assertIn(self.ContactUs,actual)

    def tearDown(self):
        global num
        num=num+1
        if num>=10:
            fangfa='testChembnbHome_0'+str(num)
            xx=getattr(ChembnbHome(),fangfa)
            self.log =xx.__doc__
        elif num<10:
            fangfa='testChembnbHome_00'+str(num)
            xx = getattr(ChembnbHome(), fangfa)
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
                screenname = screen_path +pattern + 'screenpicture' + now + '.png'
                print(screenname)
                self.BL.getPicture(screenname)  #进行截图处理
                sendEmail = dd.Email() #实例化类
                new_pic = sendEmail.newReport(screen_path) #获取最新的截图
                content1=result.errors[0][-1]
                content=content1.replace('File','<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;File').replace('During','<br/><br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;During')
                sendEmail.email_Text(new_pic,"注意！测试用例执行失败了！！！",self.log,content)  #发送邮件
                self.BL.driver.refresh()
        list = self.BL.getAllHandles()
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
