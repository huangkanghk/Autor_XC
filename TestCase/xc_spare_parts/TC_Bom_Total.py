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
new_arr_final = [] #备料总表数据#

class TestBomTotal(unittest.TestCase):

    def setUp(self):
        BL = xc_common.WindowsBL
        if BL == '':
            raise  Exception("无法获取用户信息")
        else:
            self.BL = BL


    def save_img(self, img_name):
        img_path=globalconfig.picture_path1
        self.BL.driver.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(img_path), img_name))
        sleep(2)


    @BeautifulReport.add_test_img("testBomTotal_001")
    def testBomTotal_001(self):
        """ 【备件测算-BOM总表】 页面数据校验(条件：PO单与存量表) """
        cur.execute(
            "SELECT proj_name,server_desc,server_aging,delivery_location,stock_location,material_mode,material_desc,sum,information_sources, proj_number,sale,remark,to_char(write_date, 'yyyy-mm-dd') from purchase_order_inventory")
        records = cur.fetchall()
        rows = []
        for record in records:
            row  = {"proj_name":record[0],
                    "server_desc":record[1],
                    "server_aging":record[2],
                    "delivery_location":record[3],
                    "stock_location":record[4],
                    "material_mode":record[5],
                    "material_desc":record[6],
                    "sum_count":record[7],
                    "information_sources":record[8],
                    "proj_number":record[9],
                    "sale":record[10],
                    "remark":record[11],
                    "write_time":record[12]}
            for tab in row:
                if row[tab] == None:
                    row[tab] = ""
            rows.append(row)
        no_boms = []
        # 第一 查询是否有BOM 处理BOM#
        no_BOM = False
        while no_BOM == False:
            return_arr = self.tearBom(rows)
            if return_arr[1] == False:
                rows = return_arr[0]
                no_boms = rows
            no_BOM = return_arr[1]

        #第二处理物料转换#
        newarr = []
        for arritem in no_boms:
            repstr = "SELECT sap_69_no,sap_302_no,material_desc from material_transformation where sap_69_no =" + "'" + arritem["material_mode"] + "'"
            cur.execute(repstr)
            rep_record = cur.fetchall()
            if len(rep_record) > 0:
                arritem["material_mode"] = rep_record[0][1]
            newarr.append(arritem)

        # 第三  过滤非电子物料#
        newarrT = []
        for arritem in newarr:
            nostr = "SELECT material_mode from non_electronic_materials where material_mode =" + "'" + arritem["material_mode"] + "'"
            cur.execute(nostr)
            rep_record = cur.fetchall()
            if len(rep_record) > 0:
                continue
            newarrT.append(arritem)

        newarrS = []
        #第四 合计处理后的数据 #
        for arritem in newarrT:
            flag = False
            print(len(newarrS))
            for newitem in newarrS:
                if arritem["proj_name"] == newitem["proj_name"] and arritem["server_desc"] == newitem["server_desc"] and arritem["server_aging"] == newitem["server_aging"] and arritem["delivery_location"] == newitem["delivery_location"] and arritem["material_mode"] == newitem["material_mode"] and arritem["material_desc"] == newitem["material_desc"] and arritem["information_sources"] == newitem["information_sources"]  and arritem["proj_number"] == newitem["proj_number"] and arritem["sale"] == newitem["sale"] and arritem["remark"] == newitem["remark"]and arritem["write_time"] == newitem["write_time"]:
                    flag = True
            if flag:
                continue
            countq = 0
            for itm in newarrT:
                if arritem["proj_name"] == itm["proj_name"] and arritem["server_desc"] == itm["server_desc"] and arritem["server_aging"] == itm["server_aging"] and arritem["delivery_location"] == itm["delivery_location"] and arritem["material_mode"] == itm["material_mode"] and arritem["material_desc"] == itm["material_desc"] and arritem["information_sources"] == itm["information_sources"]  and arritem["proj_number"] == itm["proj_number"] and arritem["sale"] == itm["sale"] and arritem["remark"] == itm["remark"]and arritem["write_time"] == itm["write_time"]:
                   countq = countq + itm["sum_count"]
            arritem["sum_count"] = countq
            newarrS.append(arritem)

        # 获取页面数据 #
        params = {"params": {"model": "bom.total.table","limit": 1000000}}
        response = requests.get(xc_common.url + "/web/dataset/search_read", headers=xc_common.headers, data=json.dumps(params))
        response = response.text
        response = json.loads(response)
        result = response["result"]
        records = result["records"]

        # 过滤None #
        new_arr_final = []
        for arritem in newarrS:
            for arritem_tab in arritem:
                if arritem[arritem_tab] is None:
                    arritem[arritem_tab] = ''
            new_arr_final.append(arritem)

        # 最终数据 VS 页面数据#
        for arritem in new_arr_final:
           is_exit = False
           for itm in records:
               if arritem["proj_name"] == itm["proj_name"] and arritem["server_desc"] == itm["server_desc"] and arritem["server_aging"] == itm["server_aging"] \
                       and arritem["delivery_location"] == itm["delivery_location"] and arritem["stock_location"] == itm["stock_location"] and arritem["material_mode"] == itm["material_mode"] \
                       and arritem["material_desc"] == itm["material_desc"] and arritem["sum_count"] == itm["sum_count"] and arritem["information_sources"] == itm["information_sources"] \
                       and arritem["proj_number"] == itm["proj_number"] and arritem["sale"] == itm["sale"] and arritem["remark"] == itm["remark"]  and arritem["write_time"] == itm["write_time"]:
                   is_exit = True
           if is_exit == False:
               print("实际的数据")
               print(arritem)
               print("页面的所有的数据")
               print(records)
               raise Exception(arritem[0]+"数据异常")
        print("BOM总表（PO单与存量）-核对数据结束")

    @BeautifulReport.add_test_img("testBomTotal_002")
    def testBomTotal_002(self):
        """ 【备件测算-BOM总表】 页面数据校验(条件：存量表) """
        cur.execute(
            "SELECT proj_name,server_desc,server_aging,delivery_location,stock_location,material_mode,material_desc,sum,information_sources, proj_number,sale,remark,to_char(write_date, 'yyyy-mm-dd') from purchase_order_inventory where information_sources ='存量表' ")
        records = cur.fetchall()
        rows = []
        for record in records:
            row = {"proj_name": record[0],
                   "server_desc": record[1],
                   "server_aging": record[2],
                   "delivery_location": record[3],
                   "stock_location": record[4],
                   "material_mode": record[5],
                   "material_desc": record[6],
                   "sum_count": record[7],
                   "information_sources": record[8],
                   "proj_number": record[9],
                   "sale": record[10],
                   "remark": record[11],
                   "write_time": record[12]}
            for tab in row:
                if row[tab] == None:
                    row[tab] = ""
            rows.append(row)
        no_boms = []
        # 第一 查询是否有BOM 处理BOM#
        no_BOM = False
        while no_BOM == False:
            return_arr = self.tearBom(rows)
            if return_arr[1] == False:
                rows = return_arr[0]
                no_boms = rows
            no_BOM = return_arr[1]

        # 第二处理物料转换#
        newarr = []
        for arritem in no_boms:
            repstr = "SELECT sap_69_no,sap_302_no,material_desc from material_transformation where sap_69_no =" + "'" + \
                     arritem["material_mode"] + "'"
            cur.execute(repstr)
            rep_record = cur.fetchall()
            if len(rep_record) > 0:
                arritem["material_mode"] = rep_record[0][1]
            newarr.append(arritem)

        # 第三  过滤非电子物料#
        newarrT = []
        for arritem in newarr:
            nostr = "SELECT material_mode from non_electronic_materials where material_mode =" + "'" + arritem[
                "material_mode"] + "'"
            cur.execute(nostr)
            rep_record = cur.fetchall()
            if len(rep_record) > 0:
                continue
            newarrT.append(arritem)

        newarrS = []
        # 第四 合计处理后的数据 #
        for arritem in newarrT:
            flag = False
            print(len(newarrS))
            for newitem in newarrS:
                if arritem["proj_name"] == newitem["proj_name"] and arritem["server_desc"] == newitem["server_desc"] and \
                        arritem["server_aging"] == newitem["server_aging"] and arritem["delivery_location"] == newitem[
                    "delivery_location"] and arritem["material_mode"] == newitem["material_mode"] and arritem[
                    "material_desc"] == newitem["material_desc"] and arritem["information_sources"] == newitem[
                    "information_sources"] and arritem["proj_number"] == newitem["proj_number"] and arritem["sale"] == \
                        newitem["sale"] and arritem["remark"] == newitem["remark"] and arritem["write_time"] == newitem[
                    "write_time"]:
                    flag = True
            if flag:
                continue
            countq = 0
            for itm in newarrT:
                if arritem["proj_name"] == itm["proj_name"] and arritem["server_desc"] == itm["server_desc"] and \
                        arritem["server_aging"] == itm["server_aging"] and arritem["delivery_location"] == itm[
                    "delivery_location"] and arritem["material_mode"] == itm["material_mode"] and arritem[
                    "material_desc"] == itm["material_desc"] and arritem["information_sources"] == itm[
                    "information_sources"] and arritem["proj_number"] == itm["proj_number"] and arritem["sale"] == itm[
                    "sale"] and arritem["remark"] == itm["remark"] and arritem["write_time"] == itm["write_time"]:
                    countq = countq + itm["sum_count"]
            arritem["sum_count"] = countq
            newarrS.append(arritem)

        # 获取页面数据 #
        params = {"params":{"model":"bom.total.table","domain":[],"limit":999999,"context":{"information_sources":"存量表"}}}
        response = requests.get(xc_common.url + "/web/dataset/search_read", headers=xc_common.headers,
                                data=json.dumps(params))
        response = response.text
        response = json.loads(response)
        result = response["result"]
        records = result["records"]

        # 过滤None #
        new_arr_final = []
        for arritem in newarrS:
            for arritem_tab in arritem:
                if arritem[arritem_tab] is None:
                    arritem[arritem_tab] = ''
            new_arr_final.append(arritem)

        # 最终数据 VS 页面数据#
        if len(new_arr_final) != len(records):
            raise Exception("数据核对异常")
        for arritem in new_arr_final:
            is_exit = False
            for itm in records:
                if arritem["proj_name"] == itm["proj_name"] and arritem["server_desc"] == itm["server_desc"] and \
                        arritem["server_aging"] == itm["server_aging"] \
                        and arritem["delivery_location"] == itm["delivery_location"] and arritem["stock_location"] == \
                        itm["stock_location"] and arritem["material_mode"] == itm["material_mode"] \
                        and arritem["material_desc"] == itm["material_desc"] and arritem["sum_count"] == itm[
                    "sum_count"] and arritem["information_sources"] == itm["information_sources"] \
                        and arritem["proj_number"] == itm["proj_number"] and arritem["sale"] == itm["sale"] and arritem[
                    "remark"] == itm["remark"] and arritem["write_time"] == itm["write_time"]:
                    is_exit = True
            if is_exit == False:
                print("实际的数据")
                print(arritem)
                print("页面的所有的数据")
                print(records)
                raise Exception(arritem[0] + "数据异常")
        print("BOM总表（存量）-核对数据结束")

    def tearBom(self,rows):
        arr = []
        is_bom = True
        for row in rows:
            quantity = row["sum_count"]
            material_mode = row["material_mode"]
            bomstr = f"""SELECT assembly,bom_quantity,bom_assembly FROM material_bom  WHERE material_code = '{material_mode}' """
            cur.execute(bomstr)
            boms = cur.fetchall()
            for bom in boms:
                bom_new = {}
                bom_material_mode = bom[0]
                bom_material_desc = bom[2]
                bom_sum_count = quantity * bom[1]
                bom_new = {"proj_name": row["proj_name"],
                       "server_desc": row["server_desc"],
                       "server_aging": row["server_aging"],
                       "delivery_location": row["delivery_location"],
                       "stock_location": row["stock_location"],
                       "material_mode": bom_material_mode,
                       "material_desc": bom_material_desc,
                       "sum_count": bom_sum_count,
                       "information_sources": row["information_sources"],
                       "proj_number": row["proj_number"],
                       "sale": row["sale"],
                       "remark": row["remark"],
                       "write_time": row["write_time"]}
                arr.append(bom_new)
                is_bom = False
            if len(boms) == 0:
                arr.append(row)
        return arr,is_bom

    def tearDown(self):
        global num
        num=num+1
        if num>=10:
            fangfa='testBomTotal_0'+str(num)
            xx=getattr(TestBomTotal(),fangfa)
            self.log =xx.__doc__
        elif num<10:
            fangfa='testBomTotal_00'+str(num)
            xx = getattr(TestBomTotal(), fangfa)
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
        TestCase = unittest.defaultTestLoader.getTestCaseNames(TestBomTotal)
        # if num == len(TestCase):
        #     self.BL.quit()
        # else:
        #     sleep(2)
        #     self.BL.driver.refresh()

    def list2reason(self, exc_list):
        if exc_list and exc_list[-1][0] is self:
            return exc_list[-1][1]

