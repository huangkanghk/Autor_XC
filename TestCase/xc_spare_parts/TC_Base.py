from builtins import str

import platform
from time import sleep

import cx_Oracle

from run import *
from Public.common import send_mail as dd
import xc_common
import requests,json

num = 0
class TestBase(unittest.TestCase):

    def setUp(self):
        BL = xc_common.WindowsBL

    @BeautifulReport.add_test_img("testBase_001")
    def testBase_001(self):
        """ 【备件测算-鲲鹏日报】 同步数据校验 """
        # 获取页面数据 #
        params = {"params": {"model": "kunpeng.daily","limit": 9999999,"domain":[["stock_category","!=","借用在途库"]]}}
        response = requests.get(xc_common.url + "/web/dataset/search_read", headers=xc_common.headers, data=json.dumps(params))
        response = response.text
        response = json.loads(response)
        result = response["result"]
        table_records = result["records"]
        new_table_Records = []
        for  arritem  in  table_records:
            if arritem["batch_code"] == False:
                arritem["batch_code"] = None
            if arritem["stock_category"] == False:
                arritem["stock_category"] = None
            item = {"service_scope_code": arritem["service_scope_code"],
                    "service_category": arritem["service_category"],
                    "factory_code": arritem["factory_code"],
                    "factory_category": arritem["factory_category"],
                    "material_code": arritem["material_code"],
                    "material_desc": arritem["material_desc"],
                    "material_category_name": arritem["material_category_name"],
                    "material_group_name": arritem["material_group_name"],
                    "stock_address": arritem["stock_address"],
                    "stock_name": arritem["stock_name"],
                    "stock_quantity": arritem["stock_quantity"],
                    "batch_code": arritem["batch_code"],
                    "stock_category": arritem["stock_category"]
            }
            new_table_Records.append(item)

        #获取BI数据#
        conn_str = xc_common.biuser + "/" + xc_common.bipw + "@" + xc_common.bihost + ":" + str(
            xc_common.biport) + "/" + xc_common.bifw
        connection_oracle = cx_Oracle.Connection(conn_str)
        cursor_oracle = connection_oracle.cursor()
        query = f"""SELECT 业务范围代码 ywfwdm,业务类型 ywlx,工厂代码 gcdm,工厂类型 gclx,cast(cast(substr(物料代码,1,12) as NUMBER) as varchar2(3)) || '-' || substr(物料代码,-6) sap_no,物料名称 wlmc, 批次代码 pcdm,物料类型名称  wllxmc,物料组名称 wlzmc, 库存地分类 kcdfl ,库存地代码 kcddm,库存地名称 kcdmc ,实际库存数量 sjkcsl FROM DCDWS.VW_DCN_DIKCMX WHERE ( 库存地分类 is NULL or 库存地分类 not in ('借用在途库')) """
        cursor_oracle.execute(query)
        bi_records = cursor_oracle.fetchall()
        new_birecord = []
        for arritem in bi_records:
            item = {"service_scope_code": arritem[0],
                    "service_category":arritem[1],
                    "factory_code":arritem[2],
                    "factory_category":arritem[3],
                    "material_code":arritem[4],
                    "material_desc":arritem[5],
                    "material_category_name":arritem[7],
                    "material_group_name":arritem[8],
                    "stock_address":arritem[10] ,
                    "stock_name":arritem[11],
                    "stock_quantity":arritem[12],
                    "batch_code": arritem[6] ,
                    "stock_category":arritem[9]
            }
            new_birecord.append(item)

        # 最终数据 VS 页面数据#
        if len(new_table_Records) != len(new_birecord):
            raise  Exception("【备件测算-鲲鹏日报】 同步数据核对异常")
        com_table = sorted(new_table_Records, key=lambda x: [x["service_scope_code"] ,x["service_category"], x["material_code"], x["factory_category"],x["factory_code"],x["batch_code"],x["material_code"],x["stock_address"],x["material_group_name"]])
        com_birecord = sorted(new_birecord, key=lambda x: [x["service_scope_code"] ,x["service_category"], x["material_code"], x["factory_category"],x["factory_code"],x["batch_code"], x["material_code"],x["stock_address"],x["material_group_name"]])
        if com_table !=  com_birecord:
            raise  Exception("【备件测算-鲲鹏日报】 同步数据核对异常")
        print("鲲鹏日报-核对数据结束")

    class ListNode(object):
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    def tearDown(self):
        global num
        num=num+1
        if num>=10:
            fangfa='testBase_0'+str(num)
            xx=getattr(TestBase(),fangfa)
            self.log =xx.__doc__
        elif num<10:
            fangfa='testBase_00'+str(num)
            xx = getattr(TestBase(), fangfa)
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

    def list2reason(self, exc_list):
        if exc_list and exc_list[-1][0] is self:
            return exc_list[-1][1]

