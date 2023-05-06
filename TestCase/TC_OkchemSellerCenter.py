import unittest,time,os,platform
from Public.common import TestCaseInfo,DoExcel,CommonConfig as cc
from Public.pages import OkchemSellerCenterPage
from time import sleep
from BeautifulReport import BeautifulReport
from config import globalconfig
from Public.common import send_mail as dd

url=DoExcel.File_Location().get_parameter("PRE地址")
seller_un=DoExcel.File_Location().get_parameter("OKCHEM卖家账号")
seller_pw=DoExcel.File_Location().get_parameter("OKCHEM卖家密码")

store_setting=DoExcel.File_Location().get_parameter("店铺设置",User_Table="SellerCenter")
store_langage=DoExcel.File_Location().get_parameter("店铺多语言",User_Table="SellerCenter")
store_picture=DoExcel.File_Location().get_parameter("店铺图片",User_Table="SellerCenter")
release_product=DoExcel.File_Location().get_parameter("发布新产品",User_Table="SellerCenter")
product_list=DoExcel.File_Location().get_parameter("产品列表",User_Table="SellerCenter")
productShowcase_set=DoExcel.File_Location().get_parameter("橱窗产品设置",User_Table="SellerCenter")
quoteforinquiry=DoExcel.File_Location().get_parameter("询盘报价",User_Table="SellerCenter")
quoteforbuying=DoExcel.File_Location().get_parameter("采购需求报价",User_Table="SellerCenter")
my_message=DoExcel.File_Location().get_parameter("我的消息",User_Table="SellerCenter")
change_profile=DoExcel.File_Location().get_parameter("信息修改",User_Table="SellerCenter")
change_password=DoExcel.File_Location().get_parameter("密码修改",User_Table="SellerCenter")
subaccount_manage=DoExcel.File_Location().get_parameter("子账号管理",User_Table="SellerCenter")
logout=DoExcel.File_Location().get_parameter("注销",User_Table="SellerCenter")
myservice_order=DoExcel.File_Location().get_parameter("我的服务订单",User_Table="SellerCenter")
mymembership=DoExcel.File_Location().get_parameter("我的会员权益",User_Table="SellerCenter")
myreport_order=DoExcel.File_Location().get_parameter("我的报告订单",User_Table="SellerCenter")
num=0

class TestOkchemSellerCenter(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        num=0
        self.url=url
        self.seller_un=seller_un
        self.seller_pw=seller_pw
        self.store_setting=store_setting
        self.store_langage=store_langage
        self.store_picture=store_picture
        self.release_product=release_product
        self.product_list=product_list
        self.productShowcase_set=productShowcase_set
        self.quoteforinquiry=quoteforinquiry
        self.quoteforbuying=quoteforbuying
        self.my_message=my_message
        self.myservice_order=myservice_order
        self.mymembership=mymembership
        self.myreport_order=myreport_order
        self.change_profile = change_profile
        self.change_password = change_password
        self.subaccount_manage= subaccount_manage
        self.logout = logout
        self.BL=OkchemSellerCenterPage.OkchemSellerCenterPage()
        self.BL.LoginSellerCenter(self.seller_un,self.seller_pw)
        self.BL.findElement(OkchemSellerCenterPage.OkchemSellerCenterPage.Lanage_text)
        self.lanage_seller=self.BL.getText(OkchemSellerCenterPage.OkchemSellerCenterPage.Lanage_text)
        if self.lanage_seller=="简体中文":
            ele=self.BL.findElement(OkchemSellerCenterPage.OkchemSellerCenterPage.Lanage_text)
            self.BL.MousePause(OkchemSellerCenterPage.OkchemSellerCenterPage.Lanage_text)
            ele=self.BL.findElement(OkchemSellerCenterPage.OkchemSellerCenterPage.Lanage_en)
            self.BL.click(ele)
            self.BL.waitContainText(OkchemSellerCenterPage.OkchemSellerCenterPage.Lanage_text,"English")

    def save_img(self, img_name):
        img_path=globalconfig.picture_path1
        self.BL.driver.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(img_path), img_name))

    @BeautifulReport.add_test_img("testOkchemSellerCenter_001")
    def testOkchemSellerCenter_001(self):
        """测试国际站卖家中心店铺管理-店铺设置"""
        self.BL.MouseClick(OkchemSellerCenterPage.OkchemSellerCenterPage.Store_Manage)
        self.BL.waitText(OkchemSellerCenterPage.OkchemSellerCenterPage.Store_Setting)
        allhandes=self.BL.driver.window_handles
        storeSet=self.BL.findElement(OkchemSellerCenterPage.OkchemSellerCenterPage.Store_Setting)
        self.BL.click(storeSet)
        self.BL.waitWindow(allhandes)
        self.BL.switchHandle(-1)
        home_exp=self.BL.findElement(OkchemSellerCenterPage.OkchemSellerCenterPage.Store_Setting_exp).text
        self.assertIn(self.store_setting,home_exp)

    @BeautifulReport.add_test_img("testOkchemSellerCenter_002")
    def testOkchemSellerCenter_002(self):
        """测试国际站卖家中心店铺管理-店铺多语言"""
        store_mulanage=self.BL.findElement(OkchemSellerCenterPage.OkchemSellerCenterPage.Store_MuliLanage)
        self.BL.click(store_mulanage)
        self.BL.waitContainText(OkchemSellerCenterPage.OkchemSellerCenterPage.Store_MuliLanage_exp,self.store_langage)
        store_mulanage_exp=self.BL.findElement(OkchemSellerCenterPage.OkchemSellerCenterPage.Store_MuliLanage_exp).text
        self.assertIn(self.store_langage,store_mulanage_exp)

    @BeautifulReport.add_test_img("testOkchemSellerCenter_003")
    def testOkchemSellerCenter_003(self):
        """测试国际站卖家中心产品管理-发布新产品"""
        productManage=self.BL.findElement(OkchemSellerCenterPage.OkchemSellerCenterPage.Product_Manage)
        self.BL.click(productManage)
        self.BL.waitText(OkchemSellerCenterPage.OkchemSellerCenterPage.Release_Product)
        allhandles=self.BL.driver.window_handles
        release_product= self.BL.findElement(OkchemSellerCenterPage.OkchemSellerCenterPage.Release_Product)
        self.BL.click(release_product)
        self.BL.waitWindow(allhandles)
        self.BL.switchHandle(-1)
        release_product_exp=self.BL.findElement(OkchemSellerCenterPage.OkchemSellerCenterPage.Release_Product_exp).text
        self.assertIn(self.release_product,release_product_exp)

    @BeautifulReport.add_test_img("testOkchemSellerCenter_004")
    def testOkchemSellerCenter_004(self):
        """测试国际站卖家中心产品管理-产品列表"""
        productlist=self.BL.findElement(OkchemSellerCenterPage.OkchemSellerCenterPage.Product_List)
        self.BL.click(productlist)
        self.BL.waitContainText(OkchemSellerCenterPage.OkchemSellerCenterPage.Product_List_exp,self.product_list)
        productlist_exp=self.BL.findElement(OkchemSellerCenterPage.OkchemSellerCenterPage.Product_List_exp).text
        self.assertIn(self.product_list,productlist_exp)

    @BeautifulReport.add_test_img("testOkchemSellerCenter_005")
    def testOkchemSellerCenter_005(self):
        """测试国际站卖家中心产品管理-橱窗产品设置"""
        ShowcaseProduct_set = self.BL.findElement(OkchemSellerCenterPage.OkchemSellerCenterPage.Product_Setting)
        self.BL.click(ShowcaseProduct_set)
        self.BL.waitContainText(OkchemSellerCenterPage.OkchemSellerCenterPage.Product_Setting_exp,self.productShowcase_set)
        ShowcaseProduct_set_exp=self.BL.findElement(OkchemSellerCenterPage.OkchemSellerCenterPage.Product_Setting_exp).text
        self.assertIn(self.productShowcase_set,ShowcaseProduct_set_exp)

    @BeautifulReport.add_test_img("testOkchemSellerCenter_006")
    def testOkchemSellerCenter_006(self):
        """测试国际站卖家中心报价管理-询盘报价"""
        quteManage=self.BL.findElement(OkchemSellerCenterPage.OkchemSellerCenterPage.Quote_Manage)
        self.BL.click(quteManage)
        self.BL.waitText(OkchemSellerCenterPage.OkchemSellerCenterPage.Inquiry_Quote)
        inquiryQuote=self.BL.findElement(OkchemSellerCenterPage.OkchemSellerCenterPage.Inquiry_Quote)
        self.BL.click(inquiryQuote)
        self.BL.waitContainText(OkchemSellerCenterPage.OkchemSellerCenterPage.Inquiry_Quote_exp,self.quoteforinquiry)
        inquiryQuote_exp=self.BL.getText(OkchemSellerCenterPage.OkchemSellerCenterPage.Inquiry_Quote_exp)
        self.assertIn(self.quoteforinquiry,inquiryQuote_exp)

    @BeautifulReport.add_test_img("testOkchemSellerCenter_007")
    def testOkchemSellerCenter_007(self):
        """测试国际站卖家中心报价管理-采购需求报价"""
        buyingRequestQuote=self.BL.findElement(OkchemSellerCenterPage.OkchemSellerCenterPage.PostBuyingRequest_Quote)
        self.BL.click(buyingRequestQuote)
        self.BL.waitContainText(OkchemSellerCenterPage.OkchemSellerCenterPage.PostBuyingRequest_Quote_exp,self.quoteforbuying)
        buyingRequestQuote_exp=self.BL.getText(OkchemSellerCenterPage.OkchemSellerCenterPage.PostBuyingRequest_Quote_exp)
        self.assertIn(self.quoteforbuying,buyingRequestQuote_exp)

    @BeautifulReport.add_test_img("testOkchemSellerCenter_008")
    def testOkchemSellerCenter_008(self):
        """测试国际站卖家中心消息管理-我的消息"""
        messageManage=self.BL.findElement(OkchemSellerCenterPage.OkchemSellerCenterPage.Message_Manage)
        self.BL.click(messageManage)
        self.BL.waitText(OkchemSellerCenterPage.OkchemSellerCenterPage.My_Message)
        myMessage=self.BL.findElement(OkchemSellerCenterPage.OkchemSellerCenterPage.My_Message)
        self.BL.click(myMessage)
        self.BL.waitContainText(OkchemSellerCenterPage.OkchemSellerCenterPage.My_Message_exp,self.my_message)
        myMessage_exp=self.BL.getText(OkchemSellerCenterPage.OkchemSellerCenterPage.My_Message_exp)
        self.assertIn(self.my_message,myMessage_exp)

    @BeautifulReport.add_test_img("testOkchemSellerCenter_009")
    def testOkchemSellerCenter_009(self):
        """测试国际站卖家中心-服务管理-我的服务订单"""
        serviceManage=self.BL.findElement(OkchemSellerCenterPage.OkchemSellerCenterPage.Service_Manage)
        self.BL.click(serviceManage)
        self.BL.waitText(OkchemSellerCenterPage.OkchemSellerCenterPage.MyService_Order)
        myServiceorder=self.BL.findElement(OkchemSellerCenterPage.OkchemSellerCenterPage.MyService_Order)
        self.BL.click(myServiceorder)
        self.BL.waitContainText(OkchemSellerCenterPage.OkchemSellerCenterPage.MyService_Order_exp,self.myservice_order)
        myServiceorder_exp=self.BL.getText(OkchemSellerCenterPage.OkchemSellerCenterPage.MyService_Order_exp)
        self.assertIn(self.myservice_order,myServiceorder_exp)

    @BeautifulReport.add_test_img("testOkchemSellerCenter_010")
    def testOkchemSellerCenter_010(self):
        """测试国际站卖家中心-服务管理-我的会员权益"""
        allhandles=self.BL.driver.window_handles
        myMembership=self.BL.findElement(OkchemSellerCenterPage.OkchemSellerCenterPage.MyMembership)
        self.BL.click(myMembership)
        self.BL.waitWindow(allhandles)
        self.BL.switchHandle(-1)
        self.BL.waitContainText(OkchemSellerCenterPage.OkchemSellerCenterPage.MyMembership_exp,self.mymembership)
        mymembership_exp=self.BL.getText(OkchemSellerCenterPage.OkchemSellerCenterPage.MyMembership_exp)
        self.assertIn(self.mymembership,mymembership_exp)

    @BeautifulReport.add_test_img("testOkchemSellerCenter_011")
    def testOkchemSellerCenter_011(self):
        """测试国际站卖家中心-报告管理-我的报告订单"""
        reportManage=self.BL.findElement(OkchemSellerCenterPage.OkchemSellerCenterPage.Report_Manage)
        self.BL.click(reportManage)
        self.BL.waitText(OkchemSellerCenterPage.OkchemSellerCenterPage.MyReport_Order)
        myReportorder=self.BL.findElement(OkchemSellerCenterPage.OkchemSellerCenterPage.MyReport_Order)
        self.BL.click(myReportorder)
        self.BL.waitContainText(OkchemSellerCenterPage.OkchemSellerCenterPage.MyReport_Order_exp,self.myreport_order)
        myServiceorder_exp=self.BL.getText(OkchemSellerCenterPage.OkchemSellerCenterPage.MyReport_Order_exp)
        self.assertIn(self.myreport_order,myServiceorder_exp)

    @BeautifulReport.add_test_img("testOkchemSellerCenter_012")
    def testOkchemSellerCenter_012(self):
        """测试国际站卖家中心-头像-信息修改"""
        self.BL.MousePause(OkchemSellerCenterPage.OkchemSellerCenterPage.Header_Icon)
        allhandles=self.BL.driver.window_handles
        changeProfile=self.BL.findElement(OkchemSellerCenterPage.OkchemSellerCenterPage.Profile_Change)
        self.BL.click(changeProfile)
        self.BL.waitWindow(allhandles)
        self.BL.switchHandle(-1)
        changeProfile_exp=self.BL.getText(OkchemSellerCenterPage.OkchemSellerCenterPage.Profile_Change_exp)
        self.assertIn(self.change_profile,changeProfile_exp)

    @BeautifulReport.add_test_img("testOkchemSellerCenter_013")
    def testOkchemSellerCenter_013(self):
        """测试国际站卖家中心-头像-密码修改"""
        self.BL.MousePause(OkchemSellerCenterPage.OkchemSellerCenterPage.Header_Icon)
        allhandles = self.BL.driver.window_handles
        passwdChanage=self.BL.findElement(OkchemSellerCenterPage.OkchemSellerCenterPage.Password_Change)
        self.BL.click(passwdChanage)
        self.BL.waitWindow(allhandles)
        self.BL.switchHandle(-1)
        passwdChanage_exp=self.BL.getText(OkchemSellerCenterPage.OkchemSellerCenterPage.Password_Change_exp)
        self.assertIn(self.change_password,passwdChanage_exp)

    @BeautifulReport.add_test_img("testOkchemSellerCenter_014")
    def testOkchemSellerCenter_014(self):
        """测试国际站卖家中心-头像-子账号管理"""
        self.BL.MousePause(OkchemSellerCenterPage.OkchemSellerCenterPage.Header_Icon)
        allhandles = self.BL.driver.window_handles
        subaccountManage=self.BL.findElement(OkchemSellerCenterPage.OkchemSellerCenterPage.Subaccount_Manage)
        self.BL.click(subaccountManage)
        self.BL.waitWindow(allhandles)
        self.BL.switchHandle(-1)
        submymessage_exp=self.BL.getText(OkchemSellerCenterPage.OkchemSellerCenterPage.Subaccount_Manage_exp)
        self.assertIn(self.subaccount_manage,submymessage_exp)

    @BeautifulReport.add_test_img("testOkchemSellerCenter_015")
    def testOkchemSellerCenter_015(self):
        """测试国际站卖家中心-头像-注销"""
        self.BL.MousePause(OkchemSellerCenterPage.OkchemSellerCenterPage.Header_Icon)
        logout=self.BL.findElement(OkchemSellerCenterPage.OkchemSellerCenterPage.Logout)
        self.BL.click(logout)
        logout_exp=self.BL.getTitle(OkchemSellerCenterPage.OkchemSellerCenterPage.Logout_exp)
        self.assertIn(self.logout,logout_exp)

    @classmethod
    def tearDownClass(self):
        self.BL.quit()

    def tearDown(self):
        global num
        num=num+1
        if num>=10:
            fangfa='testOkchemSellerCenter_0'+str(num)
            xx=getattr(TestOkchemSellerCenter(),fangfa)
            self.log =xx.__doc__
        elif num<10:
            fangfa='testOkchemSellerCenter_00'+str(num)
            xx = getattr(TestOkchemSellerCenter(), fangfa)
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
                screenname = screen_path + pattern+ 'screenpicture' + now + '.png'
                print(screenname)
                self.BL.getPicture(screenname)  #进行截图处理
                sendEmail = dd.Email() #实例化类
                new_pic = sendEmail.newReport(screen_path) #获取最新的截图
                content1=result.errors[0][-1]
                content=content1.replace('File','<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;File').replace('During','<br/><br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;During')
                sendEmail.email_Text(new_pic,"注意！测试用例执行失败了！！！",self.log,content)  #发送邮件
                self.BL.driver.refresh()
        # self.BL.driver.delete_all_cookies()
        list = self.BL.getAllHandles()
        if len(list) > 1:
            self.BL.driver.close()
            self.BL.switchHandle(0)
        else:
            pass
            #self.BL.driver.back()

    def list2reason(self, exc_list):
        if exc_list and exc_list[-1][0] is self:
            return exc_list[-1][1]
