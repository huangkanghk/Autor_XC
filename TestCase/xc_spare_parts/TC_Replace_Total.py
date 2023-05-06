from builtins import str

import platform
from time import sleep
from run import *
from Public.common import send_mail as dd
import xc_common
import psycopg2,requests,json
import math

conn = psycopg2.connect(dbname=xc_common.dbname, user=xc_common.user, password=xc_common.password, host=xc_common.host, port=xc_common.port)
cur = conn.cursor();
num =0

class TestReplaceTotal(unittest.TestCase):

    def setUp(self):
        BL = xc_common.WindowsBL

    def save_img(self, img_name):
        img_path=globalconfig.picture_path1
        self.BL.driver.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(img_path), img_name))
        sleep(2)


    @BeautifulReport.add_test_img("testReplaceTotal_001")
    def testReplaceTotal_001(self):
        """ 【备件测算-替代料备料总表】 页面数据校验（条件：PO单与存量） """
        # 获取页面数据 #
        params = {"params": {"model": "alternative.prepare.materials", "limit": 1000000}}
        response = requests.get(xc_common.url + "/web/dataset/search_read", headers=xc_common.headers,
                                data=json.dumps(params))
        response = response.text
        response = json.loads(response)
        result = response["result"]
        Bom_records = result["records"]

        # 获取备料总表页面数据 #
        params = {"params": {"model": "prepare.materials", "domain": [], "limit": 999999,
                             "context": {"information_sources": ""}}}
        response = requests.get(xc_common.url + "/web/dataset/search_read", headers=xc_common.headers,
                                data=json.dumps(params))
        response = response.text
        response = json.loads(response)
        result = response["result"]
        records = result["records"]
        # 过滤None #
        global new_arr_final
        new_arr_final = []
        for arritem in records:
            for arritem_tab in arritem:
                if arritem[arritem_tab] is None:
                    arritem[arritem_tab] = ''
                    if arritem_tab == "kt02_quantity" or arritem_tab == "kt16_quantity" or arritem_tab == "kt17_quantity":
                        arritem[arritem_tab] = 0
                if isinstance(arritem[arritem_tab], float):
                    if arritem_tab != 'theo_non_rate':
                        arritem[arritem_tab] = int(arritem[arritem_tab])
            new_arr_final.append(arritem)

        new_bales = []
        for  item in new_arr_final:
            if item["bundling_number"] != '':
                sum_count = 0
                sum_reject = 0
                sum_xl = 0
                bhl = ''
                kc = 0
                qk = ''
                whkc = 0
                kcyj = ''
                KT02 = 0
                KT16 =0
                KT17 = 0
                psl = 0
                zcsl = 0
                rmasl = 0
                count = 0
                is_reject = False
                for f_item in new_arr_final:
                    if item["bundling_number"] == f_item["bundling_number"]:
                        count = count + 1
                        sum_count = sum_count + f_item["total_usage"]
                        if f_item["theo_non_rate"] != '':
                            is_reject =True
                            sum_reject = sum_reject + f_item["theo_non_rate"]
                        whkc = whkc + f_item["wuhan_stock_quantity"]
                        KT02 = KT02 + f_item["kt02_quantity"]
                        KT16 = KT16 + f_item["kt16_quantity"]
                        KT17 = KT17 + f_item["kt17_quantity"]
                        psl = psl + f_item["purchase_in_transit"]
                        zcsl = zcsl + f_item["dump_in_transit"]
                        rmasl = rmasl + f_item["rma_in_transit"]
                        if item["city"] == f_item["city"]:
                            sum_xl = sum_xl + f_item["sales"]
                            kc = kc + f_item["stock_quantity"]
                if is_reject == True:
                    sum_reject =round( sum_reject/count,8)
                    temp = sum_xl * sum_reject
                    if temp >= 8:
                        bhl = math.ceil(temp / 4)  # 向上取整#
                    if temp >= 1 and temp < 8:
                        bhl = 2
                    if temp > 0 and temp < 1:
                        bhl = 1
                    if temp == 0:
                        bhl = 0
                    qk = kc - bhl
                    zsl = sum_count
                    x = zsl * sum_reject / 6
                    y = bhl
                    if y >= x:
                        kcyj = 'adequate'
                    elif y >= x / 2 and y < x:
                        kcyj = 'replenished'
                    elif y > 0 and y < x / 2:
                        kcyj = 'urgently_replenished'
                    elif y <= 0:
                        kcyj = 'out_of_stock'
                    else:
                        kcyj = ''
                else:
                    sum_reject = ''
                    bhl = ''
                item_temp = {
                    "bundling_number": item["bundling_number"],
                    "m_name": item["name"],
                    "sum_count": sum_count,
                    "reject": sum_reject,
                    "city": item["city"],
                    "sum_xl": sum_xl,
                    "bhl": bhl,
                    "kc": kc,
                    "qk": qk,
                    "whkc": whkc,
                    "kcyj": kcyj,
                    "sum_qk": '',
                    "final_qk": '',
                    "KT02": KT02,
                    "KT16": KT16,
                    "KT17": KT17,
                    "psl": psl,
                    "zcsl": zcsl,
                    "rmasl": rmasl
                }
                new_bales.append(item)

        for arritem in new_bales:
            is_exit = False
            for itm in Bom_records:
                if arritem["bundling_number"] == itm["bundling_number"] and arritem["m_name"] == itm["name"] and arritem["city"] == itm["city"] and \
                        arritem["psl"] == itm["purchase_in_transit"] and arritem["zcsl"] == itm["dump_in_transit"] and \
                        arritem["rmasl"] == itm["rma_in_transit"] and arritem["KT02"] == itm["kt02_quantity"] and \
                        arritem["KT16"] == itm["kt16_quantity"] and arritem["KT17"] == itm["kt17_quantity"] \
                        and arritem["whkc"] == itm["wuhan_stock_quantity"] and arritem["kc"] == itm["stock_quantity"] \
                        and arritem["qk"] == itm["gap_quantity"] and arritem["reject"] == itm["theo_non_rate"] \
                        and arritem["kcyj"] == itm["stock_alert_status"] and arritem["sum_count"] == itm["total_usage"] \
                        and arritem["sum_xl"] == itm["sales"] and arritem["final_qk"] == itm["final_gap"] \
                        and arritem["sum_qk"] == itm["sum_each_gap"] and arritem["bhl"] == itm["reserve_quantity"]:
                    is_exit = True
                    break
            if is_exit == False:
                print("实际的数据")
                print(arritem)
                raise Exception("备料总表数据核对异常")
        if len(new_bales) != len(Bom_records):
            raise Exception("备料总表数据核对异常")
        print("备料总表-核对数据结束（PO单与存量表）")

    def tearDown(self):
        global num
        num=num+1
        if num>=10:
            fangfa='testReplaceTotal_0'+str(num)
            xx=getattr(TestReplaceTotal(),fangfa)
            self.log =xx.__doc__
        elif num<10:
            fangfa='testPrepareTotal_00'+str(num)
            xx = getattr(TestReplaceTotal(), fangfa)
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
        TestCase = unittest.defaultTestLoader.getTestCaseNames(TestReplaceTotal)
        # if num == len(TestCase):
        #     self.BL.quit()
        # else:
        #     sleep(2)
        #     self.BL.driver.refresh()

    def list2reason(self, exc_list):
        if exc_list and exc_list[-1][0] is self:
            return exc_list[-1][1]

