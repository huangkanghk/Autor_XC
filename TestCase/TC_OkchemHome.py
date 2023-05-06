import unittest,time,os,platform
from Public.common import TestCaseInfo,DoExcel,CommonConfig as cc
from Public.pages import OkchemHomePage
from time import sleep
from config import globalconfig
from BeautifulReport import BeautifulReport
from Public.common import send_mail as dd
import traceback
import logging,sys

product_dir=DoExcel.File_Location().get_parameter("产品目录",User_Table ="Home")
buying_request=DoExcel.File_Location().get_parameter("采购需求",User_Table ="Home")
chembnb=DoExcel.File_Location().get_parameter("集采",User_Table ="Home")
sourcing=DoExcel.File_Location().get_parameter("寻源",User_Table ="Home")
factory=DoExcel.File_Location().get_parameter("验厂",User_Table ="Home")
sample=DoExcel.File_Location().get_parameter("样品",User_Table ="Home")
inspect=DoExcel.File_Location().get_parameter("监装",User_Table ="Home")
creditseller=DoExcel.File_Location().get_parameter("卖家贷款",User_Table ="Home")
payment=DoExcel.File_Location().get_parameter("金融支付",User_Table ="Home")
buyerguide=DoExcel.File_Location().get_parameter("买家向导",User_Table ="Home")
OverseasOffices=DoExcel.File_Location().get_parameter("海外驻点",User_Table ="Home")
Globalexport=DoExcel.File_Location().get_parameter("出口全球",User_Table ="Home")
increase_sales=DoExcel.File_Location().get_parameter("提高销售额",User_Table ="Home")
local_buyer=DoExcel.File_Location().get_parameter("本地买家",User_Table ="Home")
seller_guide=DoExcel.File_Location().get_parameter("卖家向导",User_Table ="Home")
trade_show=DoExcel.File_Location().get_parameter("贸易展示",User_Table ="Home")
news=DoExcel.File_Location().get_parameter("新闻",User_Table ="Home")
es_lanage=DoExcel.File_Location().get_parameter("西语",User_Table ="Home")
pt_lanage=DoExcel.File_Location().get_parameter("葡萄牙语",User_Table ="Home")
ru_lanage=DoExcel.File_Location().get_parameter("俄语",User_Table ="Home")
product_cate_home=DoExcel.File_Location().get_parameter("首页产品分类",User_Table ="Home")
productDetail_exp=DoExcel.File_Location().get_parameter("产品详情",User_Table ="Home")
join_us=DoExcel.File_Location().get_parameter("加入我们",User_Table ="Home")
product_footer=DoExcel.File_Location().get_parameter("产品目录footer",User_Table ="Home")
about_okchem=DoExcel.File_Location().get_parameter("关于OKCHEM",User_Table ="Home")
contact_us=DoExcel.File_Location().get_parameter("联系我们",User_Table ="Home")
china_site=DoExcel.File_Location().get_parameter("中国站",User_Table ="Home")
partner_more=DoExcel.File_Location().get_parameter("更多合作伙伴",User_Table ="Home")
supplierDetail=DoExcel.File_Location().get_parameter("首页供应商",User_Table ="Home")
showroom_title=DoExcel.File_Location().get_parameter("showroom",User_Table ="Home")
casno_title=DoExcel.File_Location().get_parameter("CasNo",User_Table ="Home")
findsupplier_ele=DoExcel.File_Location().get_parameter("查找供应商",User_Table ="Home")
num=0

class TestOkchemHome(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.product_dir=product_dir
        self.buying_request = buying_request
        self.chembnb = chembnb
        self.sourcing = sourcing
        self.factory = factory
        self.sample = sample
        self.inspect = inspect
        self.creditseller = creditseller
        self.payment = payment
        self.buyerguide = buyerguide
        self.OverseasOffices = OverseasOffices
        self.Globalexport = Globalexport
        self.increase_sales = increase_sales
        self.local_buyer = local_buyer
        self.seller_guide = seller_guide
        self.trade_show = trade_show
        self.news = news
        self.es_lanage = es_lanage
        self.pt_lanage = pt_lanage
        self.ru_lanage = ru_lanage
        self.product_cate_home = product_cate_home
        self.join_us = join_us
        self.product_footer = product_footer
        self.about_okchem = about_okchem
        self.contact_us = contact_us
        self.china_site = china_site
        self.partner_more = partner_more
        self.supplierDetail=supplierDetail
        self.showroom_title=showroom_title
        self.casno_title=casno_title
        self.findsupplier_ele=findsupplier_ele
        self.BL=OkchemHomePage.OkchemHomePage()
        self.BL.LoginOkchemHome()
        self.BL.driver.delete_all_cookies()

    def save_img(self, img_name):
        img_path=globalconfig.picture_path1
        self.BL.driver.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(img_path), img_name))

    @BeautifulReport.add_test_img("testOkchemHome_001")
    def testOkchemHome_001(self):
        """测试国际站首页进入产品目录界面"""
        self.BL.MousePause(OkchemHomePage.OkchemHomePage.ForBuyer_link)
        ele=self.BL.findElement(OkchemHomePage.OkchemHomePage.ProductDictory)
        self.BL.click(ele)
        actul=self.BL.getTitle(OkchemHomePage.OkchemHomePage.ProductDictory_exp)
        self.assertEqual(self.product_dir,actul)

    @BeautifulReport.add_test_img("testOkchemHome_002")
    def testOkchemHome_002(self):
        """测试国际站首页进入提交采购需求界面"""
        #self.BL.MousePause(OkchemHomePage.OkchemHomePage.ForBuyer_link)
        ele=self.BL.findElement(OkchemHomePage.OkchemHomePage.ForBuyer_link)
        self.BL.click(ele)
        ele=self.BL.findElement(OkchemHomePage.OkchemHomePage.PostBuyingRequest)
        self.BL.click(ele)
        actul=self.BL.getTitle(OkchemHomePage.OkchemHomePage.PostBuyingRequest_exp)
        self.assertIn(self.buying_request,actul)

    @BeautifulReport.add_test_img("testOkchemHome_003")
    def testOkchemHome_003(self):
        """测试国际站首页进入集采平台"""
        #self.BL.MousePause(OkchemHomePage.OkchemHomePage.ForBuyer_link)
        ele=self.BL.findElement(OkchemHomePage.OkchemHomePage.ForBuyer_link)
        self.BL.click(ele)
        allhandes = self.BL.driver.window_handles
        ele=self.BL.findElement(OkchemHomePage.OkchemHomePage.GroupBuying)
        self.BL.click(ele)
        self.BL.waitWindow(allhandes)
        self.BL.switchHandle(-1)
        actul=self.BL.getTitle(OkchemHomePage.OkchemHomePage.GroupBuying_exp)
        self.assertEqual(self.chembnb,actul)

    @BeautifulReport.add_test_img("testOkchemHome_004")
    def testOkchemHome_004(self):
        """测试国际站首页进入trade services页面"""
        #self.BL.MousePause(OkchemHomePage.OkchemHomePage.ForBuyer_link)
        ele=self.BL.findElement(OkchemHomePage.OkchemHomePage.ForBuyer_link)
        self.BL.click(ele)
        ele=self.BL.findElement(OkchemHomePage.OkchemHomePage.TradeServices)
        self.BL.click(ele)
        actul=self.BL.getTitle(OkchemHomePage.OkchemHomePage.TradeServices_exp)
        self.assertIn(self.buying_request,actul)

    @BeautifulReport.add_test_img("testOkchemHome_005")
    def testOkchemHome_005(self):
        """测试国际站首页进入sourcing页面"""
        #self.BL.MousePause(OkchemHomePage.OkchemHomePage.ForBuyer_link)
        ele=self.BL.findElement(OkchemHomePage.OkchemHomePage.ForBuyer_link)
        self.BL.click(ele)
        ele=self.BL.findElement(OkchemHomePage.OkchemHomePage.Sourcing)
        self.BL.click(ele)
        actul=self.BL.getTitle(OkchemHomePage.OkchemHomePage.Sourcing_exp)
        self.assertEqual(self.sourcing,actul)

    @BeautifulReport.add_test_img("testOkchemHome_006")
    def testOkchemHome_006(self):
        """测试国际站首页进入factory audit页面"""
        #self.BL.MousePause(OkchemHomePage.OkchemHomePage.ForBuyer_link)
        ele=self.BL.findElement(OkchemHomePage.OkchemHomePage.ForBuyer_link)
        self.BL.click(ele)
        ele=self.BL.findElement(OkchemHomePage.OkchemHomePage.FactoryAudit)
        self.BL.click(ele)
        actul=self.BL.getTitle(OkchemHomePage.OkchemHomePage.FactoryAudit_exp)
        self.assertEqual(self.factory,actul)

    @BeautifulReport.add_test_img("testOkchemHome_007")
    def testOkchemHome_007(self):
        """测试国际站首页进入sample collection页面"""
        #self.BL.MousePause(OkchemHomePage.OkchemHomePage.ForBuyer_link)
        ele=self.BL.findElement(OkchemHomePage.OkchemHomePage.ForBuyer_link)
        self.BL.click(ele)
        ele=self.BL.findElement(OkchemHomePage.OkchemHomePage.SampleCollection)
        self.BL.click(ele)
        actul=self.BL.getTitle(OkchemHomePage.OkchemHomePage.SampleCollection_exp)
        self.assertEqual(self.sample,actul)

    @BeautifulReport.add_test_img("testOkchemHome_008")
    def testOkchemHome_008(self):
        """测试国际站首页进入insection页面"""
        #self.BL.MousePause(OkchemHomePage.OkchemHomePage.ForBuyer_link)
        ele=self.BL.findElement(OkchemHomePage.OkchemHomePage.ForBuyer_link)
        self.BL.click(ele)
        ele=self.BL.findElement(OkchemHomePage.OkchemHomePage.InspectionService)
        self.BL.click(ele)
        actul=self.BL.getTitle(OkchemHomePage.OkchemHomePage.InspectionService_exp)
        self.assertEqual(self.inspect,actul)

    @BeautifulReport.add_test_img("testOkchemHome_009")
    def testOkchemHome_009(self):
        """测试国际站首页进入credit seller页面"""
        #self.BL.MousePause(OkchemHomePage.OkchemHomePage.ForBuyer_link)
        ele=self.BL.findElement(OkchemHomePage.OkchemHomePage.ForBuyer_link)
        self.BL.click(ele)
        ele=self.BL.findElement(OkchemHomePage.OkchemHomePage.CreditSeller)
        self.BL.click(ele)
        actul=self.BL.getTitle(OkchemHomePage.OkchemHomePage.CreditSeller_exp)
        self.assertEqual(self.creditseller,actul)

    @BeautifulReport.add_test_img("testOkchemHome_010")
    def testOkchemHome_010(self):
        """测试国际站首页进入payment solution页面"""
        #self.BL.MousePause(OkchemHomePage.OkchemHomePage.ForBuyer_link)
        ele=self.BL.findElement(OkchemHomePage.OkchemHomePage.ForBuyer_link)
        self.BL.click(ele)
        ele=self.BL.findElement(OkchemHomePage.OkchemHomePage.PaymentSolution)
        self.BL.click(ele)
        actul=self.BL.getTitle(OkchemHomePage.OkchemHomePage.PaymentSolution_exp)
        self.assertEqual(self.payment,actul)

    @BeautifulReport.add_test_img("testOkchemHome_011")
    def testOkchemHome_011(self):
        """测试国际站首页进入买家向导页面"""
        #self.BL.MousePause(OkchemHomePage.OkchemHomePage.ForBuyer_link)
        ele=self.BL.findElement(OkchemHomePage.OkchemHomePage.ForBuyer_link)
        self.BL.click(ele)
        ele=self.BL.findElement(OkchemHomePage.OkchemHomePage.BuyerGuide)
        self.BL.click(ele)
        actul=self.BL.getTitle(OkchemHomePage.OkchemHomePage.BuyerGuide_exp)
        self.assertEqual(self.buyerguide,actul)

    @BeautifulReport.add_test_img("testOkchemHome_012")
    def testOkchemHome_012(self):
        """测试国际站首页进入从买家服务进入海外驻点页面"""
        #self.BL.MousePause(OkchemHomePage.OkchemHomePage.ForBuyer_link)
        ele=self.BL.findElement(OkchemHomePage.OkchemHomePage.ForBuyer_link)
        self.BL.click(ele)
        allhandes = self.BL.driver.window_handles
        ele=self.BL.findElement(OkchemHomePage.OkchemHomePage.OverseasOffices)
        self.BL.click(ele)
        self.BL.waitWindow(allhandes)
        self.BL.switchHandle(-1)
        actul=self.BL.getTitle(OkchemHomePage.OkchemHomePage.OverseasOffices_exp)
        self.assertIn(self.OverseasOffices,actul)

    @BeautifulReport.add_test_img("testOkchemHome_013")
    def testOkchemHome_013(self):
        """测试国际站首页进入出口全球页面"""
        #self.BL.MousePause(OkchemHomePage.OkchemHomePage.ForSeller_link)
        ele=self.BL.findElement(OkchemHomePage.OkchemHomePage.ForSeller_link)
        self.BL.click(ele)
        allhandes = self.BL.driver.window_handles
        ele=self.BL.findElement(OkchemHomePage.OkchemHomePage.GlobalExports)
        self.BL.click(ele)
        self.BL.waitWindow(allhandes)
        self.BL.switchHandle(-1)
        actul=self.BL.getTitle(OkchemHomePage.OkchemHomePage.GlobalExports_expo)
        self.assertIn(self.Globalexport,actul)

    @BeautifulReport.add_test_img("testOkchemHome_014")
    def testOkchemHome_014(self):
        """测试国际站首页进入increase sales页面"""
        #self.BL.MousePause(OkchemHomePage.OkchemHomePage.ForSeller_link)
        ele=self.BL.findElement(OkchemHomePage.OkchemHomePage.ForSeller_link)
        self.BL.click(ele)
        ele=self.BL.findElement(OkchemHomePage.OkchemHomePage.IncreaseSales)
        self.BL.click(ele)
        actul=self.BL.getTitle(OkchemHomePage.OkchemHomePage.IncreaseSales_exp)
        self.assertEqual(self.increase_sales,actul)

    @BeautifulReport.add_test_img("testOkchemHome_015")
    def testOkchemHome_015(self):
        """测试国际站首页进入Search Buyerlead页面"""
        #self.BL.MousePause(OkchemHomePage.OkchemHomePage.ForSeller_link)
        ele=self.BL.findElement(OkchemHomePage.OkchemHomePage.ForSeller_link)
        self.BL.click(ele)
        ele=self.BL.findElement(OkchemHomePage.OkchemHomePage.SearchBuyLead)
        self.BL.click(ele)
        actul=self.BL.getTitle(OkchemHomePage.OkchemHomePage.SearchBuyLead_exp)
        self.assertIn(self.buying_request,actul)

    @BeautifulReport.add_test_img("testOkchemHome_016")
    def testOkchemHome_016(self):
        """测试国际站首页进入寻找潜在买家页面"""
        #self.BL.MousePause(OkchemHomePage.OkchemHomePage.ForSeller_link)
        ele=self.BL.findElement(OkchemHomePage.OkchemHomePage.ForSeller_link)
        self.BL.click(ele)
        ele=self.BL.findElement(OkchemHomePage.OkchemHomePage.FindPotentialBuyers)
        self.BL.click(ele)
        actul=self.BL.getTitle(OkchemHomePage.OkchemHomePage.FindPotentialBuyers_exp)
        self.assertIn(self.buying_request,actul)

    @BeautifulReport.add_test_img("testOkchemHome_017")
    def testOkchemHome_017(self):
        """测试国际站首页进入本地目标客户页面"""
        #self.BL.MousePause(OkchemHomePage.OkchemHomePage.ForSeller_link)
        ele=self.BL.findElement(OkchemHomePage.OkchemHomePage.ForSeller_link)
        self.BL.click(ele)
        ele=self.BL.findElement(OkchemHomePage.OkchemHomePage.LocateTargetBuyers)
        self.BL.click(ele)
        actul=self.BL.getTitle(OkchemHomePage.OkchemHomePage.LocateTargetBuyers_exp)
        self.assertEqual(self.local_buyer,actul)

    @BeautifulReport.add_test_img("testOkchemHome_018")
    def testOkchemHome_018(self):
        """测试国际站首页进入卖家向导页面"""
        #self.BL.MousePause(OkchemHomePage.OkchemHomePage.ForSeller_link)
        ele=self.BL.findElement(OkchemHomePage.OkchemHomePage.ForSeller_link)
        self.BL.click(ele)
        ele=self.BL.findElement(OkchemHomePage.OkchemHomePage.SupplierGuide)
        self.BL.click(ele)
        actul=self.BL.getTitle(OkchemHomePage.OkchemHomePage.SupplierGuide_exp)
        self.assertEqual(self.seller_guide,actul)

    @BeautifulReport.add_test_img("testOkchemHome_019")
    def testOkchemHome_019(self):
        """测试国际站首页从卖家服务进入海外驻点页面"""
        #self.BL.MousePause(OkchemHomePage.OkchemHomePage.ForSeller_link)
        ele=self.BL.findElement(OkchemHomePage.OkchemHomePage.ForSeller_link)
        self.BL.click(ele)
        allhandes = self.BL.driver.window_handles
        ele=self.BL.findElement(OkchemHomePage.OkchemHomePage.OverseaOffices_Seller)
        self.BL.click(ele)
        self.BL.waitWindow(allhandes)
        self.BL.switchHandle(-1)
        actul=self.BL.getTitle(OkchemHomePage.OkchemHomePage.OverseasOffices_exp)
        self.assertIn(self.OverseasOffices,actul)

    @BeautifulReport.add_test_img("testOkchemHome_020")
    def testOkchemHome_020(self):
        """测试国际站首页进入trade shows页面"""
        ele=self.BL.findElement(OkchemHomePage.OkchemHomePage.TradeShows)
        self.BL.click(ele)
        actul=self.BL.getTitle(OkchemHomePage.OkchemHomePage.TradeShows_exp)
        self.assertEqual(self.trade_show,actul)

    @BeautifulReport.add_test_img("testOkchemHome_021")
    def testOkchemHome_021(self):
        """测试国际站首页进入news页面"""
        ele=self.BL.findElement(OkchemHomePage.OkchemHomePage.IndustryNews)
        self.BL.click(ele)
        actul=self.BL.getTitle(OkchemHomePage.OkchemHomePage.IndustryNews_exp)
        self.assertEqual(self.news,actul)

    @BeautifulReport.add_test_img("testOkchemHome_022")
    def testOkchemHome_022(self):
        """测试国际站首页首页点击任意产品分类"""
        self.BL.MousePause(OkchemHomePage.OkchemHomePage.all_category)
        self.BL.MousePause(OkchemHomePage.OkchemHomePage.first_category)
        ele=self.BL.findElement(OkchemHomePage.OkchemHomePage.sub_category)
        self.BL.click(ele)
        actul=self.BL.getTitle(OkchemHomePage.OkchemHomePage.sub_category_exp)
        self.assertEqual(self.product_cate_home,actul)

    @BeautifulReport.add_test_img("testOkchemHome_023")
    def testOkchemHome_023(self):
        """测试国际站首页进入Post Buying Request页面"""
        ele=self.BL.findElement(OkchemHomePage.OkchemHomePage.PostBuyingRequest_sum)
        self.BL.click(ele)
        actul=self.BL.getTitle(OkchemHomePage.OkchemHomePage.PostBuyingRequest_sum_exp)
        self.assertIn(self.buying_request,actul)

    @BeautifulReport.add_test_img("testOkchemHome_024")
    def testOkchemHome_024(self):
        """测试国际站首页点击你也喜欢下的第一个产品图片"""
        sleep(5)
        self.BL.scrollTo(OkchemHomePage.OkchemHomePage.LikeProduct_img)
        allhandes = self.BL.driver.window_handles
        ele=self.BL.findElement(OkchemHomePage.OkchemHomePage.LikeProduct_img)
        self.BL.click(ele)
        self.BL.waitWindow(allhandes)
        self.BL.switchHandle(1)
        actul=self.BL.getText(OkchemHomePage.OkchemHomePage.LikeProduct_img_exp)
        self.assertEqual(productDetail_exp,actul)

    @BeautifulReport.add_test_img("testOkchemHome_025")
    def testOkchemHome_025(self):
        """测试国际站首页点击Latest Buying Requests右侧more按钮"""
        self.BL.scrollTo(OkchemHomePage.OkchemHomePage.LatestBuyingRequest)
        ele=self.BL.findElement(OkchemHomePage.OkchemHomePage.LatestBuyingRequest)
        self.BL.click(ele)
        actul=self.BL.getTitle(OkchemHomePage.OkchemHomePage.LatestBuyingRequest_exp)
        self.assertIn(self.buying_request,actul)

    @BeautifulReport.add_test_img("testOkchemHome_026")
    def testOkchemHome_026(self):
        """测试国际站首页点击join now按钮"""
        self.BL.scrollTo(OkchemHomePage.OkchemHomePage.JoinNow)
        ele=self.BL.findElement(OkchemHomePage.OkchemHomePage.JoinNow)
        self.BL.click(ele)
        actul=self.BL.getTitle(OkchemHomePage.OkchemHomePage.JoinNow_exp)
        self.assertEqual(self.join_us,actul)

    @BeautifulReport.add_test_img("testOkchemHome_027")
    def testOkchemHome_027(self):
        """测试国际站首页点击集采右侧more按钮"""
        self.BL.scrollTo(OkchemHomePage.OkchemHomePage.Chembnb_more)
        allhandes = self.BL.driver.window_handles
        ele=self.BL.findElement(OkchemHomePage.OkchemHomePage.Chembnb_more)
        self.BL.click(ele)
        self.BL.waitWindow(allhandes)
        self.BL.switchHandle(1)
        actul=self.BL.getTitle(OkchemHomePage.OkchemHomePage.GroupBuying_exp)
        self.assertEqual(self.chembnb,actul)

    @BeautifulReport.add_test_img("testOkchemHome_028")
    def testOkchemHome_028(self):
        """测试国际站首页点击第一个集采下的图片"""
        self.BL.scrollTo(OkchemHomePage.OkchemHomePage.Chembnb_img)
        allhandes = self.BL.driver.window_handles
        ele=self.BL.findElement(OkchemHomePage.OkchemHomePage.Chembnb_img)
        self.BL.click(ele)
        self.BL.waitWindow(allhandes)
        self.BL.switchHandle(1)
        actul=self.BL.getText(OkchemHomePage.OkchemHomePage.Chembnb_img_exp)
        self.assertEqual("Group Buying",actul)

    @BeautifulReport.add_test_img("testOkchemHome_029")
    def testOkchemHome_029(self):
        """测试国际站首页点击Trade show右侧more按钮"""
        self.BL.scrollTo(OkchemHomePage.OkchemHomePage.TradeShows_more)
        allhandes = self.BL.driver.window_handles
        ele=self.BL.findElement(OkchemHomePage.OkchemHomePage.TradeShows_more)
        self.BL.click(ele)
        self.BL.waitWindow(allhandes)
        self.BL.switchHandle(1)
        actul=self.BL.getTitle(OkchemHomePage.OkchemHomePage.TradeShows_exp)
        self.assertEqual(self.trade_show,actul)

    @BeautifulReport.add_test_img("testOkchemHome_030")
    def testOkchemHome_030(self):
        """测试国际站首页点击Trade show下的第一个展会图片"""
        self.BL.scrollTo(OkchemHomePage.OkchemHomePage.TradeShows_more)
        allhandes = self.BL.driver.window_handles
        ele = self.BL.findElement(OkchemHomePage.OkchemHomePage.TradeShows_more)
        self.BL.click(ele)
        self.BL.waitWindow(allhandes)
        self.BL.switchHandle(1)
        self.BL.scrollTo(OkchemHomePage.OkchemHomePage.TradeShows_img)
        allhandes = self.BL.driver.window_handles
        ele = self.BL.findElement(OkchemHomePage.OkchemHomePage.TradeShows_img)
        self.BL.click(ele)
        self.BL.waitWindow(allhandes)
        self.BL.switchHandle(1)
        actul=self.BL.getText(OkchemHomePage.OkchemHomePage.TradeShows_exp)
        self.assertEqual("Trade Shows",actul)

    @BeautifulReport.add_test_img("testOkchemHome_031")
    def testOkchemHome_031(self):
        """测试国际站首页点击news右侧more按钮"""
        self.BL.scrollTo(OkchemHomePage.OkchemHomePage.NewsMore)
        allhandes = self.BL.driver.window_handles
        ele=self.BL.findElement(OkchemHomePage.OkchemHomePage.NewsMore)
        self.BL.click(ele)
        self.BL.waitWindow(allhandes)
        self.BL.switchHandle(1)
        actul=self.BL.getTitle(OkchemHomePage.OkchemHomePage.IndustryNews_exp)
        self.assertEqual(self.news,actul)

    @BeautifulReport.add_test_img("testOkchemHome_032")
    def testOkchemHome_032(self):
        """测试国际站首页点击第一个news下的新闻图片"""
        self.BL.scrollTo(OkchemHomePage.OkchemHomePage.News_img)
        allhandes = self.BL.driver.window_handles
        ele=self.BL.findElement(OkchemHomePage.OkchemHomePage.News_img)
        self.BL.click(ele)
        self.BL.waitWindow(allhandes)
        self.BL.switchHandle(1)
        actul=self.BL.getText(OkchemHomePage.OkchemHomePage.News_img_exp)
        self.assertEqual("Industry News",actul)

    @BeautifulReport.add_test_img("testOkchemHome_033")
    def testOkchemHome_033(self):
        """测试国际站首页点击底部product directory"""
        self.BL.scrollTo(OkchemHomePage.OkchemHomePage.ProductDirectory_footer)
        ele=self.BL.findElement(OkchemHomePage.OkchemHomePage.ProductDirectory_footer)
        self.BL.click(ele)
        actul=self.BL.getTitle(OkchemHomePage.OkchemHomePage.ProductDictory_exp)
        self.assertEqual(self.product_footer,actul)

    @BeautifulReport.add_test_img("testOkchemHome_034")
    def testOkchemHome_034(self):
        """测试国际站首页点击底部post buying request"""
        self.BL.scrollTo(OkchemHomePage.OkchemHomePage.PostBuyingRequest_footer)
        ele=self.BL.findElement(OkchemHomePage.OkchemHomePage.PostBuyingRequest_footer)
        self.BL.click(ele)
        actul=self.BL.getTitle(OkchemHomePage.OkchemHomePage.PostBuyingRequest_exp)
        self.assertIn(self.buying_request,actul)

    @BeautifulReport.add_test_img("testOkchemHome_035")
    def testOkchemHome_035(self):
        """测试国际站首页点击底部group buying"""
        self.BL.scrollTo(OkchemHomePage.OkchemHomePage.GroupBuying_footer)
        allhandes = self.BL.driver.window_handles
        ele=self.BL.findElement(OkchemHomePage.OkchemHomePage.GroupBuying_footer)
        self.BL.click(ele)
        self.BL.waitWindow(allhandes)
        self.BL.switchHandle(1)
        actul=self.BL.getTitle(OkchemHomePage.OkchemHomePage.GroupBuying_exp)
        self.assertIn(self.chembnb,actul)

    @BeautifulReport.add_test_img("testOkchemHome_036")
    def testOkchemHome_036(self):
        """测试国际站首页点击底部trade services"""
        self.BL.scrollTo(OkchemHomePage.OkchemHomePage.TradeServices_footer)
        ele=self.BL.findElement(OkchemHomePage.OkchemHomePage.TradeServices_footer)
        self.BL.click(ele)
        actul=self.BL.getTitle(OkchemHomePage.OkchemHomePage.TradeServices_exp)
        self.assertIn(self.buying_request,actul)

    @BeautifulReport.add_test_img("testOkchemHome_037")
    def testOkchemHome_037(self):
        """测试国际站首页点击底部买家向导"""
        self.BL.scrollTo(OkchemHomePage.OkchemHomePage.BuyerGuide_footer)
        ele=self.BL.findElement(OkchemHomePage.OkchemHomePage.BuyerGuide_footer)
        self.BL.click(ele)
        actul=self.BL.getTitle(OkchemHomePage.OkchemHomePage.BuyerGuide_exp)
        self.assertEqual(self.buyerguide,actul)

    @BeautifulReport.add_test_img("testOkchemHome_038")
    def testOkchemHome_038(self):
        """测试国际站首页点击底部出口全球"""
        self.BL.scrollTo(OkchemHomePage.OkchemHomePage.GlobalExports_footer)
        allhandes = self.BL.driver.window_handles
        ele=self.BL.findElement(OkchemHomePage.OkchemHomePage.GlobalExports_footer)
        self.BL.click(ele)
        self.BL.waitWindow(allhandes)
        self.BL.switchHandle(-1)
        actul=self.BL.getTitle(OkchemHomePage.OkchemHomePage.GlobalExports_expo)
        self.assertIn(self.Globalexport,actul)

    @BeautifulReport.add_test_img("testOkchemHome_039")
    def testOkchemHome_039(self):
        """测试国际站首页点击底部increase sales"""
        self.BL.scrollTo(OkchemHomePage.OkchemHomePage.IncreaseSales_footer)
        ele=self.BL.findElement(OkchemHomePage.OkchemHomePage.IncreaseSales_footer)
        self.BL.click(ele)
        actul=self.BL.getTitle(OkchemHomePage.OkchemHomePage.IncreaseSales_exp)
        self.assertEqual(self.increase_sales,actul)

    @BeautifulReport.add_test_img("testOkchemHome_040")
    def testOkchemHome_040(self):
        """测试国际站首页点击底部search buylead"""
        self.BL.scrollTo(OkchemHomePage.OkchemHomePage.SearchBuylead_footer)
        ele=self.BL.findElement(OkchemHomePage.OkchemHomePage.SearchBuylead_footer)
        self.BL.click(ele)
        actul=self.BL.getTitle(OkchemHomePage.OkchemHomePage.SearchBuyLead_exp)
        self.assertIn(self.buying_request,actul)

    @BeautifulReport.add_test_img("testOkchemHome_041")
    def testOkchemHome_041(self):
        """测试国际站首页点击底部find potential buyer"""
        self.BL.scrollTo(OkchemHomePage.OkchemHomePage.FindPotentialBuyers_footer)
        ele=self.BL.findElement(OkchemHomePage.OkchemHomePage.FindPotentialBuyers_footer)
        self.BL.click(ele)
        actul=self.BL.getTitle(OkchemHomePage.OkchemHomePage.FindPotentialBuyers_exp)
        self.assertIn(self.buying_request,actul)

    @BeautifulReport.add_test_img("testOkchemHome_042")
    def testOkchemHome_042(self):
        """测试国际站首页点击底部locate target buyers"""
        self.BL.scrollTo(OkchemHomePage.OkchemHomePage.LocateTargetBuyers_footer)
        ele=self.BL.findElement(OkchemHomePage.OkchemHomePage.LocateTargetBuyers_footer)
        self.BL.click(ele)
        actul=self.BL.getTitle(OkchemHomePage.OkchemHomePage.LocateTargetBuyers_exp)
        self.assertEqual(self.local_buyer,actul)

    @BeautifulReport.add_test_img("testOkchemHome_043")
    def testOkchemHome_043(self):
        """测试国际站首页点击底部卖家向导"""
        self.BL.scrollTo(OkchemHomePage.OkchemHomePage.SupplierGuide_footer)
        ele=self.BL.findElement(OkchemHomePage.OkchemHomePage.SupplierGuide_footer)
        self.BL.click(ele)
        actul=self.BL.getTitle(OkchemHomePage.OkchemHomePage.SupplierGuide_exp)
        self.assertEqual(self.seller_guide,actul)

    @BeautifulReport.add_test_img("testOkchemHome_044")
    def testOkchemHome_044(self):
        """测试国际站首页点击底部about OKCHEM"""
        self.BL.scrollTo(OkchemHomePage.OkchemHomePage.AboutOkchem_footer)
        ele=self.BL.findElement(OkchemHomePage.OkchemHomePage.AboutOkchem_footer)
        self.BL.click(ele)
        actul=self.BL.getTitle(OkchemHomePage.OkchemHomePage.SupplierGuide_exp)
        self.assertEqual(self.about_okchem,actul)

    @BeautifulReport.add_test_img("testOkchemHome_045")
    def testOkchemHome_045(self):
        """测试国际站首页点击底部Contact us"""
        self.BL.scrollTo(OkchemHomePage.OkchemHomePage.ContactUs_footer)
        ele=self.BL.findElement(OkchemHomePage.OkchemHomePage.ContactUs_footer)
        self.BL.click(ele)
        actul=self.BL.getTitle(OkchemHomePage.OkchemHomePage.SupplierGuide_exp)
        self.assertEqual(self.contact_us,actul)

    @BeautifulReport.add_test_img("testOkchemHome_046")
    def testOkchemHome_046(self):
        """测试国际站首页点击底部中国站"""
        self.BL.scrollTo(OkchemHomePage.OkchemHomePage.Chinasite_footer)
        allhandes = self.BL.driver.window_handles
        ele=self.BL.findElement(OkchemHomePage.OkchemHomePage.Chinasite_footer)
        self.BL.click(ele)
        self.BL.waitWindow(allhandes)
        self.BL.switchHandle(-1)
        actul=self.BL.getTitle(OkchemHomePage.OkchemHomePage.Chinasite_footer_exp)
        self.assertIn(self.china_site,actul)

    @BeautifulReport.add_test_img("testOkchemHome_047")
    def testOkchemHome_047(self):
        """测试国际站首页点击底部Overseas Offices"""
        self.BL.scrollTo(OkchemHomePage.OkchemHomePage.OverseasOffices_footer)
        allhandes = self.BL.driver.window_handles
        ele=self.BL.findElement(OkchemHomePage.OkchemHomePage.OverseasOffices_footer)
        self.BL.click(ele)
        self.BL.waitWindow(allhandes)
        self.BL.switchHandle(-1)
        actul=self.BL.getTitle(OkchemHomePage.OkchemHomePage.OverseasOffices_exp)
        self.assertIn(self.OverseasOffices,actul)

    @BeautifulReport.add_test_img("testOkchemHome_048")
    def testOkchemHome_048(self):
        """测试国际站首页点击底部合作伙伴下方more按钮"""
        self.BL.scrollTo(OkchemHomePage.OkchemHomePage.ContactUs_footer)
        ele=self.BL.findElement(OkchemHomePage.OkchemHomePage.OurPartnerMore_footer)
        self.BL.click(ele)
        actul=self.BL.getTitle(OkchemHomePage.OkchemHomePage.OurPartnerMore_footer_more)
        self.assertEqual(self.partner_more,actul)

    @BeautifulReport.add_test_img("testOkchemHome_049")
    def testOkchemHome_049(self):
        """测试国际站首页点击设置的供应商图片"""
        self.BL.scrollTo(OkchemHomePage.OkchemHomePage.SupplierHome)
        allhandes=self.BL.driver.window_handles
        ele=self.BL.findElement(OkchemHomePage.OkchemHomePage.SupplierHome)
        self.BL.driver.execute_script("arguments[0].click();", ele)
        #self.BL.click(ele)
        self.BL.waitWindow(allhandes)
        self.BL.switchHandle(1)
        self.BL.waitTitle("Chemical")
        actul =self.BL.driver.title
        self.assertIn(self.supplierDetail,actul)

    @BeautifulReport.add_test_img("testOkchemHome_050")
    def testOkchemHome_050(self):
        """测试国际站首页底部点击a进入showroom"""
        self.BL.scrollTo(OkchemHomePage.OkchemHomePage.showroom_a)
        ele=self.BL.findElement(OkchemHomePage.OkchemHomePage.showroom_a)
        self.BL.click(ele)
        actul=self.BL.getTitle(OkchemHomePage.OkchemHomePage.showroom_detail)
        self.assertIn(self.showroom_title,actul)

    @BeautifulReport.add_test_img("testOkchemHome_051")
    def testOkchemHome_051(self):
        """测试国际站首页底部点击b进入showroom"""
        self.BL.scrollTo(OkchemHomePage.OkchemHomePage.showroom_b)
        ele=self.BL.findElement(OkchemHomePage.OkchemHomePage.showroom_b)
        self.BL.click(ele)
        actul=self.BL.getTitle(OkchemHomePage.OkchemHomePage.showroom_detail)
        self.assertIn(self.showroom_title,actul)

    @BeautifulReport.add_test_img("testOkchemHome_052")
    def testOkchemHome_052(self):
        """测试国际站首页底部点击c进入showroom"""
        self.BL.scrollTo(OkchemHomePage.OkchemHomePage.showroom_c)
        ele=self.BL.findElement(OkchemHomePage.OkchemHomePage.showroom_c)
        self.BL.click(ele)
        actul=self.BL.getTitle(OkchemHomePage.OkchemHomePage.showroom_detail)
        self.assertIn(self.showroom_title,actul)

    @BeautifulReport.add_test_img("testOkchemHome_053")
    def testOkchemHome_053(self):
        """测试国际站首页底部点击0-9进入showroom"""
        self.BL.scrollTo(OkchemHomePage.OkchemHomePage.showroom_num)
        ele=self.BL.findElement(OkchemHomePage.OkchemHomePage.showroom_num)
        self.BL.click(ele)
        actul=self.BL.getTitle(OkchemHomePage.OkchemHomePage.showroom_detail)
        self.assertIn(self.showroom_title,actul)

    @BeautifulReport.add_test_img("testOkchemHome_054")
    def testOkchemHome_054(self):
        """测试国际站首页底部点击Source Products By Cas No右侧数字1"""
        self.BL.scrollTo(OkchemHomePage.OkchemHomePage.casno_1)
        ele=self.BL.findElement(OkchemHomePage.OkchemHomePage.casno_1)
        self.BL.click(ele)
        actul=self.BL.getTitle(OkchemHomePage.OkchemHomePage.casno_detail)
        self.assertIn(self.casno_title,actul)

    @BeautifulReport.add_test_img("testOkchemHome_055")
    def testOkchemHome_055(self):
        """测试国际站首页点击底部India Pavilion"""
        self.BL.scrollTo(OkchemHomePage.OkchemHomePage.OverseasOffices_footer)
        allhandes = self.BL.driver.window_handles
        ele=self.BL.findElement(OkchemHomePage.OkchemHomePage.india)
        self.BL.click(ele)
        self.BL.waitWindow(allhandes)
        self.BL.switchHandle(-1)
        actul=self.BL.getTitle(OkchemHomePage.OkchemHomePage.india_exp)
        self.assertIn('India Pavilion',actul)

    @BeautifulReport.add_test_img("testOkchemHome_056")
    def testOkchemHome_056(self):
        """测试国际站首页底部点击find suppliers"""
        ele=self.BL.findElement(OkchemHomePage.OkchemHomePage.findsupplier_footer)
        self.BL.click(ele)
        actul=self.BL.getText(OkchemHomePage.OkchemHomePage.findsupplier_exp)
        self.assertEqual(self.findsupplier_ele,actul)

    @BeautifulReport.add_test_img("testOkchemHome_057")
    def testOkchemHome_057(self):
        """测试国际站首页for buyer下点击find suppliers"""
        self.BL.scrollTo(OkchemHomePage.OkchemHomePage.ForBuyer_link)
        self.BL.MousePause(OkchemHomePage.OkchemHomePage.ForBuyer_link)
        ele=self.BL.findElement(OkchemHomePage.OkchemHomePage.findsupplier_footer)
        self.BL.click(ele)
        actul=self.BL.getText(OkchemHomePage.OkchemHomePage.findsupplier_exp)
        self.assertEqual(self.findsupplier_ele,actul)

    @BeautifulReport.add_test_img("testOkchemHome_058")
    def testOkchemHome_058(self):
        """测试国际站首页切换到西语"""
        self.BL.scrollTo(OkchemHomePage.OkchemHomePage.Lanage)
        self.BL.MousePause(OkchemHomePage.OkchemHomePage.Lanage)
        ele = self.BL.findElement(OkchemHomePage.OkchemHomePage.Lange_es)
        self.BL.click(ele)
        self.BL.waitTitle(self.es_lanage)
        actul = self.BL.getTitle(OkchemHomePage.OkchemHomePage.Lange_es_exp)
        self.assertEqual(self.es_lanage, actul)
        # sleep(5)
        # url = self.BL.driver.current_url
        # if "es" in url:
        #     actul = self.BL.getTitle(OkchemHomePage.OkchemHomePage.Lange_es_exp)
        #     self.assertEqual(self.es_lanage, actul)
        # else:
        #     sleep(5)
        #     actul = self.BL.getTitle(OkchemHomePage.OkchemHomePage.Lange_es_exp)
        #     self.assertEqual(self.es_lanage, actul)

    @BeautifulReport.add_test_img("testOkchemHome_059")
    def testOkchemHome_059(self):
        """测试国际站首页切换到葡萄牙语"""
        ele = self.BL.findElement(OkchemHomePage.OkchemHomePage.Lanage)
        self.BL.click(ele)
        ele = self.BL.findElement(OkchemHomePage.OkchemHomePage.Lange_pt)
        self.BL.click(ele)
        self.BL.waitTitle(self.pt_lanage)
        actul = self.BL.getTitle(OkchemHomePage.OkchemHomePage.Lange_es_exp)
        self.assertEqual(self.pt_lanage, actul)

    @BeautifulReport.add_test_img("testOkchemHome_060")
    def testOkchemHome_060(self):
        """测试国际站首页切换到俄语"""
        ele = self.BL.findElement(OkchemHomePage.OkchemHomePage.Lanage)
        self.BL.click(ele)
        ele = self.BL.findElement(OkchemHomePage.OkchemHomePage.Lange_ru)
        self.BL.click(ele)
        self.BL.waitTitle(self.ru_lanage)
        actul = self.BL.getTitle(OkchemHomePage.OkchemHomePage.Lange_es_exp)
        self.assertEqual(self.ru_lanage, actul)
        # url = self.BL.driver.current_url
        # if "ru" in url:
        #     actul = self.BL.getTitle(OkchemHomePage.OkchemHomePage.Lange_es_exp)
        #     self.assertEqual(self.ru_lanage, actul)
        # else:
        #     sleep(5)
        #     actul = self.BL.getTitle(OkchemHomePage.OkchemHomePage.Lange_es_exp)
        #     self.assertEqual(self.ru_lanage, actul)

    @classmethod
    def tearDownClass(self):
        self.BL.driver.quit()

    # def tearDown(self):
    #     #self.BL.driver.delete_all_cookies()
    #     list=self.BL.getAllHandles()
    #     #listInfo = ["500", "502", "404", "Site Maintenance"]
    #     if len(list)>1:
    #         self.BL.driver.close()
    #         self.BL.switchHandle(0)
    #     else:
    #         self.BL.driver.back()

    def tearDown(self):
        global num
        num=num+1
        if num>=10:
            fangfa='testOkchemHome_0'+str(num)
            xx=getattr(TestOkchemHome(),fangfa)
            self.log =xx.__doc__
        elif num<10:
            fangfa='testOkchemHome_00'+str(num)
            xx = getattr(TestOkchemHome(), fangfa)
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
        print(len(list))
        if len(list)==2:
            self.BL.driver.close()
            self.BL.switchHandle(0)
        elif len(list)==3:
            self.BL.driver.close()
            self.BL.switchHandle(1)
            self.BL.driver.close()
            self.BL.switchHandle(0)
        else:
            self.BL.driver.back()

    def list2reason(self, exc_list):
        if exc_list and exc_list[-1][0] is self:
            return exc_list[-1][1]
