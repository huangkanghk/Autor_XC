import os
#from Public.common.ReadConfigIni import ReadConfigIni

#获取工程目录
project_path=os.path.dirname(os.path.dirname(__file__))

#获取config.ini的路径
file_path=os.path.split(os.path.realpath(__file__))[0]


#读取配置文件
read_config=os.path.join(project_path,"config.ini")
#read_config=ReadConfigIni(os.path.join(file_path,"config.ini"))
# print(read_config)

#借助config.ini获取项目参数
#project_path=os.path.join(project_path,"project_path")
#project_path=read_config.getConfigValue("project","project_path")
# print(project_path)

#日志路径
log_path=os.path.join(project_path,"report","Log")
# print(log_path)

#测试用例路径
TestCase_path=os.path.join(project_path,"TestCase")
#TestCase_path=os.path.join(project_path,"TestCase")

#测试报告路径
report_path=os.path.join(project_path,"Data","ReportResult")

#测试数据路径
data_path=os.path.join(project_path,"Data","TestData","BCM_data.xls")

#测试截图路径
picture_path=os.path.join(project_path,"report","Screenshot")

#测试截图路径--BeautifulReport
picture_path1=os.path.join(project_path,"img")