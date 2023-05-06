import xlrd
import os
import xlwt
from xlutils.copy import copy
class File_Location():

	def file_path(self,folder):
		#当前所在目录的上上一级
		Based_Dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
		file_path = os.path.join(Based_Dir,folder)
		return file_path

	def get_latest_file(self,File_Folder):

		result_dir = File_Folder
		lists = os.listdir(result_dir)
		lists.sort(key=lambda fn: os.path.getmtime(result_dir+Symbol+fn) if not os.path.isdir(result_dir+Symbol+fn) else 0)
		get_Latest_file = os.path.join(result_dir,lists[-1])
		return get_Latest_file

	# def get_build(self,url = "http://www.daboowifi.com/web/intro/index",Build_Location = file_path('self',"Data"+Symbol)):
	#
	# 	html = urllib2.urlopen(url).read()
	# 	reg = r"(http.*?\.apk)" #创建搜索规则
	# 	apkre = re.compile(reg)
	# 	apk_addr = re.findall(apkre,html)#得到的是一个列表，需要进行切片操作得到地址
	# 	apk_name = apk_addr[0]
	# 	#print '[信息:]已连接到下载服务器，请耐心等待下载完成.'
	#  	#urllib.urlretrieve(apk_addr[0], Build_Location+apk_name[32:]) #下载地址 和 下载后的路径与命名
	# 	#print '[信息:]成功下载当前线上最新版本程序.'
	#  	#return Build_Location+apk_name[32:]

	def get_parameter(self,Name,location = 1 ,User_Table = 'Login',File_location = file_path('self',"Data/TestData/"+"Test_Config.xlsx")):

		wb = xlrd.open_workbook(File_location)
		sh = wb.sheet_by_name(User_Table)

		for row in range(0,sh.nrows):
			rowValuelist = sh.row_values(row)
			if Name in rowValuelist:
				value = rowValuelist[(rowValuelist.index(Name)+location)]
				if type(value) is float:
					get_value = str(value)
					start_index = get_value.find('.')
					get_value_after_potin = get_value[start_index :]
					verify_less_than_zero = float(get_value_after_potin)
					if verify_less_than_zero > 0:
						return str(value)
					else:
						return int(value)
				else:
					return str(value)

	def get_all_cases(self,case_name):

		wb = xlrd.open_workbook(File_Location().file_path("02-Test_Data"+Symbol+"Test_Config2.xlsx"))
		sh = wb.sheet_by_name(case_name)
		#获取第一行的case数量
		global Cases
		Cases = len([cases for cases in sh.row_values(0) if "Test_Case_" in cases])
		return Cases

	def get_index(self,string,start,end):

		start_index = string.find(start)
		end_index = string.find(end)
		return string[start_index+1 :end_index]

# test=File_Location().get_parameter("OKCHEM卖家密码")
# print(test)
#通过excel数据进行驱动测试
class ReadExcel():
    def __init__(self,filename,sheetname):
        self.workbook=xlrd.open_workbook(filename)
        self.sheetName=self.workbook.sheet_by_name(sheetname)

    #获取某个单元格的内容
    def read_excel(self,rownum,colnum):
        value=self.sheetName.cell(rownum,colnum).value
        return value

    def total_row_num(self):
        return  self.sheetName.nrows

    def total_col_num(self):
        return  self.sheetName.ncols

#调试一下
filename="C:\\Users\\20073\\Desktop\\RPA_AA\\Desktop\\新员工信息表.xls"
sheetname="新员工信息表"
#打开指定Excel
data=xlrd.open_workbook(filename)
#通过名称获取工作表
table1=data.sheet_by_name(sheetname)
#获取类别标签所在列的内容
category=table1.col_values(9,1,table1.nrows)
#找到列值为“作业员”对应的行索引
category_list=[]
for index,value in enumerate(category):
    #print("索引："+str(index),"，值："+value)
    #判断是作业员的列数据
    if value=="作业员":
        category_list.append(index)
row_list=[]
for row_index in category_list:
    #判断预订入社时间
    if table1.row_values(row_index)[6]==44031.0:
        #组合需要的数据
        laowusuo=table1.row_values(row_index)[8]
        print(table1.row_values(row_index)[1:7])
        row_list.append(table1.row_values(row_index)[1:7]+[laowusuo])
print(row_list)
filename1="C:\\Users\\20073\\Desktop\\RPA_AA\\Desktop\\Omron\\Report\\作业员入社名单（人事）.xlsx"
data1=xlrd.open_workbook(filename1)
table1=data1.sheet_by_name('Sheet1')
newdata=copy(data1)
# for i in range(len(row_list)):
#
