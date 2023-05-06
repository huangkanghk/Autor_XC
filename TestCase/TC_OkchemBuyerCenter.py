import unittest,time,os,platform
from Public.common import TestCaseInfo,DoExcel,CommonConfig as cc
from Public.pages import OkchemBuyerCenterPage
from time import sleep
from config import globalconfig
from BeautifulReport import BeautifulReport
from Public.common import send_mail as dd

url=DoExcel.File_Location().get_parameter("PRE地址")
buyer_un=DoExcel.File_Location().get_parameter("OKCHEM买家账号")
buyer_pw=DoExcel.File_Location().get_parameter("OKCHEM买家密码")
home_text=DoExcel.File_Location().get_parameter("Home页面",User_Table="BuyerCenter")
product_text=DoExcel.File_Location().get_parameter("收藏的产品",User_Table="BuyerCenter")
supplier_text=DoExcel.File_Location().get_parameter("收藏的店铺",User_Table="BuyerCenter")
myinquiry_text=DoExcel.File_Location().get_parameter("我的询价",User_Table="BuyerCenter")
mymessage_text=DoExcel.File_Location().get_parameter("我的消息",User_Table="BuyerCenter")
mybuyingrequest_text=DoExcel.File_Location().get_parameter("我的采购需求",User_Table="BuyerCenter")
myserviceorder_text=DoExcel.File_Location().get_parameter("我的服务订单",User_Table="BuyerCenter")
mycredit_text=DoExcel.File_Location().get_parameter("信用贷服务",User_Table="BuyerCenter")
myrefer_text=DoExcel.File_Location().get_parameter("我的收支",User_Table="BuyerCenter")
myprofile_text=DoExcel.File_Location().get_parameter("我的资料",User_Table="BuyerCenter")
myprefer_text=DoExcel.File_Location().get_parameter("个人喜好",User_Table="BuyerCenter")
changepw_text=DoExcel.File_Location().get_parameter("修改密码",User_Table="BuyerCenter")
logout_text=DoExcel.File_Location().get_parameter("退出登录",User_Table="BuyerCenter")
num=0

class TestOkchemBuyerCenter(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.url=url
        self.buyer_un=buyer_un
        self.buyer_pw=buyer_pw
        self.home_text=home_text
        self.product_text=product_text
        self.supplier_text=supplier_text
        self.myinquiry_text=myinquiry_text
        self.mymessage_text=mymessage_text
        self.mybuyingrequest_text=mybuyingrequest_text
        self.myserviceorder_text=myserviceorder_text
        self.mycredit_text=mycredit_text
        self.myrefer_text=myrefer_text
        self.myprofile_text = myprofile_text
        self.myprefer_text = myprefer_text
        self.changepw_text = changepw_text
        self.logout_text = logout_text
        self.BL=OkchemBuyerCenterPage.OkchemBuyerCenterPage()
        self.BL.LoginBuyerCenter(self.buyer_un,self.buyer_pw)

    def save_img(self, img_name):
        img_path=globalconfig.picture_path1
        self.BL.driver.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(img_path), img_name))

    @BeautifulReport.add_test_img("testBuyerCenter_001")
    def testBuyerCenter_001(self):
        """测试国际站买家中心Home页面"""
        home_exp=self.BL.findElement(OkchemBuyerCenterPage.OkchemBuyerCenterPage.Home_exp).text
        self.assertEqual(self.home_text,home_exp)

    @BeautifulReport.add_test_img("testBuyerCenter_002")
    def testBuyerCenter_002(self):
        """测试国际站买家中心收藏的产品页面"""
        product_exp=self.BL.findElement(OkchemBuyerCenterPage.OkchemBuyerCenterPage.Wishlist_link)
        self.BL.click(product_exp)
        self.BL.waitText(OkchemBuyerCenterPage.OkchemBuyerCenterPage.FavoriteProduct_link)
        product_exp1=self.BL.findElement(OkchemBuyerCenterPage.OkchemBuyerCenterPage.FavoriteProduct_link)
        self.BL.click(product_exp1)
        self.BL.waitContainText(OkchemBuyerCenterPage.OkchemBuyerCenterPage.FavoriteProduct_exp,self.product_text)
        product_exp2=self.BL.findElement(OkchemBuyerCenterPage.OkchemBuyerCenterPage.FavoriteProduct_exp).text
        self.assertEqual(self.product_text,product_exp2)

    @BeautifulReport.add_test_img("testBuyerCenter_003")
    def testBuyerCenter_003(self):
        """测试国际站买家中心收藏的供应商页面"""
        supplier_exp1=self.BL.findElement(OkchemBuyerCenterPage.OkchemBuyerCenterPage.FavoriteSupplier_link)
        self.BL.click(supplier_exp1)
        self.BL.waitContainText(OkchemBuyerCenterPage.OkchemBuyerCenterPage.FavoriteSupplier_exp,self.supplier_text)
        supplier_exp2=self.BL.findElement(OkchemBuyerCenterPage.OkchemBuyerCenterPage.FavoriteSupplier_exp).text
        self.assertEqual(self.supplier_text,supplier_exp2)

    @BeautifulReport.add_test_img("testBuyerCenter_004")
    def testBuyerCenter_004(self):
        """测试国际站买家中心我的询价页面"""
        inquiry_exp=self.BL.findElement(OkchemBuyerCenterPage.OkchemBuyerCenterPage.MyInquiry_link)
        self.BL.click(inquiry_exp)
        inquiry_exp1=self.BL.findElement(OkchemBuyerCenterPage.OkchemBuyerCenterPage.MyInquiry_exp).text
        self.assertEqual(self.myinquiry_text,inquiry_exp1)

    @BeautifulReport.add_test_img("testBuyerCenter_005")
    def testBuyerCenter_005(self):
        """测试国际站买家中心我的消息页面"""
        message_exp=self.BL.findElement(OkchemBuyerCenterPage.OkchemBuyerCenterPage.MyMessage_link)
        self.BL.click(message_exp)
        message_exp1=self.BL.findElement(OkchemBuyerCenterPage.OkchemBuyerCenterPage.MyMessage_exp).text
        self.assertEqual(self.mymessage_text,message_exp1)

    @BeautifulReport.add_test_img("testBuyerCenter_006")
    def testBuyerCenter_006(self):
        """测试国际站买家中心我的采购需求页面"""
        mybuying_exp=self.BL.findElement(OkchemBuyerCenterPage.OkchemBuyerCenterPage.MyBuyingRequest_link)
        self.BL.click(mybuying_exp)
        mybuying_exp1=self.BL.findElement(OkchemBuyerCenterPage.OkchemBuyerCenterPage.MyBuyingRequest_exp).text
        self.assertEqual(self.mybuyingrequest_text,mybuying_exp1)

    @BeautifulReport.add_test_img("testBuyerCenter_007")
    def testBuyerCenter_007(self):
        """测试国际站买家中心我的服务订单页面"""
        mybuying_exp=self.BL.findElement(OkchemBuyerCenterPage.OkchemBuyerCenterPage.MyServiceOrder_link)
        self.BL.click(mybuying_exp)
        mybuying_exp1=self.BL.findElement(OkchemBuyerCenterPage.OkchemBuyerCenterPage.MyServiceOrder_exp).text
        self.assertEqual(self.myserviceorder_text,mybuying_exp1)

    @BeautifulReport.add_test_img("testBuyerCenter_008")
    def testBuyerCenter_008(self):
        """测试国际站买家中心信用贷款服务页面"""
        credit_exp=self.BL.findElement(OkchemBuyerCenterPage.OkchemBuyerCenterPage.MyCreditSeller_link)
        self.BL.click(credit_exp)
        credit_exp1=self.BL.findElement(OkchemBuyerCenterPage.OkchemBuyerCenterPage.MyCreditSeller_exp).text
        self.assertEqual(self.mycredit_text,credit_exp1)

    @BeautifulReport.add_test_img("testBuyerCenter_009")
    def testBuyerCenter_009(self):
        """测试国际站买家中心我的收支页面"""
        myrefer_exp=self.BL.findElement(OkchemBuyerCenterPage.OkchemBuyerCenterPage.MyRefer_link)
        self.BL.click(myrefer_exp)
        myrefer_exp1=self.BL.findElement(OkchemBuyerCenterPage.OkchemBuyerCenterPage.MyRefer_exp).text
        self.assertEqual(self.myrefer_text,myrefer_exp1)

    @BeautifulReport.add_test_img("testBuyerCenter_010")
    def testBuyerCenter_010(self):
        """测试国际站买家中心个人资料页面"""
        myprofile_exp=self.BL.findElement(OkchemBuyerCenterPage.OkchemBuyerCenterPage.EditMyAccount_link)
        self.BL.click(myprofile_exp)
        myprofile_exp1=self.BL.findElement(OkchemBuyerCenterPage.OkchemBuyerCenterPage.MyProfile_link)
        self.BL.click(myprofile_exp1)
        myprofile_exp2=self.BL.findElement(OkchemBuyerCenterPage.OkchemBuyerCenterPage.MyProfile_exp).text
        self.assertEqual(self.myprofile_text,myprofile_exp2)

    @BeautifulReport.add_test_img("testBuyerCenter_011")
    def testBuyerCenter_011(self):
        """测试国际站买家中心个人喜好页面"""
        myprefer_exp1=self.BL.findElement(OkchemBuyerCenterPage.OkchemBuyerCenterPage.MyPreference_link)
        self.BL.click(myprefer_exp1)
        myprefer_exp2=self.BL.findElement(OkchemBuyerCenterPage.OkchemBuyerCenterPage.MyPreference_exp).text
        self.assertEqual(self.myprefer_text,myprefer_exp2)

    @BeautifulReport.add_test_img("testBuyerCenter_012")
    def testBuyerCenter_012(self):
        """测试国际站买家中心修改密码页面"""
        changepw_exp=self.BL.findElement(OkchemBuyerCenterPage.OkchemBuyerCenterPage.ChangePassword_link)
        self.BL.click(changepw_exp)
        changepw_exp1=self.BL.findElement(OkchemBuyerCenterPage.OkchemBuyerCenterPage.ChangePassword_exp).text
        self.assertEqual(self.changepw_text,changepw_exp1)

    @BeautifulReport.add_test_img("testBuyerCenter_013")
    def testBuyerCenter_013(self):
        """测试国际站买家中心退出登录"""
        logout_exp=self.BL.findElement(OkchemBuyerCenterPage.OkchemBuyerCenterPage.Logout_link)
        self.BL.click(logout_exp)
        logout_exp1=self.BL.getTitle(OkchemBuyerCenterPage.OkchemBuyerCenterPage.Logout_exp)
        self.assertEqual(self.logout_text,logout_exp1)

    def tearDown(self):
        global num
        num=num+1
        if num>=10:
            fangfa='testBuyerCenter_0'+str(num)
            xx=getattr(TestOkchemBuyerCenter(),fangfa)
            self.log =xx.__doc__
        elif num<10:
            fangfa='testBuyerCenter_00'+str(num)
            xx = getattr(TestOkchemBuyerCenter(), fangfa)
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
                screenname = screen_path + pattern + 'screenpicture' + now + '.png'
                print(screenname)
                self.BL.getPicture(screenname)  #进行截图处理
                sendEmail = dd.Email() #实例化类
                new_pic = sendEmail.newReport(screen_path) #获取最新的截图
                content1=result.errors[0][-1]
                content=content1.replace('File','<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;File').replace('During','<br/><br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;During')
                sendEmail.email_Text(new_pic,"注意！测试用例执行失败了！！！",self.log,content)  #发送邮件
                self.BL.driver.refresh()

    @classmethod
    def tearDownClass(self):
        self.BL.quit()

    def list2reason(self, exc_list):
        if exc_list and exc_list[-1][0] is self:
            return exc_list[-1][1]


