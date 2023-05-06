from Public.common import DoExcel
import xlrd
WindowsBL = ''
Cookies = DoExcel.File_Location().get_parameter("cookies",User_Table ="登录信息")
headers = {"Content-Type": "application/json;charset=UTF-8", "Cookie": "session_id=" + Cookies}
citys = ["大连","深圳","石家庄","佛山","天津","杭州","阿克苏","海口","厦门","哈尔滨","西宁","成都","南京","广州","济南","兰州",
        "合肥","长春","郑州","福州","西安","重庆","北京","乌鲁木齐","呼和浩特","贵阳","武汉项目","银川","沈阳","烟台","昆明","汕头","上海",
        "肇庆","太原","待定","东莞","宁波","南宁"]
#系统登录信息#
url = DoExcel.File_Location().get_parameter("登录地址",User_Table ="登录信息")
itcode = DoExcel.File_Location().get_parameter("账号",User_Table ="登录信息")
itpw = DoExcel.File_Location().get_parameter("密码",User_Table ="登录信息")
uid = DoExcel.File_Location().get_parameter("uid",User_Table ="登录信息")

#pgsql连接信息#
dbname = DoExcel.File_Location().get_parameter("dbname",User_Table ="数据库")
user = DoExcel.File_Location().get_parameter("user",User_Table ="数据库")
password = DoExcel.File_Location().get_parameter("password",User_Table ="数据库")
host = DoExcel.File_Location().get_parameter("host",User_Table ="数据库")
port = DoExcel.File_Location().get_parameter("port",User_Table ="数据库")

#bi连接信息#
biport = DoExcel.File_Location().get_parameter("port",User_Table ="bi")
bihost = DoExcel.File_Location().get_parameter("host",User_Table ="bi")
bifw = DoExcel.File_Location().get_parameter("fw",User_Table ="bi")
biuser = DoExcel.File_Location().get_parameter("user",User_Table ="bi")
bipw = DoExcel.File_Location().get_parameter("pw",User_Table ="bi")


def __init__(self):
    self.WindowsBL = ''

def set_WindowsBL(BL):
    global WindowsBL
    WindowsBL = BL

def set_Cookies(cookies):
    global Cookies
    global headers
    Cookies = cookies
    headers = {"Content-Type": "application/json;charset=UTF-8",
               "Cookie": "session_id=" + Cookies}

def get_TestCases():
    global  testcases
    testcases = DoExcel.File_Location().get_BySheet(User_Table ="testcase")
    testcases.sort(key=lambda all_lists: all_lists[1])
    new_testcases=[]
    for testcase in testcases:
        if testcase[3] ==1:
            new_test =[testcase[0],testcase[2]]
            new_testcases.append(new_test)
    return new_testcases