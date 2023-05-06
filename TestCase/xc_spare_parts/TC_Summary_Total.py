from builtins import str

import platform
from time import sleep
from run import *
from Public.common import send_mail as dd
import xc_common
import psycopg2,requests,json
import math

num =0

class TestSummaryTotal(unittest.TestCase):

    def setUp(self):
        BL = xc_common.WindowsBL

    @BeautifulReport.add_test_img("testSumaryTotal_001")
    def testSumaryTotal_001(self):
        """ 【汇总看板】 页面数据校验（条件：PO单与存量） """
        # 获取页面数据 #
        params = {"params": {"model": "summary.kanban", "limit": 9999999}}
        response = requests.get(xc_common.url + "/web/dataset/search_read", headers=xc_common.headers,
                                data=json.dumps(params))
        response = response.text
        response = json.loads(response)
        result = response["result"]
        sum_records = result["records"]

        # 获取BOM总表页面数据 #
        params = {"params": {"model": "bom.total.table", "limit": 9999999}}
        response = requests.get(xc_common.url + "/web/dataset/search_read", headers=xc_common.headers,
                                data=json.dumps(params))
        response = response.text
        response = json.loads(response)
        result = response["result"]
        records = result["records"]

        # 获取备料总表数据 #
        pre_params = {"params": {"model": "prepare.materials", "limit": 9999999}}
        pre_response = requests.get(xc_common.url + "/web/dataset/search_read", headers=xc_common.headers,
                                data=json.dumps(pre_params))
        pre_response = pre_response.text
        pre_response = json.loads(pre_response)
        pre_result = pre_response["result"]
        pre_records = pre_result["records"]

        # 获取替代料备料总表数据 #
        rep_params = {"params": {"model": "alternative.prepare.materials", "limit": 9999999}}
        rep_response = requests.get(xc_common.url + "/web/dataset/search_read", headers=xc_common.headers,
                                data=json.dumps(rep_params))
        rep_response = rep_response.text
        rep_response = json.loads(rep_response)
        rep_result = rep_response["result"]
        rep_records = rep_result["records"]

        new_records = []
        for record in records:
            information_sources = record["information_sources"]
            proj_name = record["proj_name"]
            stock_location = record["stock_location"]
            if stock_location == "武汉":
                stock_location = "武汉项目"
            server_aging = record["server_aging"]
            server_desc = record["server_desc"]
            if "介质保留" in server_desc:
                server_desc = "是"
            else:
                server_desc = "否"
            material_mode = record["material_mode"]
            bind_material_code = ""
            material_name = ""
            sum_count = 0
            for record_temp in records:
                if record["information_sources"] == record_temp["information_sources"] and record["proj_name"] == record_temp["proj_name"] and record["stock_location"] == record_temp["stock_location"] and record["server_aging"] == record_temp["server_aging"] and record["material_mode"] == record_temp["material_mode"] :
                    record_server_desc = record["server_desc"]
                    temp__server_desc = record_temp["server_desc"]
                    if "介质保留" in record_server_desc:
                        record_server_desc = "是"
                    else:
                        record_server_desc = "否"
                    if "介质保留" in temp__server_desc:
                        temp__server_desc = "是"
                    else:
                        temp__server_desc = "否"
                    if record_server_desc ==  temp__server_desc:
                        sum_count = sum_count + record_temp["sum_count"]
            bhl = ''
            kcl = ''
            qk = ''
            wuhankc = ''
            zqk = ''
            kt02 = 0
            kt16 = 0
            kt17 = 0
            cgsl = 0
            ccsl = 0
            rmasl = 0

            for pre_record in pre_records:
                if material_mode == pre_record["material_code"] and stock_location == pre_record["city"]:
                    bind_material_code=  pre_record["bundling_number"]
                    if bind_material_code != "":
                        break
                    material_name = pre_record["name"]
                    bhl = pre_record["bhl"]
                    kcl = pre_record["kcl"]
                    qk = pre_record["qk"]
                    wuhankc = pre_record["wuhankc"]
                    zqk = pre_record["zqk"]
                    kt02 = pre_record["kt02"]
                    kt16 = pre_record["kt16"]
                    kt17 = pre_record["kt17"]
                    cgsl = pre_record["cgsl"]
                    ccsl = pre_record["ccsl"]
                    rmasl = pre_record["rmasl"]

            for rep_record in rep_records:
                if bind_material_code == rep_record["bundling_number"] and stock_location == rep_record["city"]:
                    material_name = rep_record["name"]
                    bhl = rep_record["bhl"]
                    kcl = rep_record["stock_quantity"]
                    qk = rep_record["quantity"]
                    wuhankc = rep_record["wuhan_stock_quantity"]
                    zqk = rep_record["sum_each_gap"]
                    kt02 = rep_record["kt02_quantity"]
                    kt16 = rep_record["kt16_quantity"]
                    kt17 = rep_record["kt17_quantity"]
                    cgsl = rep_record["purchase_in_transit"]
                    ccsl = rep_record["purchase_in_transit"]
                    rmasl = rep_record["rma_in_transit"]

            print(123)



    def tearDown(self):
        global num
        num=num+1
        if num>=10:
            fangfa='testSummaryTotal_0'+str(num)
            xx=getattr(TestSummaryTotal(),fangfa)
            self.log =xx.__doc__
        elif num<10:
            fangfa='testSummaryTotal_00'+str(num)
            xx = getattr(TestSummaryTotal(), fangfa)
            self.log= xx.__doc__
        result = self.defaultTestResult()
        self._feedErrorsToResult(result, self._outcome.errors)
        error = self.list2reason(result.errors)
        failure = self.list2reason(result.failures)

    def list2reason(self, exc_list):
        if exc_list and exc_list[-1][0] is self:
            return exc_list[-1][1]

