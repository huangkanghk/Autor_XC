import unittest,time,os,platform,logging,sys,traceback
from Public.common import DoExcel
from Public.pages import OkchemSearchPage
from config import globalconfig
from BeautifulReport import BeautifulReport
from Public.common import send_mail as dd

url=DoExcel.File_Location().get_parameter("PRE地址")
product_sh=DoExcel.File_Location().get_parameter("搜索产品名称",User_Table ="Search")
supplier_sh=DoExcel.File_Location().get_parameter("搜索供应商名称",User_Table ="Search")
new_sh=DoExcel.File_Location().get_parameter("搜索新闻名称",User_Table ="Search")
product_exp=DoExcel.File_Location().get_parameter("匹配的产品",User_Table ="Search")
supplier_exp=DoExcel.File_Location().get_parameter("匹配的供应商",User_Table ="Search")
new_exp=DoExcel.File_Location().get_parameter("匹配的新闻",User_Table ="Search")
num=0

# sys.path.append(os.path.dirname(os.path.abspath(__file__)) + r'\..')
# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
#                     datefmt='%a, %d %b %Y %H:%M:%S',
#                     filename='log_test.log',
#                     filemode='w')
# logger = logging.getLogger()
# logger.level=logging.DEBUG
# logger.addHandler(logging.StreamHandler(sys.stdout))


class TestOkchemSearch(unittest.TestCase):

    def insertStr(self,str_1,a,b):
        # 把字符串转为 list
        str_list = list(str_1)
        # 找到a的位置
        nPos = str_list.index(a)
        # 在斜杠位置之前 插入要插入的字符b
        str_list.insert(nPos,b)
        # 将 list 转为 str
        str_2 = "".join(str_list)
        return str_2
        
    @classmethod
    def setUpClass(self):
        self.url=url
        self.product_sh=product_sh
        self.supplier_sh=supplier_sh
        self.new_sh = new_sh
        self.product_exp=product_exp
        self.supplier_exp=supplier_exp
        self.new_exp=new_exp
        self.BL=OkchemSearchPage.OkchemSearchPage()

    def save_img(self, img_name):
        img_path=globalconfig.picture_path1
        self.BL.driver.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(img_path), img_name))

    @BeautifulReport.add_test_img("testOkchemSearch_001")
    def testOkchemSearch_001(self):
        """测试OKCHEM平台搜索产品"""
        self.BL.Search(self.product_sh,"product")
        a=self.BL.findElement(OkchemSearchPage.OkchemSearchPage.ProductName).text
        self.assertEqual(self.product_exp,a)

    @BeautifulReport.add_test_img("testOkchemSearch_002")
    def testOkchemSearch_002(self):
        """测试OKCHEM平台搜索供应商"""
        self.BL.Search(self.supplier_sh,"suppliers")
        b=self.BL.findElement(OkchemSearchPage.OkchemSearchPage.SupplierName).text
        self.assertEqual(self.supplier_exp,b)

    def tearDown(self):
        global num
        num=num+1
        if num>=10:
            fangfa='testOkchemSearch_0'+str(num)
            xx=getattr(TestOkchemSearch(),fangfa)
            self.log =xx.__doc__
        elif num<10:
            fangfa='testOkchemSearch_00'+str(num)
            xx = getattr(TestOkchemSearch(), fangfa)
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
                sendEmail.email_Text(new_pic,"注意！测试用例执行失败了！！！",self.log,content) #发送邮件
                self.BL.driver.refresh()
        self.BL.driver.back()

    @classmethod
    def tearDownClass(self):
        self.BL.driver.quit()

    def list2reason(self, exc_list):
        if exc_list and exc_list[-1][0] is self:
            return exc_list[-1][1]


