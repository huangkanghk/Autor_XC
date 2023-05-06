from builtins import str
from run import *
import xc_common
import psycopg2,requests,json
import datetime
import cx_Oracle,random

num = 0
class TestSupplyDemandMatchingQuery(unittest.TestCase):

    def setUp(self):
        BL = xc_common.WindowsBL

    @BeautifulReport.add_test_img("testSupplyDemandMatchingQuery_001")
    def testSupplyDemandMatchingQuery_001(self):
        """订单-信息查询-供需匹配模 核对全部数据"""
        conn = psycopg2.connect(dbname=xc_common.dbname, user=xc_common.user,
                                password=xc_common.password, host=xc_common.host,
                                port=xc_common.port)
        cur = conn.cursor();
        cur.execute("SELECT sap_no,material_desc FROM material material ")
        rows = cur.fetchall()
        rows = random.sample(rows,3)

        rq = datetime.datetime.now().strftime("%Y-%m-%d")
        conn_str = xc_common.biuser + "/" + xc_common.bipw + "@" + xc_common.bihost + ":" + str(
            xc_common.biport) + "/" + xc_common.bifw
        connection_oracle = cx_Oracle.Connection(conn_str)
        cursor_oracle = connection_oracle.cursor()

        # 查询需求#
        xq_sql = "SELECT to_char(A.billing_time,'yyyy-mm-dd') rq,C.sap_no,m.material_desc,a.crm_no,a.proj_name,SUM( C.material_total ) xqsl FROM order_quotation A,order_quotation_product b,order_material C,material m  WHERE A.crm_no IS NOT NULL 	AND A.ID = b.quot_id 	AND b.ID = C.prod_id 	AND ( A.order_status IS NULL OR A.order_status = '0' ) 	AND ( A.proj_status != '输单' OR A.proj_status IS NULL ) and m.sap_no = c.sap_no "
        xq_sql = xq_sql + " GROUP BY C.sap_no,m.material_desc,A.billing_time,a.crm_no,a.proj_name"
        cur.execute(xq_sql)
        xq_Datas = cur.fetchall()

        #查询库存#
        sql = "SELECT SAP_NO, material_desc,SL FROM ( SELECT a.sap_no,A.material_desc, COALESCE((SELECT sum(quantity) kc from dos_wms_data  d where d.sap_no in (SELECT mi2.sap_no sap_no302 FROM quotation_product_rel qp,material mi,material mi2 WHERE qp.mid = mi.ID AND qp.rid = mi2.ID and mi.sap_no =a.sap_no ) ),0) sl from  material  a where sap_no like '69-%' union all SELECT a.sap_no ,A.material_desc,(SELECT sum(quantity) kc from dos_wms_data  d where d.sap_no =a.sap_no) SL from  material  a where sap_no not like '69-%' ) AS KK where 1= 1"
        cur.execute(sql)
        kc_Data = cur.fetchall()

        #查询bi#
        query = f"""SELECT
                                            JHDHRQ opo_date,
                                            cast(cast(substr(WLDM,1,12) as NUMBER) as varchar2(3)) || '-' || substr(WLDM,-6) sap_no,
                                            CGDDDM order_no,
                                            GYSMC order_name,
                                            SUM( SL ) quantity
                                        FROM
                                            DCDWS.VW_DCN_CGMX
                                        WHERE
                                            1 =1
                                            AND ZT = '未清'
                                            AND JHDHRQ > TO_DATE('{rq}'  ,'YYYY-MM-DD')
                                        GROUP BY
                                            WLDM,
                                            JHDHRQ,
                                            CGDDDM,
                                            GYSMC"""
        cursor_oracle.execute(query)
        records_bi = cursor_oracle.fetchall()

        count = 0
        for row in rows:
            count = count + 1
            print(count)
            params = {"params": {"model": "order.supply.demand.matching.query","domain": [["sap_no", "=", row[0]]],"limit": 10000}}
            response = requests.get(xc_common.url + "/web/dataset/search_read", headers=xc_common.headers, data=json.dumps(params))
            response = response.text
            response = json.loads(response)
            result = response["result"]
            records = result["records"]
            table_datas = []
            for record in records:
                for tab in record:
                    if record[tab] is None:
                        record[tab] =''
                table_data = [record['category'],record['opo_date'],record['sap_no'],record['desc'],
                              record['order_no'],record['order_name'],record['quantity'],record['margin']]
                table_datas.append(table_data)

            search_list = []
            kc_temp = []
            kc = 0
            for kc_item in kc_Data:
                if kc_item[0] == row[0]:
                    sap_no = kc_item[0]
                    kc = kc_item[2]
                    if kc_item[2] == None:
                        kc = 0
                    kc_list = ["库存", rq, sap_no, kc_item[1], '', '', kc,kc]
                    search_list.append(kc_list)
                else:
                    kc_temp.append(kc_item)
            kc_Data = kc_temp

            gy_lists = []
            xq_temp =  []
            for xq_Data in xq_Datas:
                if row[0] == xq_Data[1]:
                    xq_list = kc_list = ["需求", xq_Data[0], xq_Data[1], xq_Data[2], xq_Data[3], xq_Data[4], xq_Data[5]]
                    gy_lists.append(xq_list)
                else:
                    xq_temp.append(xq_Data)
            xq_Datas = xq_temp

            # 查询bi供应 #
            bi_temp = []
            if "69-" not in row[0] or "80-" not in row[0]:
                for record_bi in records_bi:
                    if record_bi[1] == row[0]:
                        record_date = record_bi[0]
                        record_date = record_date.strftime('%Y-%m-%d')
                        gy_list = ["供应", record_date, record_bi[1], row[1], str(record_bi[2]), record_bi[3], record_bi[4]]
                        gy_lists.append(gy_list)
                    else:
                        bi_temp.append(record_bi)
            records_bi = bi_temp

            if len(gy_lists) > 0:
                gy_lists.sort(key=lambda all_lists: (all_lists[1],all_lists[4]))
            for gy_list in gy_lists:
                if gy_list[0] == '需求':
                    gy_list[6] = -1 * gy_list[6]
                gy_list.append(kc + gy_list[6])
                kc = kc + gy_list[6]
                search_list.append(gy_list)

            if len(search_list) != len(table_datas):
                raise Exception(row[0] + "物料核对信息错误")
            for search in search_list:
                if search not in table_datas:
                    raise Exception(row[0] + "物料核对信息错误")
        print("结束")
        conn.close()

    def tearDown(self):
        global num
        num=num+1
        if num>=10:
            fangfa='testSupplyDemandMatchingQuery_0'+str(num)
            xx=getattr(TestSupplyDemandMatchingQuery(),fangfa)
            self.log =xx.__doc__
        elif num<10:
            fangfa='testSupplyDemandMatchingQuery_00'+str(num)
            xx = getattr(TestSupplyDemandMatchingQuery(), fangfa)
            self.log= xx.__doc__
        result = self.defaultTestResult()
        self._feedErrorsToResult(result, self._outcome.errors)

    def list2reason(self, exc_list):
        if exc_list and exc_list[-1][0] is self:
            return exc_list[-1][1]

