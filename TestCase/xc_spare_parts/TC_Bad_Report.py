from builtins import str

import platform
from time import sleep
from run import *
from Public.common import send_mail as dd
import xc_common
import psycopg2,requests,json
from datetime import datetime
import math
import cx_Oracle
from itertools import  combinations

num =0
conn = psycopg2.connect(dbname=xc_common.dbname, user=xc_common.user, password=xc_common.password, host=xc_common.host, port=xc_common.port)
cur = conn.cursor();


class TestBadReport(unittest.TestCase):

    def setUp(self):
        BL = xc_common.WindowsBL

    @BeautifulReport.add_test_img("testBadReport_001")
    def testBadReport_001(self):
        """ 【备件测算--不良率】 页面数据校验 """
        params = {"params": {"model": "network.bad.report","domain":[], "limit": 999999},"context":{"params": {"model": "network.bad.report"}}}
        response = requests.get(xc_common.url + "/web/dataset/search_read", headers=xc_common.headers,
                                data=json.dumps(params))
        response = response.text
        response = json.loads(response)
        result = response["result"]
        bad_records = result["records"]

        sapstr = f"""SELECT DISTINCT material_code,version  from network_product_repair_details"""
        cur.execute(sapstr)
        all_records = cur.fetchall()

        conn_str = xc_common.biuser + "/" + xc_common.bipw + "@" + xc_common.bihost + ":" + str(
            xc_common.biport) + "/" + xc_common.bifw
        connection_oracle = cx_Oracle.Connection(conn_str)
        cursor_oracle = connection_oracle.cursor()
        query1 = f""" SELECT sum(sl),WLDM,year from DCDWS.VW_DCN_XSMXHB where 1=1  GROUP BY WLDM,year"""
        query2 = f"""SELECT  sum(sl),WLDM,CJFPRQ  from DCDWS.VW_DCN_XSMX where 1=1  GROUP BY WLDM,CJFPRQ"""
        cursor_oracle.execute(query1)
        sale_XSMXHB = cursor_oracle.fetchall()
        cursor_oracle.execute(query2)
        sale_XSMX = cursor_oracle.fetchall()

        now = datetime.now()

        new_list = []
        for all_record in all_records:
            print(all_record[0])
            count = 1
            year = now.year

            sum_bad =0
            sum_sale = 0
            sum_real_bad_rate = 0
            sum_bad_rate_compared = "低"
            supplier_theory_rate = "1.00%"
            supplier_theory_rate1 = supplier_theory_rate[0:-1]
            sum_real_repair_year_1 = 0
            sum_real_repair_year_2 = 0
            sum_real_repair_year_3 = 0
            sum_real_repair_year_4 = 0
            sum_real_repair_year_5 = 0
            sum_real_repair_year_6 = 0
            sum_real_repair_year_7 = 0
            sum_real_repair_year_8 = 0

            sum_real_repair_rate_year_1  = "0.00%"
            sum_real_repair_rate_year_2  = "0.00%"
            sum_real_repair_rate_year_3  = "0.00%"
            sum_real_repair_rate_year_4  = "0.00%"
            sum_real_repair_rate_year_5  = "0.00%"
            sum_real_repair_rate_year_6  = "0.00%"
            sum_real_repair_rate_year_7  = "0.00%"
            sum_real_repair_rate_year_8  = "0.00%"

            sum_three_year_avg = 0
            sum_four_five_year_avg = 0
            sum_six_seven_year_avg = 0

            device_model =""
            original_factory = ""
            product_line = ""
            sql = f""" SELECT  equipment_mode  ,factory,product_line from network_product_repair_details a where 
            material_code = '{all_record[0]}' and version = {all_record[1]}   LIMIT 1"""
            cur.execute(sql)
            material_record = cur.fetchall()
            material_record = material_record[0]
            if material_record[0] is not None:
                device_model = material_record[0]
            if material_record[1] is not None:
                original_factory = material_record[1]
            if material_record[2] is not None:
                product_line = material_record[2]
            while count <= 8:
                repair_amount = 0
                sale_amount = 0
                real_bad_rate = 0
                bad_rate_compared = "低"

                real_repair_rate_year_1 = "0.00%"
                real_repair_rate_year_2 = "0.00%"
                real_repair_rate_year_3 = "0.00%"
                real_repair_rate_year_4 = "0.00%"
                real_repair_rate_year_5 = "0.00%"
                real_repair_rate_year_6 = "0.00%"
                real_repair_rate_year_7 = "0.00%"
                real_repair_rate_year_8 = "0.00%"
                three_year_avg = 0
                four_five_year_avg = 0
                six_seven_year_avg = 0

                ## 查询报修量
                sqlcount = f""" SELECT  count(*),material_code,version,EXTRACT(YEAR FROM a.dcn_ship_date) from network_product_repair_details a where 
                material_code = '{all_record[0]}' and version = {all_record[1]}  and  EXTRACT(YEAR FROM a.dcn_ship_date)={year}   
                and  hand_method != '调试'
                GROUP BY  material_code,version,EXTRACT(YEAR FROM a.dcn_ship_date)"""
                cur.execute(sqlcount)
                count_ma= cur.fetchall()
                if len(count_ma) == 1:
                    count_ma = count_ma[0]
                    repair_amount = count_ma[0]

                ## 查询销量
                # if year <=2021:
                #     query =f""" SELECT sum(sl) from DCDWS.VW_DCN_XSMXHB where WLDM like  '%{all_record[0]}'
                #       and year like '{year}%' """
                # else:
                #     query = f"""SELECT  sum(sl)  from DCDWS.VW_DCN_XSMX where WLDM like '%{all_record[0]}' and CJFPRQ like '{year}%' """
                # cursor_oracle.execute(query)
                # sale_record = cursor_oracle.fetchall()
                # if len(sale_record) == 1:
                #     sale_record = sale_record[0]
                #     if sale_record[0] is not None:
                #         sale_amount = sale_record[0]
                if year <= 2021:
                    for xs in sale_XSMXHB:
                        if xs[2] == year:
                            len_str =len(xs[1])
                            if xs[2] in all_record[0][0,len_str]:
                                sale_amount = sale_amount + xs[0]
                else:
                    for xs in sale_XSMX:
                        if xs[2] == year:
                            len_str = len(xs[1])
                            if xs[2] in all_record[0][0, len_str]:
                                sale_amount = sale_amount + xs[0]

                if real_bad_rate > float(supplier_theory_rate1):
                    bad_rate_compared = "高"

                ## 8年报修量
                year1  = now.year
                count1 = 1
                year_c = []
                while count1 <= 8:
                    sum_count = 0
                    bad_sql =f""" SELECT  count(*), material_code,version ,EXTRACT(YEAR FROM dcn_ship_date) dcn_ship_date,
                    EXTRACT(YEAR FROM get_date)  get_date from network_product_repair_details a where 
                    material_code = '{all_record[0]}' and version = {all_record[1]}  and  EXTRACT(YEAR FROM dcn_ship_date)={year}  
                    and  EXTRACT(YEAR FROM get_date)={year1}    and  hand_method != '调试'
                    GROUP BY material_code,version,EXTRACT(YEAR FROM dcn_ship_date), EXTRACT(YEAR FROM get_date) """
                    cur.execute(bad_sql)
                    year_record = cur.fetchall()
                    if len(year_record) == 1:
                        year_record = year_record[0]
                        sum_count  = year_record[0]
                    year_c.append(sum_count)
                    year1 = year1 - 1
                    count1 = count1 + 1

                if sale_amount !=0:
                    real_bad_rate = round(repair_amount/sale_amount)*100
                    real_repair_rate_year_1 = round(year_c[7]/sale_amount)*100
                    real_repair_rate_year_2 = round(year_c[6] / sale_amount) * 100
                    real_repair_rate_year_3 = round(year_c[5] / sale_amount) * 100
                    real_repair_rate_year_4 = round(year_c[4] / sale_amount) * 100
                    real_repair_rate_year_5 = round(year_c[3] / sale_amount) * 100
                    real_repair_rate_year_6 = round(year_c[2] / sale_amount) * 100
                    real_repair_rate_year_7 = round(year_c[1] / sale_amount) * 100
                    real_repair_rate_year_8 = round(year_c[0] / sale_amount) * 100

                    three_year_avg = round((year_c[7] + year_c[6] + year_c[5]) / sale_amount) * 100
                    four_five_year_avg = round((year_c[4] + year_c[4] ) / sale_amount) * 100
                    six_seven_year_avg = round((year_c[3] + year_c[2] ) / sale_amount) * 100

                record ={
                    "material_code":all_record[0],
                    "device_model":material_record[0],
                    "version": all_record[1],
                    "original_factory":material_record[1],
                    "sale_year":str(year),
                    "product_line":material_record[2],
                    "repair_amount": repair_amount,
                    "sale_amount":sale_amount,
                    "real_bad_rate":real_bad_rate,
                    "supplier_theory_rate":supplier_theory_rate,
                    "bad_rate_compared":bad_rate_compared,
                    "real_repair_year_1": year_c[7],
                    "real_repair_year_2": year_c[6],
                    "real_repair_year_3": year_c[5],
                    "real_repair_year_4": year_c[4],
                    "real_repair_year_5": year_c[3],
                    "real_repair_year_6": year_c[2],
                    "real_repair_year_7": year_c[1],
                    "real_repair_year_8": year_c[0],
                    "real_repair_rate_year_1": str(real_repair_rate_year_1)+"%",
                    "real_repair_rate_year_2": str(real_repair_rate_year_2)+"%",
                    "real_repair_rate_year_3": str(real_repair_rate_year_3)+"%",
                    "real_repair_rate_year_4": str(real_repair_rate_year_4)+"%",
                    "real_repair_rate_year_5": str(real_repair_rate_year_5)+"%",
                    "real_repair_rate_year_6": str(real_repair_rate_year_6)+"%",
                    "real_repair_rate_year_7": str(real_repair_rate_year_7)+"%",
                    "real_repair_rate_year_8": str(real_repair_rate_year_8)+"%",
                    "three_year_avg":three_year_avg,
                    "four_five_year_avg": four_five_year_avg,
                    "six_seven_year_avg": six_seven_year_avg
                }
                new_list.append(record)
                year = year - 1
                count = count + 1
                sum_bad = sum_bad + repair_amount
                sum_sale= sum_sale + sale_amount

                sum_real_repair_year_1 = sum_real_repair_year_1 + year_c[7]
                sum_real_repair_year_2 = sum_real_repair_year_2 + year_c[6]
                sum_real_repair_year_3 = sum_real_repair_year_3 + year_c[5]
                sum_real_repair_year_4 = sum_real_repair_year_4 + year_c[4]
                sum_real_repair_year_5 = sum_real_repair_year_5 + year_c[3]
                sum_real_repair_year_6 = sum_real_repair_year_6 + year_c[2]
                sum_real_repair_year_7 = sum_real_repair_year_7 + year_c[1]
                sum_real_repair_year_8 = sum_real_repair_year_8 + year_c[0]

            if sum_sale != 0:
                sum_real_bad_rate = round(sum_bad / sum_sale)*100
                sum_real_repair_rate_year_1 =  round(sum_real_repair_year_1 / sum_sale)*100
                sum_real_repair_rate_year_2 = round(sum_real_repair_year_2 / sum_sale) * 100
                sum_real_repair_rate_year_3 = round(sum_real_repair_year_3 / sum_sale) * 100
                sum_real_repair_rate_year_4 = round(sum_real_repair_year_4 / sum_sale) * 100
                sum_real_repair_rate_year_5 = round(sum_real_repair_year_5 / sum_sale) * 100
                sum_real_repair_rate_year_6 = round(sum_real_repair_year_6 / sum_sale) * 100
                sum_real_repair_rate_year_7 = round(sum_real_repair_year_7 / sum_sale) * 100
                sum_real_repair_rate_year_8 = round(sum_real_repair_year_8 / sum_sale) * 100

                sum_three_year_avg = round((sum_real_repair_year_1 + sum_real_repair_year_2 + sum_real_repair_year_3) / sum_sale)*100
                sum_four_five_year_avg = round((sum_real_repair_year_4 + sum_real_repair_year_5 ) / sum_sale)*100
                sum_six_seven_year_avg = round((sum_real_repair_year_6 + sum_real_repair_year_7 ) / sum_sale)*100

            if sum_real_bad_rate > float(supplier_theory_rate1) * 100:
                sum_bad_rate_compared = "高"
            record = {
                "material_code":all_record[0],
                "device_model":device_model,
                "version": all_record[1],
                "original_factory":original_factory,
                "sale_year": "汇总",
                "product_line":product_line,
                "repair_amount": sum_bad,
                "sale_amount": sum_sale,
                "real_bad_rate":sum_real_bad_rate,
                "supplier_theory_rate": supplier_theory_rate,
                "sum_bad_rate_compared":sum_bad_rate_compared,
                "real_repair_year_1": sum_real_repair_year_1,
                "real_repair_year_2": sum_real_repair_year_2,
                "real_repair_year_3": sum_real_repair_year_3,
                "real_repair_year_4": sum_real_repair_year_4,
                "real_repair_year_5": sum_real_repair_year_5,
                "real_repair_year_6": sum_real_repair_year_6,
                "real_repair_year_7": sum_real_repair_year_7,
                "real_repair_year_8": sum_real_repair_year_8,
                "sum_real_repair_rate_year_1":str(sum_real_repair_rate_year_1)+"%",
                "sum_real_repair_rate_year_2": str(sum_real_repair_rate_year_2) + "%",
                "sum_real_repair_rate_year_3": str(sum_real_repair_rate_year_3) + "%",
                "sum_real_repair_rate_year_4": str(sum_real_repair_rate_year_4) + "%",
                "sum_real_repair_rate_year_5": str(sum_real_repair_rate_year_5) + "%",
                "sum_real_repair_rate_year_6": str(sum_real_repair_rate_year_6) + "%",
                "sum_real_repair_rate_year_7": str(sum_real_repair_rate_year_7) + "%",
                "sum_real_repair_rate_year_8": str(sum_real_repair_rate_year_8) + "%",
                "sum_three_year_avg":sum_three_year_avg,
                "sum_four_five_year_avg": sum_four_five_year_avg,
                "sum_six_seven_year_avg": sum_six_seven_year_avg
            }
            new_list.append(record)


        for list in new_list:
            count = 0
            for bad_record in bad_records:
                if list["material_code"] == bad_record["material_code"] and list["version"] == bad_record["version"] and list["sale_year"] == bad_record["sale_year"]:
                    if  list["repair_amount"] == bad_record["real_repair"]  or (list["repair_amount"] == 0 and bad_record["real_repair"] is None ):
                        if list["sale_amount"] == bad_record["sale_amount"]  and list["bad_rate_compared"] == bad_record["bad_rate_compared"] and list["real_bad_rate"] == bad_record["real_bad_rate"] :
                            if list["real_repair_year_1"] == bad_record["real_repair_year_1"]  and list["real_repair_year_2"] == bad_record["real_repair_year_2"] and list["real_repair_year_3"] == bad_record["real_repair_year_3"]  and list["real_repair_year_4"] == bad_record["real_repair_year_4"] and list["real_repair_year_5"] == bad_record["real_repair_year_5"] and list["real_repair_year_6"] == bad_record["real_repair_year_6"] and list["real_repair_year_7"] == bad_record["real_repair_year_7"] and list["real_repair_year_8"] == bad_record["real_repair_year_8"]:
                                count = count + 1
            if count != 1:
                raise Exception(list["material_code"] + "核对信息错误")

    def tearDown(self):
        global num
        num=num+1
        if num>=10:
            fangfa='testBadReport_0'+str(num)
            xx=getattr(TestBadReport(),fangfa)
            self.log =xx.__doc__
        elif num<10:
            fangfa='testBadReport_00'+str(num)
            xx = getattr(TestBadReport(), fangfa)
            self.log= xx.__doc__
        result = self.defaultTestResult()
        self._feedErrorsToResult(result, self._outcome.errors)
        error = self.list2reason(result.errors)
        failure = self.list2reason(result.failures)

    def list2reason(self, exc_list):
        if exc_list and exc_list[-1][0] is self:
            return exc_list[-1][1]