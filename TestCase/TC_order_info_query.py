import unittest,time,os,platform,xlrd,xlwt
import xlsxwriter as xw
from time import sleep
import logging
from log import log
from Public.common import TestCaseInfo,DoExcel,CommonConfig as cc
from Public.pages import OkchemLoginPage
from Public.pages import QutoLoginPage
from config import globalconfig
from BeautifulReport import BeautifulReport
from run import *
from Public.common import send_mail as dd
import  pytesseract,sys,os
import  requests,json,redis
import psycopg2
import time
from builtins import str
import calendar
import itertools as it
import calendar
import datetime
import math
from operator import itemgetter

# wb = xlrd.open_workbook("E:\Desktop\gitlab-port.xls")
# sh = wb.sheet_by_name("address")
# url = sh.col_values(0)
# port = sh.col_values(1)

url =""
num =0

class Test_order_info_query(unittest.TestCase):

    def setUp(self):
        self.url = 'http://10.3.70.154:7888'


    def save_img(self, img_name):
        img_path=globalconfig.picture_path1
        self.BL.driver.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(img_path), img_name))
        sleep(2)


    @BeautifulReport.add_test_img("testQutoLogin_001")
    def testQutoLogin_001(self):
        """测试登录页面UI"""
        datarow = []
        conn = psycopg2.connect(dbname="xc-test",user="odoo",password="xctest$",host="10.3.70.132",port="32682")
        cur = conn.cursor();
        cur.execute('select * from purchase_order_inventory')
        rows = cur.fetchall()
        for row in rows:
            sapno = row[1]
            cur.execute('select * from material_bom where material_code = s%',sapno)
            bomrows = cur.fetchall()
            if len(bomrows) >0:
                for bomrow in bomrows:
                    sapno1 = bomrow[1]
                    quat = bomrow[3]
            else:
                datarow.append(row)

        for row in datarow:
            print(1)



    # @BeautifulReport.add_test_img("testQutoLogin_001")
    # def testQutoLogin_001(self):
    #     """文件修改"""
    #     tnows = 1;
    #     workbook = xw.Workbook("E:\\Desktop\\gittest.xlsx")  # 创建工作簿
    #     worksheet1 = workbook.add_worksheet("sheet1")  # 创建子表
    #     worksheet1.activate()  # 激活表
    #
    #     ##打开表
    #     wb = xlrd.open_workbook("E:\\Desktop\\test.xls")
    #     sh = wb.sheet_by_name("Sheet1")
    #     url = sh.col_values(0)
    #
    #     ### 100个gitlab项目
    #     counti = 100
    #     for i in range(counti):
    #         i = i + 1
    #         snum = 0
    #         for urlDetail in url:
    #             print(urlDetail)
    #             print(i)
    #             print(tnows)
    #             rowvalue  = sh.row_values(snum)
    #             rowvalue.append("gitlab"+str(i))
    #             worksheet1.write_row('A' + str(tnows), rowvalue)
    #             tnows = tnows + 1
    #             snum = snum +1
    #     workbook.close()

    # # 获取移动平均价
    # @BeautifulReport.add_test_img("testQutoLogin_0052")
    # def testQutoLogin_0051(self):
    #     """测试不输入账号密码是否有提示信息"""
    #     wb = xlrd.open_workbook("D:\download\PO单与存量123.xls")
    #     order_data = wb.sheet_by_name("PO单与存量")
    #     nrows = order_data.nrows
    #
    #     i = 1
    #     flag = False
    #     while nrows > i:
    #         orders = order_data.row_values(i)
    #         order0= orders[0]
    #         order1 = orders[2]
    #         order2 = orders[4]
    #         order3 = orders[5]
    #         order4 = orders[8]
    #         order5 = orders[9]
    #         order6 = orders[10]
    #         order7 = orders[11]
    #         order8 = orders[12]
    #
    #         j = i+1
    #         flag = True
    #         while nrows > j:
    #             ordersj = order_data.row_values(j)
    #             orderj0 = ordersj[0]
    #             orderj1 = ordersj[2]
    #             orderj2 = ordersj[4]
    #             orderj3 = ordersj[5]
    #             orderj4 = ordersj[8]
    #             orderj5 = ordersj[9]
    #             orderj6 = ordersj[10]
    #             orderj7 = ordersj[11]
    #             orderj8 = ordersj[12]
    #             print(j)
    #             if orderj0 == order0 and  orderj1 == order1 and order2 == orderj2 and order3 == orderj3  and order4 == orderj4 and order5 == orderj5 and order6 == orderj6 and order7 == orderj7 and order8 == orderj8 :
    #                 print(orderj3)
    #             j = j+1
    #         i = i+1
    #     # 获取移动平均价
    #
    # @BeautifulReport.add_test_img("testQutoLogin_0053")
    # def testQutoLogin_0053(self):
    #     """测试不输入账号密码是否有提示信息"""
    #     wb = xlrd.open_workbook("E:\Desktop\物料数量和物料行数.xls")
    #     order_data = wb.sheet_by_name("Sheet1")
    #     quot_data = wb.sheet_by_name("Sheet2")
    #     all_order = order_data.nrows;
    #     all_quot = quot_data.nrows;
    #     order_data
    #     workbook = xw.Workbook("E:\\Desktop\\gittest—row.xlsx")  # 创建工作簿
    #     worksheet1 = workbook.add_worksheet("sheet1")  # 创建子表
    #     worksheet1.activate()  # 激活表
    #
    #     i = 1
    #     while all_order > i:
    #         orders = order_data.row_values(i)
    #         order_quot = orders[0]
    #         num_order = orders[1]
    #         j = 1
    #         flag = True
    #         while all_quot > j:
    #             quots = quot_data.row_values(j)
    #             quot = quots[0]
    #             num_quot = quots[1]
    #             if quot != order_quot or num_order != num_quot:
    #                 print(order_quot + "  ")
    #
    #                 j = j + 1
    #             else:
    #                 print(i)
    #                 i = i + 1
    #                 worksheet1.write('A' + str(i), order_quot)
    #                 worksheet1.write('B' + str(i), quot)
    #                 worksheet1.write('C' + str(i), 'True')
    #                 worksheet1.write('D' + str(i), num_order)
    #                 worksheet1.write('E' + str(i), quot)
    #                 worksheet1.write('F' + str(i), 'True')
    #                 flag = False
    #                 break;
    #         if flag:
    #             worksheet1.write('A' + str(i), order_quot)
    #             worksheet1.write('B' + str(i), quot)
    #             worksheet1.write('C' + str(i), 'Fale')
    #             worksheet1.write('D' + str(i), num_order)
    #             worksheet1.write('E' + str(i), quot)
    #             worksheet1.write('F' + str(i), 'Fale')
    #             i = i + 1
    #     worksheet1.close()

    #
    @BeautifulReport.add_test_img("testQutoLogin_003")
    def testQutoLogin_003(self):
        """测试输入账号密码但验证码错误是否有提示信息"""
        conn = psycopg2.connect(dbname="xc-test",user="odoo",password="xctest$",host="10.3.70.132",port="32682")
        cur = conn.cursor();
        cur.execute('select sap_no from material')
        rows = cur.fetchall()

        workbook = xw.Workbook("E:\\Desktop\\cesgy99.xlsx")  # 创建工作簿
        worksheet1 = workbook.add_worksheet("sheet1")  # 创建子表
        worksheet1.activate()  # 激活表
        worksheet1.write('A1', "类型")
        worksheet1.write('B1', "日期")
        worksheet1.write('C1', "物料代码")
        worksheet1.write('D1', "物料描述")
        worksheet1.write('E1', "需求/供应单号")
        worksheet1.write('F1', "需求/供应单名称")
        worksheet1.write('G1', "数量")
        worksheet1.write('H1', "余量")
        worksheet1.write('I1', "idces")
        ##连接Bi
        i = 2
        for row in rows:
            print(row)
            headers = {"Content-Type": "application/json;charset=UTF-8",
                       "Cookie": "session_id=c977cd09b8193ad0779d913076e11eae10798911"}
            params = {"jsonrpc": "2.0", "method": "call", "params": {"model": "order.supply.demand.matching.query",
                                                                     "domain": [["sap_no", "=", row]],
                                                                     "fields": ["category", "opo_date", "sap_no",
                                                                                "desc", "order_no", "order_name",
                                                                                "quantity", "margin"], "limit": 1000,
                                                                     "sort": "",
                                                                     "context": {"lang": "zh_CN", "tz": "Asia/Shanghai",
                                                                                 "uid": 591, "allowed_company_ids": [1],
                                                                                 "params": {"menu_id": 617,
                                                                                            "action": 1581}}},
                      "id": 233090290}
            response = requests.get("http://10.3.70.154:7888/web/dataset/search_read", headers=headers,
                                    data=json.dumps(params))
            response = response.text
            response = json.loads(response)
            result = response["result"]
            records = result["records"]
            k =1
            print(i)
            print(1111)
            for record in records:
                worksheet1.write('A' + str(i), record["category"])
                worksheet1.write('A' + str(i), record["category"])
                worksheet1.write('B' + str(i), record["opo_date"])
                worksheet1.write('C' + str(i), record["sap_no"])
                worksheet1.write('D' + str(i), record["desc"])
                worksheet1.write('E' + str(i), record["order_no"])
                worksheet1.write('F' + str(i), record["order_name"])
                worksheet1.write('G' + str(i), record["quantity"])
                worksheet1.write('H' + str(i), record["margin"])
                worksheet1.write('I' + str(i), k)
                k = k+1
                i = i+1
        workbook.close()

    @BeautifulReport.add_test_img("testQutoLogin_004")
    def testQutoLogin_004(self):
        conn = psycopg2.connect(dbname="xc-test", user="odoo", password="xctest$", host="10.3.70.132", port="32682")
        cur = conn.cursor();
        cur.execute('select sap_no from material')
        rows = cur.fetchall()

        workbook = xw.Workbook("E:\\Desktop\\cg.xlsx")  # 创建工作簿
        worksheet1 = workbook.add_worksheet("sheet1")  # 创建子表
        worksheet1.activate()  # 激活表
        worksheet1.write('A1', "状态")
        worksheet1.write('B1', "下单岗姓名")
        worksheet1.write('C1', "采购订单代码")
        worksheet1.write('D1', "采购单行项目")
        worksheet1.write('E1', "供应商名称")
        worksheet1.write('F1', "传送条目")
        worksheet1.write('G1', "CRM项目编号")
        worksheet1.write('H1', "项目名称")
        worksheet1.write('I1', "物料代码")
        worksheet1.write('J1', "物料名称")
        worksheet1.write('K1', "采购单创建日期")
        worksheet1.write('L1', "计划到货日期")
        worksheet1.write('M1', "采购数量")
        worksheet1.write('N1', "人民币金额（不含税）")
        i = 2
        for row in rows:
            print(row)
            if "69-" in row[0]:
                continue
            rowstr = row[0].replace("-","")
            cont = 18 - len(rowstr)
            ss = 0
            ssstr = ""
            while ss < cont:
                ssstr = ssstr + "0"
                ss = ss + 1
            rowstr = ssstr + rowstr
            # if i == 20:
            #     break
            headers = {"Content-Type": "application/json;charset=UTF-8",
                       "Cookie": "session_id=46cfc05fb7b3bfe165238f0fc366c45a18c8a5fc"}
            params = {"jsonrpc":"2.0","method":"call","params":{"model":"order.purchase.order.query",
                                                                "domain":[["wldm","ilike",rowstr]],
                                                                "limit":8000,"context":{"lang":"zh_CN","tz":"Asia/Shanghai","uid":591,"allowed_company_ids":[1],
                                                                                                                                                                                                                                                                                                          "params":{"action":1580,"cids":1,"menu_id":617,"model":"order.purchase.order.query","view_type":"list"}}},"id":282830911}
            response = requests.get("http://10.3.70.154:7888/web/dataset/search_read", headers=headers,
                                    data=json.dumps(params))
            sleep(0.25)
            response = response.text
            response = json.loads(response)
            result = response["result"]
            records = result["records"]

            for record in records:
                worksheet1.write('A' + str(i), record["zt"])
                worksheet1.write('B' + str(i), record["ddsqr"])
                worksheet1.write('C' + str(i), record["cgdddm"])
                worksheet1.write('D' + str(i), record["cgdhxm"])
                worksheet1.write('E' + str(i), record["gysmc"])
                worksheet1.write('F' + str(i), record["cstm"])
                worksheet1.write('G' + str(i), record["btwb"])
                worksheet1.write('H' + str(i), record["btzs"])
                worksheet1.write('I' + str(i), record["wldm"])
                worksheet1.write('J' + str(i), record["zwwlmc"])
                worksheet1.write('K' + str(i), record["cgdcjrq"])
                worksheet1.write('L' + str(i), record["jhdhrq"])
                worksheet1.write('M' + str(i), record["sl"])
                worksheet1.write('N' + str(i), record["je"])
                i = i + 1
        workbook.close()


     ##查询库存-----------------1
    @BeautifulReport.add_test_img("testQutoLogin_005")
    def testQutoLogin_005(self):
        conn = psycopg2.connect(dbname="xc-test", user="odoo", password="xctest$", host="10.3.70.132", port="32682")
        cur = conn.cursor();
        cur.execute('select sap_no from material where 1 =1  order by sap_no ')
        rows = cur.fetchall()

        workbook = xw.Workbook("E:\\Desktop\\kc.xlsx")  # 创建工作簿
        worksheet1 = workbook.add_worksheet("sheet1")  # 创建子表
        worksheet1.activate()  # 激活表
        worksheet1.write('A1', "库存代码")
        worksheet1.write('B1', "库存地")
        worksheet1.write('C1', "SAP NO")
        worksheet1.write('D1', "移动平均价")
        worksheet1.write('E1', "kcsl")
        worksheet1.write('F1', "kcje")
        i = 2
        kk = 0
        for row in rows:
            kk = kk +1
            print(kk)
            print(row)
            headers = {"Content-Type": "application/json;charset=UTF-8",
                       "Cookie": "session_id=c977cd09b8193ad0779d913076e11eae10798911"}
            params = {"jsonrpc":"2.0","method":"call",
                      "params":{"model":"order.stock.information.query",
                                "domain":[["sap_no","ilike",row[0]]],
                                "limit":8000,"context":{"lang":"zh_CN","tz":"Asia/Shanghai","uid":591,"allowed_company_ids":[1],"params":{"menu_id":617,"action":1582}}},"id":131690649}
            if row[0] == "282-279104":
                print(123)
            response = requests.get("http://10.3.70.154:7888/web/dataset/search_read", headers=headers,data=json.dumps(params))
            response = response.text
            response = json.loads(response)
            if "result" not in response:
                continue
            result = response["result"]
            records = result["records"]
            if len(records) == 0:
                continue
            for record in records:
                worksheet1.write('A' + str(i), record["stock_address"])
                worksheet1.write('B' + str(i), '')
                worksheet1.write('C' + str(i), record["sap_no"])
                worksheet1.write('D' + str(i), record["mov_avg_price"])
                if record["mov_avg_price"] != 0 and record["mov_avg_price"] == False:
                    worksheet1.write('D' + str(i), "")
                worksheet1.write('E' + str(i), record["stock_count"])
                if record["stock_count"] != 0 and record["stock_count"] == False:
                    worksheet1.write('E' + str(i), "")
                worksheet1.write('F' + str(i), record["stock_amount"])
                if record["stock_amount"] != 0 and record["stock_amount"] == False:
                    worksheet1.write('F' + str(i), "")
                i = i + 1
                print("数量" + str(i))
        workbook.close()

    ##查询库存---------------------2
    @BeautifulReport.add_test_img("testQutoLogin_006")
    def testQutoLogin_006(self):
        conn = psycopg2.connect(dbname="xc-test", user="odoo", password="xctest$", host="10.3.70.132", port="32682")
        cur = conn.cursor();
        cur.execute('select sap_no from material')
        rows = cur.fetchall()

        workbook = xw.Workbook("E:\\Desktop\\testyyjj.xlsx")  # 创建工作簿
        worksheet1 = workbook.add_worksheet("sheet1")  # 创建子表
        worksheet1.activate()  # 激活表
        worksheet1.write('A1', "库存代码")
        worksheet1.write('B1', "库存地")
        worksheet1.write('C1', "SAP NO")
        worksheet1.write('D1', "ydjj")
        worksheet1.write('E1', "kcsl")

        wb = xlrd.open_workbook("E:\\Desktop\\订单-信息查询.xls")
        order_datas = wb.sheet_by_name("订单-信息查询")

        i = 2
        for row in rows:
            print(row)
            if '69-' in row[0]:
                repstr = "SELECT mi2.sap_no sap_no302, mi.sap_no sap_no69 FROM quotation_product_rel qp,material mi,material mi2 " \
                         "WHERE	qp.mid = mi.ID AND qp.rid = mi2.ID "
                repstr = repstr + "and mi.sap_no ='" +str(row[0]) + "'"
                cur.execute(repstr)
                records302 = cur.fetchall()
                sumPrice=0
                avg_count=0
                for record in records302:
                    for order_data in  order_datas:
                        strnew =""
                        if str(order_data[0].value)[0:10] == "0000000000":
                            strnew = str(order_data[0].value)[-10:]
                            strlist = list(strnew)
                            strlist.insert(2, "-")
                            strnew = "".join(strlist)
                        if str(order_data[0].value)[0:9] == "000000000":
                            strnew = str(order_data[0].value)[-9:]
                            strlist = list(strnew)
                            strlist.insert(3, "-")
                            strnew = "".join(strlist)
                        if strnew == record[0]:
                            sumPrice = sumPrice + order_data[1].value
                            avg_count = avg_count+1
                if avg_count>0:
                    worksheet1.write('A' + str(i), row[0])
                    worksheet1.write('B' + str(i), sumPrice/avg_count)
                    i = i + 1
            else:
                sumPrice = 0
                avg_count = 0
                for order_data in order_datas:
                    strnew = ""
                    if str(order_data[0].value)[0:10] == "0000000000":
                        strnew = str(order_data[0].value)[-10:]
                        strlist = list(strnew)
                        strlist.insert(2,"-")
                        strnew= "".join(strlist)
                    if str(order_data[0].value)[0:9] == "000000000":
                        strnew = str(order_data[0].value)[-9:]
                        strlist = list(strnew)
                        strlist.insert(3, "-")
                        strnew = "".join(strlist)
                    if row[0] == strnew:
                        worksheet1.write('A' + str(i), row[0])
                        worksheet1.write('B' + str(i), order_data[1].value)
                        i = i+1
                        break
        workbook.close()

    @BeautifulReport.add_test_img("testQutoLogin_007")
    def testQutoLogin_007(self):
        conn = psycopg2.connect(dbname="xc-test", user="odoo", password="xctest$", host="10.3.70.132", port="32682")
        cur = conn.cursor();
        cur.execute('SELECT proj_name,server_desc,server_aging,delivery_location,stock_location,material_mode,material_desc,sum,information_sources, proj_number,sale,remark,write_date from purchase_order_inventory')
        rows = cur.fetchall()

        workbook = xw.Workbook("E:\\Desktop\\bom.xlsx")  # 创建工作簿
        worksheet1 = workbook.add_worksheet("sheet1")  # 创建子表
        worksheet1.activate()  # 激活表
        worksheet1.write('A1', "proj_name")
        worksheet1.write('B1', "server_desc")
        worksheet1.write('C1', "server_aging")
        worksheet1.write('D1', "delivery_location")
        worksheet1.write('E1', "stock_location")
        worksheet1.write('F1', "material_mode")
        worksheet1.write('G1', "material_desc")
        worksheet1.write('H1', "sum")
        worksheet1.write('I1', "information_sources")
        worksheet1.write('J1', "proj_number")
        worksheet1.write('K1', "sale")
        worksheet1.write('L1', "remark")
        worksheet1.write('M1', "write_date")
        arr = []
        i = 2
        for row in rows:
            print(row[5])
            quantity = row[7]
            bomstr = "SELECT assembly,bom_quantity,bom_assembly FROM material_bom  WHERE material_code ="+"'"+row[5]+"'"
            cur.execute(bomstr)
            boms = cur.fetchall()
            if len(boms) == 0:
                # worksheet1.write('A' + str(i), row[0])
                # worksheet1.write('B' + str(i), row[1])
                # worksheet1.write('C' + str(i), row[2])
                # worksheet1.write('D' + str(i), row[3])
                # worksheet1.write('E' + str(i), row[4])
                # worksheet1.write('F' + str(i), row[5])
                # worksheet1.write('G' + str(i), row[6])
                # worksheet1.write('H' + str(i), row[7])
                # worksheet1.write('I' + str(i), row[8])
                # worksheet1.write('J' + str(i), row[9])
                # worksheet1.write('K' + str(i), row[10])
                # worksheet1.write('L' + str(i), row[11])
                # worksheet1.write('M' + str(i), str(row[12]))
                item = {"A": row[0],
                        'B': row[1],
                        'C': row[2],
                        'D': row[3],
                        'E': row[4],
                        'F': row[5],
                        'G': row[6],
                        'H': row[7] ,
                        'I': row[8],
                        'J': row[9],
                        'K': row[10],
                        'L': row[11],
                        'M': str(row[12])}
                arr.append(item)
                ##i = i + 1
                continue
            ###拆BOM
            for bom in boms:
                bomstr = "SELECT assembly,bom_quantity,bom_assembly FROM material_bom  WHERE material_code =" + "'" + bom[0] + "'"
                cur.execute(bomstr)
                bomsub1 = cur.fetchall()
                if len(bomsub1) == 0:
                    # worksheet1.write('A' + str(i), row[0])
                    # worksheet1.write('B' + str(i), row[1])
                    # worksheet1.write('C' + str(i), row[2])
                    # worksheet1.write('D' + str(i), row[3])
                    # worksheet1.write('E' + str(i), row[4])
                    # worksheet1.write('F' + str(i), bom[0])
                    # worksheet1.write('G' + str(i), row[6])
                    # worksheet1.write('H' + str(i), row[7] * bom[1] )
                    # worksheet1.write('I' + str(i), row[8])
                    # worksheet1.write('J' + str(i), row[9])
                    # worksheet1.write('K' + str(i), row[10])
                    # worksheet1.write('L' + str(i), row[11])
                    # worksheet1.write('M' + str(i), str(row[12]))
                    item = {"A": row[0],
                            'B': row[1],
                            'C': row[2],
                            'D': row[3],
                            'E': row[4],
                            'F': bom[0],
                            'G': bom[2],
                            'H': row[7] * bom[1],
                            'I': row[8],
                            'J': row[9],
                            'K': row[10],
                            'L': row[11],
                            'M': str(row[12])}
                    arr.append(item)
                    ##i = i + 1
                    continue
                for bomsu  in bomsub1:
                    bomstr = "SELECT assembly,bom_quantity,bom_assembly FROM material_bom  WHERE material_code =" + "'" + bomsu[0] + "'"
                    cur.execute(bomstr)
                    bomsub2 = cur.fetchall()
                    if len(bomsub2) == 0:
                        # worksheet1.write('A' + str(i), row[0])
                        # worksheet1.write('B' + str(i), row[1])
                        # worksheet1.write('C' + str(i), row[2])
                        # worksheet1.write('D' + str(i), row[3])
                        # worksheet1.write('E' + str(i), row[4])
                        # worksheet1.write('F' + str(i), bomsu[0])
                        # worksheet1.write('G' + str(i), row[6])
                        # worksheet1.write('H' + str(i),  row[7]* bom[1] * bomsu[1])
                        # worksheet1.write('I' + str(i), row[8])
                        # worksheet1.write('J' + str(i), row[9])
                        # worksheet1.write('K' + str(i), row[10])
                        # worksheet1.write('L' + str(i), row[11])
                        # worksheet1.write('M' + str(i), str(row[12]))
                        item ={"A":row[0],
                               'B': row[1],
                               'C': row[2],
                               'D': row[3],
                               'E': row[4],
                               'F' :bomsu[0],
                               'G' :bomsu[2],
                               'H' : row[7]* bom[1] * bomsu[1],
                               'I' : row[8],
                               'J' : row[9],
                               'K' : row[10],
                               'L' : row[11],
                               'M' : str(row[12])}
                        arr.append(item)
                        ##i = i + 1
                        continue
                    for bomsu2  in bomsub2:
                        bomstr = "SELECT assembly,bom_quantity,bom_assembly FROM material_bom  WHERE material_code =" + "'" + bomsu2[
                            0] + "'"
                        cur.execute(bomstr)
                        bomsub3 = cur.fetchall()
                        if len(bomsub3) == 0:
                            # worksheet1.write('A' + str(i), row[0])
                            # worksheet1.write('B' + str(i), row[1])
                            # worksheet1.write('C' + str(i), row[2])
                            # worksheet1.write('D' + str(i), row[3])
                            # worksheet1.write('E' + str(i), row[4])
                            # worksheet1.write('F' + str(i), bomsu2[0])
                            # worksheet1.write('G' + str(i), row[6])
                            # worksheet1.write('H' + str(i), row[7] * bom[1] * bomsu[1] * bomsu2[1])
                            # worksheet1.write('I' + str(i), row[8])
                            # worksheet1.write('J' + str(i), row[9])
                            # worksheet1.write('K' + str(i), row[10])
                            # worksheet1.write('L' + str(i), row[11])
                            # worksheet1.write('M' + str(i), str(row[12]))
                            item = {"A": row[0],
                                    'B': row[1],
                                    'C': row[2],
                                    'D': row[3],
                                    'E': row[4],
                                    'F': bomsu2[0],
                                    'G': bomsu2[2],
                                    'H': row[7] * bom[1] * bomsu[1] * bomsu2[1],
                                    'I': row[8],
                                    'J': row[9],
                                    'K': row[10],
                                    'L': row[11],
                                    'M': str(row[12])}
                            arr.append(item)
                            ##i = i + 1
                            continue
                        for bomsu3 in bomsub3:
                            print(12)
        newarr = []
        for arritem  in arr:
            repstr = "SELECT sap_69_no,sap_302_no,material_desc from material_transformation where sap_69_no =" + "'" + arritem[
                "F"] + "'"
            cur.execute(repstr)
            rep_record = cur.fetchall()
            if len(rep_record) > 0:
                arritem["F"] = rep_record[0][1]
            newarr.append(arritem)

        newarrT = []
        ss = 0
        for arritem  in newarr:
            nostr = "SELECT material_mode from non_electronic_materials where material_mode =" + "'" + arritem[
                "F"] + "'"
            cur.execute(nostr)
            rep_record = cur.fetchall()
            if len(rep_record) > 0:
                ss = ss + 1
                continue
            newarrT.append(arritem)

        newarrS = []
        for arritem in newarrT:
            flag = False
            print(len(newarrS))
            for newitem in newarrS:
                if arritem["A"] == newitem["A"] and arritem["B"] == newitem["B"] and arritem["C"] == newitem["C"] and arritem["D"] == newitem["D"] and arritem["E"] == newitem["E"] and arritem["F"] == newitem["F"] and arritem["G"] == newitem["G"] and arritem["I"] == newitem["I"] and arritem["J"] == newitem["J"] and arritem["K"] == newitem["K"] and arritem["L"] == newitem["L"] and arritem["M"] == newitem["M"]:
                        flag = True
            if flag:
                continue
            countq = 0
            for itm in newarrT:
                if arritem["A"] == itm["A"] and arritem["B"] == itm["B"] and arritem["C"] == itm["C"] and arritem["D"] == itm["D"] and arritem["E"] == itm["E"] and arritem["F"] == itm["F"] and arritem["G"] == itm["G"]  and arritem["I"] == itm["I"] and arritem["J"] == itm["J"] and arritem["K"] == itm["K"] and arritem["L"] == itm["L"] and arritem["M"] == itm["M"] :
                    countq =countq + itm["H"]
            arritem["H"] = countq
            newarrS.append(arritem)
        for arritem in newarrS:
            worksheet1.write('A' + str(i), arritem["A"])
            worksheet1.write('B' + str(i), arritem["B"])
            worksheet1.write('C' + str(i), arritem["C"])
            worksheet1.write('D' + str(i), arritem["D"])
            worksheet1.write('E' + str(i), arritem["E"])
            worksheet1.write('F' + str(i), arritem["F"])
            worksheet1.write('G' + str(i), arritem["G"])
            worksheet1.write('H' + str(i), arritem["H"])
            worksheet1.write('I' + str(i), arritem["I"])
            worksheet1.write('J' + str(i), arritem["J"])
            worksheet1.write('K' + str(i), arritem["K"])
            worksheet1.write('L' + str(i), arritem["L"])
            worksheet1.write('M' + str(i), arritem["M"])
            i = i + 1
        print("非电子物料"+str(ss))
        workbook.close()

    @BeautifulReport.add_test_img("testQutoLogin_008")
    def testQutoLogin_008(self):
        """测试正常登录首页是否正常打开"""
        headers = {"Content-Type": "application/json;charset=UTF-8",
                   "Cookie": "session_id=46cfc05fb7b3bfe165238f0fc366c45a18c8a5fc"}
        params = {"jsonrpc":"2.0","method":"call",
                  "params":{"model":"complete.machine.wizard","domain":[],
                            "limit":12222225,"sort":"","context":{"lang":"zh_CN","tz":"Asia/Shanghai","uid":591,"allowed_company_ids":[1]}},"id":288025188}
        response = requests.get("http://10.3.70.154:7888/web/dataset/search_read", headers=headers,
                                data=json.dumps(params))
        response = response.text
        response = json.loads(response)
        result = response["result"]
        records = result["records"]

        workbook = xw.Workbook("E:\\Desktop\\sy.xlsx")  # 创建工作簿
        worksheet1 = workbook.add_worksheet("sheet1")  # 创建子表
        worksheet1.activate()  # 激活表

        rowcount = 1
        for record in records:
            if rowcount == 13821:
                print(1)
            value_list = list(record.values())
            worksheet1.write_row("A"+ str(rowcount),value_list)
            rowcount = rowcount + 1
            print(rowcount)
        workbook.close()
        print(123)

    @BeautifulReport.add_test_img("testQutoLogin_009")
    def testQutoLogin_009(self):
        m = 100
        month=12
        sumk =0
        count =0
        i=1
        year =2023
        mm=2
        while i <= month:
            day =  calendar._monthlen(2023,1)
            count = count + m
            sumk =sumk +  count*day

        print(count)
        print(sumk)

    @BeautifulReport.add_test_img("testQutoLogin_010")
    def testQutoLogin_010(self):
        data_list = []
        d = datetime.datetime.now()
        date_now = datetime.datetime(d.year, d.month, 1, 0, 0, 0)
        # pre_month = datetime.datetime.strptime(str(d.year) + '-' + str(d.month + 3), "%Y-%m") - datetime.timedelta(
        #     days=1)
        month = d.month - 1 + 2
        year = d.year + month // 12
        month = month % 12 + 1
        day = calendar.monthrange(year, month)[1]
        date_futer = datetime.datetime(year, month, day, 23, 59, 59)
        for i in range(1):
            dayscount = datetime.timedelta(days=d.day)
            dayto = d - dayscount
            date_to = datetime.datetime(dayto.year, dayto.month, dayto.day, 23, 59, 59)
            d = dayto
        for i in range(5):
            dayscount = datetime.timedelta(days=d.day)
            dayto = d - dayscount
            date_from = datetime.datetime(dayto.year, dayto.month, 1, 0, 0, 0)
            d = dayto
        data_list.append(date_from)
        data_list.append(date_to)
        data_list.append(date_now)
        data_list.append(date_futer)


    def tearDown(self):
        global num
        num=num+1
        if num>=10:
            fangfa='testQutoLogin_0'+str(num)
            xx=getattr(Test_order_info_query(),fangfa)
            self.log =xx.__doc__
        elif num<10:
            fangfa='testQutoLogin_00'+str(num)
            xx = getattr(Test_order_info_query(), fangfa)
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
        TestCase = unittest.defaultTestLoader.getTestCaseNames(Test_order_info_query)
        if num == len(TestCase):
            self.BL.quit()
        else:
            sleep(2)
            self.BL.driver.refresh()

    def list2reason(self, exc_list):
        if exc_list and exc_list[-1][0] is self:
            return exc_list[-1][1]

