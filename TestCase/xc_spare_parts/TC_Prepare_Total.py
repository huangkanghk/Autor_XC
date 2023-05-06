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

class TestPrepareTotal(unittest.TestCase):

    def setUp(self):
        BL = xc_common.WindowsBL

    def save_img(self, img_name):
        img_path=globalconfig.picture_path1
        self.BL.driver.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(img_path), img_name))
        sleep(2)


    @BeautifulReport.add_test_img("testPrepareTotal_001")
    def testPrepareTotal_001(self):
        """ 【备件测算-备料总表】 页面数据校验（条件：PO单与存量） """
        # 获取页面数据 #
        params = {"params": {"model": "bom.total.table", "limit": 999999}}
        response = requests.get(xc_common.url + "/web/dataset/search_read", headers=xc_common.headers,
                                data=json.dumps(params))
        response = response.text
        response = json.loads(response)
        result = response["result"]
        Bom_records = result["records"]

        sap_nos =[]
        for Bom_record in Bom_records:
            if Bom_record["material_mode"] in sap_nos:
                continue
            else:
                sap_nos.append(Bom_record["material_mode"])

        # 同一捆绑料号的物料 也需要展示#
        arr_sap_nos = []
        for sap_no in sap_nos:
            sapstr = f"""SELECT bb.material_mode from bundling_part_number bb where bb.bundling_number = (SELECT b.bundling_number from bundling_part_number b where b.material_mode ='{sap_no}')"""
            cur.execute(sapstr)
            sap_record = cur.fetchall()
            for b_sapno in sap_record:
                if b_sapno[0] in arr_sap_nos:
                    continue
                else:
                    arr_sap_nos.append(b_sapno[0])
            if len(sap_record) ==0:
                if sap_no not in arr_sap_nos:
                    arr_sap_nos.append(sap_no)

        new_bales = []
        citys = xc_common.citys
        for arr_sap_no in arr_sap_nos:
            for city in citys:
                kc_city = city
                if kc_city =="武汉项目":
                    kc_city = "武汉"
                bl_table_querySql =f"""
                    SELECT  
                    (SELECT b.bundling_number from bundling_part_number b where b.material_mode = m.material_code) bundling_number,
                    m.material_code,
                    m.material_desc,
                    m.supplier_pn,
                    m.name m_name,
                    COALESCE((SELECT sum(sum_count) from bom_total_table bo where bo.material_mode = m.material_code ),0) sum_count,
                    (SELECT r.theoretical_defect_rate from reject_ratio r where r.sap_no =  m.material_code) reject,
                    '{city}' city,
                    COALESCE((SELECT sum(sum_count) from bom_total_table bo where bo.material_mode = m.material_code and bo.stock_location = '{kc_city}' ),0) sum_xl,
                    '' bhl,
                    COALESCE((SELECT st.num whkc from  reservoir_area_stock st where m.material_code = st.sap_no and st.city ='{city}' ),0)  kc,
                    '' qk,
                    COALESCE((SELECT st.num whkc from  reservoir_area_stock st where m.material_code = st.sap_no and st.city ='武汉' ),0) whkc,
                    '' kcyj,
                    '' sum_qk,
                    '' final_qk,
                    COALESCE((SELECT sum(kun.stock_quantity) from  kunpeng_daily kun where kun.material_code = m.material_code and ( kun.stock_category is NULL or kun.stock_category not in ('借用在途库')) and kun.factory_code ='MHMU' and kun.stock_address= 'KT02'),0) KT02,
                    COALESCE((SELECT sum(kun.stock_quantity) from  kunpeng_daily kun where kun.material_code = m.material_code and ( kun.stock_category is NULL or kun.stock_category not in ('借用在途库')) and kun.factory_code ='MHMU' and kun.stock_address= 'KT16'),0) KT16,
                    COALESCE((SELECT sum(kun.stock_quantity) from  kunpeng_daily kun where kun.material_code = m.material_code and ( kun.stock_category is NULL or kun.stock_category not in ('借用在途库')) and kun.factory_code ='MH48' and kun.stock_address= 'KT17'),0) KT17,
                    COALESCE((SELECT p.num from purchasing_transit p where p.material_mode = m.material_code),0) psl,
                    COALESCE((SELECT zc.material_num from dump_transit zc where zc.sap_no = m.material_code),0) zcsl,
                    COALESCE((SELECT rma.quantity from rma_transit rma where rma.material_code = m.material_code),0) rmasl
                     from base_material m
                    where m.material_code='{arr_sap_no}'
                    """
                cur.execute(bl_table_querySql)
                bl_table_lists = cur.fetchall()

                for bl_table_list in bl_table_lists:
                    bhl =''
                    qk = ''
                    kcyj =''
                    bundling_number = bl_table_list[0]
                    if bundling_number is None:
                        bundling_number= ''
                    reject = bl_table_list[6]
                    sum_xl= bl_table_list[8],
                    if reject !='' and reject is not None:
                        reject = float(reject)
                        temp = int(sum_xl[0]) * reject
                        if temp >= 8:
                            bhl = math.ceil(temp/4) #向上取整#
                        if temp >= 1 and temp < 8:
                            bhl = 2
                        if temp > 0 and temp < 1:
                            bhl = 1
                        if temp == 0:
                            bhl = 0
                        qk = bl_table_list[10] - bhl
                        zsl =bl_table_list[5]
                        x = zsl * reject/6
                        y = bl_table_list[12]
                        ##('adequate', '充足'), ('replenished', '补货'),('urgently_replenished', '急需补货'), ('out_of_stock', '无库存') 符合条件不再判断
                        if y >= x:
                            kcyj ='adequate'
                        elif y>= x/2 and y < x:
                            kcyj ='replenished'
                        elif y > 0 and y < x/2:
                            kcyj = 'urgently_replenished'
                        elif y <= 0:
                            kcyj = 'out_of_stock'
                    else:
                        reject = ''
                    item = {
                        "bundling_number":bundling_number,
                        "material_code":bl_table_list[1],
                        "material_desc":bl_table_list[2],
                        "supplier_pn":bl_table_list[3],
                        "m_name":bl_table_list[4],
                        "sum_count":bl_table_list[5],
                        "reject":reject,
                        "city":bl_table_list[7],
                        "sum_xl":bl_table_list[8],
                        "bhl":bhl,
                        "kc":bl_table_list[10],
                        "qk":qk,
                        "whkc":bl_table_list[12],
                        "kcyj":kcyj,
                        "sum_qk":bl_table_list[14],
                        "final_qk":bl_table_list[15],
                        "KT02":bl_table_list[16],
                        "KT16":bl_table_list[17],
                        "KT17":bl_table_list[18]-bl_table_list[20] , ##以“捆绑料号”为条件，由“备料总表”中汇总“KT17库存”。取工厂代码为MH48的KT17库存数据之后，减去对应物料的转储在途数量后再参与后续所有业务逻辑和页面展示。（V1.6）
                        "psl":bl_table_list[19],
                        "zcsl":bl_table_list[20],
                        "rmasl":bl_table_list[21]
                    }
                    new_bales.append(item)

        final_table =[]
        for new_bale in new_bales:
            count_qk = 0
            is_bhl = False
            for new_balet in new_bales:
                if new_bale["material_code"] == new_balet["material_code"]:
                    if new_balet["qk"] != '':
                        count_qk = count_qk + new_balet["qk"]
                        is_bhl = True
            if is_bhl == True:
                final_qk = count_qk + new_bale["KT17"]+ new_bale["psl"]+ new_bale["zcsl"]+ new_bale["rmasl"]
                new_bale["sum_qk"] = count_qk
                new_bale["final_qk"] = final_qk
            final_table.append(new_bale)


        # 获取页面数据 #
        params = {"params": {"model": "prepare.materials", "domain": [], "limit": 999999,"context":{"information_sources":""}}}
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
                if arritem[arritem_tab] is None :
                    arritem[arritem_tab] = ''
                    if arritem_tab =="kt02_quantity" or arritem_tab =="kt16_quantity" or arritem_tab =="kt17_quantity":
                        arritem[arritem_tab] = 0
                if isinstance(arritem[arritem_tab], float):
                    if arritem_tab!= 'theo_non_rate':
                        arritem[arritem_tab] = int(arritem[arritem_tab])
            new_arr_final.append(arritem)

        for arritem in final_table:
            is_exit = False
            for itm in new_arr_final:
                if arritem["bundling_number"] == itm["bundling_number"] and arritem["material_code"] == itm["material_code"] and  arritem["material_desc"] == itm["material_desc"] and arritem["supplier_pn"] == itm["supplier_pn"] and arritem["m_name"] == itm["name"] and  arritem["city"] == itm["city"] and arritem["psl"] == itm["purchase_in_transit"] and  arritem["zcsl"] == itm["dump_in_transit"] and arritem["rmasl"] == itm["rma_in_transit"] and  arritem["KT02"] == itm["kt02_quantity"] and arritem["KT16"] == itm["kt16_quantity"] and  arritem["KT17"] == itm["kt17_quantity"] and  arritem["whkc"] == itm["wuhan_stock_quantity"] and arritem["kc"] == itm["stock_quantity"] and arritem["qk"] == itm["gap_quantity"] and  arritem["reject"] == itm["theo_non_rate"] and  arritem["kcyj"] == itm["stock_alert_status"] and arritem["sum_count"] == itm["total_usage"] and arritem["sum_xl"] == itm["sales"] and  arritem["final_qk"] == itm["final_gap"] and arritem["sum_qk"] == itm["sum_each_gap"] and  arritem["bhl"] == itm["reserve_quantity"]:
                    is_exit = True
                    break
            if is_exit ==False:
                print("实际的数据")
                print(arritem)
                raise Exception("备料总表数据核对异常")
        if len(final_table) != len(new_arr_final):
            raise Exception("备料总表数据核对异常")
        print("备料总表-核对数据结束(PO单与存量)")

    @BeautifulReport.add_test_img("testPrepareTotal_002")
    def testPrepareTotal_002(self):
        """ 【备件测算-备料总表】 页面数据校验（条件：存量） """
        # 获取页面数据 #
        params = {"params":{"model":"bom.total.table","domain":[], "limit": 999999,"context":{"information_sources":"存量表"}}}
        response = requests.get(xc_common.url + "/web/dataset/search_read", headers=xc_common.headers,
                                data=json.dumps(params))
        response = response.text
        response = json.loads(response)
        result = response["result"]
        Bom_records = result["records"]

        sap_nos = []
        for Bom_record in Bom_records:
            if Bom_record["material_mode"] in sap_nos:
                continue
            else:
                sap_nos.append(Bom_record["material_mode"])

        # 同一捆绑料号的物料 也需要展示#
        arr_sap_nos = []
        for sap_no in sap_nos:
            sapstr = f"""SELECT bb.material_mode from bundling_part_number bb where bb.bundling_number = (SELECT b.bundling_number from bundling_part_number b where b.material_mode ='{sap_no}')"""
            cur.execute(sapstr)
            sap_record = cur.fetchall()
            for b_sapno in sap_record:
                if b_sapno[0] in arr_sap_nos:
                    continue
                else:
                    arr_sap_nos.append(b_sapno[0])
            if len(sap_record) == 0:
                if sap_no not in arr_sap_nos:
                    arr_sap_nos.append(sap_no)

        new_bales = []
        citys = xc_common.citys
        for arr_sap_no in arr_sap_nos:
            for city in citys:
                kc_city = city
                if kc_city == "武汉项目":
                    kc_city = "武汉"
                bl_table_querySql = f"""
                        SELECT  
                        (SELECT b.bundling_number from bundling_part_number b where b.material_mode = m.material_code) bundling_number,
                        m.material_code,
                        m.material_desc,
                        m.supplier_pn,
                        m.name m_name,
                        COALESCE((SELECT sum(sum_count) from bom_total_table bo where bo.material_mode = m.material_code and information_sources ='存量表' ),0) sum_count,
                        (SELECT r.theoretical_defect_rate from reject_ratio r where r.sap_no =  m.material_code) reject,
                        '{city}' city,
                        COALESCE((SELECT sum(sum_count) from bom_total_table bo where bo.material_mode = m.material_code and bo.stock_location = '{kc_city}' and information_sources ='存量表' ),0) sum_xl,
                        '' bhl,
                        COALESCE((SELECT st.num whkc from  reservoir_area_stock st where m.material_code = st.sap_no and st.city ='{city}' ),0)  kc,
                        '' qk,
                        COALESCE((SELECT st.num whkc from  reservoir_area_stock st where m.material_code = st.sap_no and st.city ='武汉' ),0) whkc,
                        '' kcyj,
                        '' sum_qk,
                        '' final_qk,
                        COALESCE((SELECT sum(kun.stock_quantity) from  kunpeng_daily kun where kun.material_code = m.material_code and ( kun.stock_category is NULL or kun.stock_category not in ('借用在途库')) and kun.factory_code ='MHMU' and kun.stock_address= 'KT02'),0) KT02,
                        COALESCE((SELECT sum(kun.stock_quantity) from  kunpeng_daily kun where kun.material_code = m.material_code and ( kun.stock_category is NULL or kun.stock_category not in ('借用在途库')) and kun.factory_code ='MHMU' and kun.stock_address= 'KT16'),0) KT16,
                        COALESCE((SELECT sum(kun.stock_quantity) from  kunpeng_daily kun where kun.material_code = m.material_code and ( kun.stock_category is NULL or kun.stock_category not in ('借用在途库')) and kun.factory_code ='MH48' and kun.stock_address= 'KT17'),0) KT17,
                        COALESCE((SELECT p.num from purchasing_transit p where p.material_mode = m.material_code),0) psl,
                        COALESCE((SELECT zc.material_num from dump_transit zc where zc.sap_no = m.material_code),0) zcsl,
                        COALESCE((SELECT rma.quantity from rma_transit rma where rma.material_code = m.material_code),0) rmasl
                         from base_material m
                        where m.material_code='{arr_sap_no}'
                        """
                cur.execute(bl_table_querySql)
                bl_table_lists = cur.fetchall()

                for bl_table_list in bl_table_lists:
                    bhl = ''
                    qk = ''
                    kcyj = ''
                    bundling_number = bl_table_list[0]
                    if bundling_number is None:
                        bundling_number = ''
                    reject = bl_table_list[6]
                    sum_xl = bl_table_list[8],
                    if reject != '' and reject is not None:
                        reject = float(reject)
                        temp = int(sum_xl[0]) * reject
                        if temp >= 8:
                            bhl = math.ceil(temp / 4)  # 向上取整#
                        if temp >= 1 and temp < 8:
                            bhl = 2
                        if temp > 0 and temp < 1:
                            bhl = 1
                        if temp == 0:
                            bhl = 0
                        qk = bl_table_list[10] - bhl
                        zsl = bl_table_list[5]
                        x = zsl * reject / 6
                        y = bl_table_list[12]
                        ##('adequate', '充足'), ('replenished', '补货'),('urgently_replenished', '急需补货'), ('out_of_stock', '无库存') 符合条件不再判断
                        if y >= x:
                            kcyj = 'adequate'
                        elif y >= x / 2 and y < x:
                            kcyj = 'replenished'
                        elif y > 0 and y < x / 2:
                            kcyj = 'urgently_replenished'
                        elif y <= 0:
                            kcyj = 'out_of_stock'
                    else:
                        reject = ''
                    item = {
                        "bundling_number": bundling_number,
                        "material_code": bl_table_list[1],
                        "material_desc": bl_table_list[2],
                        "supplier_pn": bl_table_list[3],
                        "m_name": bl_table_list[4],
                        "sum_count": bl_table_list[5],
                        "reject": reject,
                        "city": bl_table_list[7],
                        "sum_xl": bl_table_list[8],
                        "bhl": bhl,
                        "kc": bl_table_list[10],
                        "qk": qk,
                        "whkc": bl_table_list[12],
                        "kcyj": kcyj,
                        "sum_qk": bl_table_list[14],
                        "final_qk": bl_table_list[15],
                        "KT02": bl_table_list[16],
                        "KT16": bl_table_list[17],
                        "KT17": bl_table_list[18] - bl_table_list[20],
                        ##以“捆绑料号”为条件，由“备料总表”中汇总“KT17库存”。取工厂代码为MH48的KT17库存数据之后，减去对应物料的转储在途数量后再参与后续所有业务逻辑和页面展示。（V1.6）
                        "psl": bl_table_list[19],
                        "zcsl": bl_table_list[20],
                        "rmasl": bl_table_list[21]
                    }
                    new_bales.append(item)

        final_table = []
        for new_bale in new_bales:
            count_qk = 0
            is_bhl = False
            for new_balet in new_bales:
                if new_bale["material_code"] == new_balet["material_code"]:
                    if new_balet["qk"] != '':
                        count_qk = count_qk + new_balet["qk"]
                        is_bhl = True
            if is_bhl == True:
                final_qk = count_qk + new_bale["KT17"] + new_bale["psl"] + new_bale["zcsl"] + new_bale["rmasl"]
                new_bale["sum_qk"] = count_qk
                new_bale["final_qk"] = final_qk
            final_table.append(new_bale)

        # 获取页面数据 #
        params = {"params": {"model": "prepare.materials", "domain": [], "limit": 999999,
                             "context": {"information_sources": "存量表"}}}
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

        for arritem in final_table:
            is_exit = False
            for itm in new_arr_final:
                if arritem["material_code"] == itm["material_code"] and arritem["city"] == itm["city"] and arritem["material_code"] == "302-000248":
                    print(123)
                if arritem["bundling_number"] == itm["bundling_number"] and arritem["material_code"] == itm[
                    "material_code"] and arritem["material_desc"] == itm["material_desc"] and arritem["supplier_pn"] == \
                        itm["supplier_pn"] and arritem["m_name"] == itm["name"] and arritem["city"] == itm["city"] and \
                        arritem["psl"] == itm["purchase_in_transit"] and arritem["zcsl"] == itm["dump_in_transit"] and \
                        arritem["rmasl"] == itm["rma_in_transit"] and arritem["KT02"] == itm["kt02_quantity"] and \
                        arritem["KT16"] == itm["kt16_quantity"] and arritem["KT17"] == itm["kt17_quantity"] and arritem[
                    "whkc"] == itm["wuhan_stock_quantity"] and arritem["kc"] == itm["stock_quantity"] and arritem[
                    "qk"] == itm["gap_quantity"] and arritem["reject"] == itm["theo_non_rate"] and arritem["kcyj"] == \
                        itm["stock_alert_status"] and arritem["sum_count"] == itm["total_usage"] and arritem[
                    "sum_xl"] == itm["sales"] and arritem["final_qk"] == itm["final_gap"] and arritem["sum_qk"] == itm[
                    "sum_each_gap"] and arritem["bhl"] == itm["reserve_quantity"]:
                    is_exit = True
                    break
            if is_exit == False:
                print("实际的数据")
                print(arritem)
                raise Exception("备料总表数据核对异常")
        if len(final_table) != len(new_arr_final):
            raise Exception("备料总表数据核对异常")
        print("备料总表-核对数据结束（存量表）")

    def tearDown(self):
        global num
        num=num+1
        if num>=10:
            fangfa='testPrepareTotal_0'+str(num)
            xx=getattr(TestPrepareTotal(),fangfa)
            self.log =xx.__doc__
        elif num<10:
            fangfa='testPrepareTotal_00'+str(num)
            xx = getattr(TestPrepareTotal(), fangfa)
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
        TestCase = unittest.defaultTestLoader.getTestCaseNames(TestPrepareTotal)
        # if num == len(TestCase):
        #     self.BL.quit()
        # else:
        #     sleep(2)
        #     self.BL.driver.refresh()

    def list2reason(self, exc_list):
        if exc_list and exc_list[-1][0] is self:
            return exc_list[-1][1]

