from BeautifulReport import BeautifulReport
import unittest
# from TestCase import TC_OkchemLogin,TC_OkchemSearch,TC_OkchemHome
import time,os
from config import globalconfig
from Public.common import send_mail as cc
# from tomorrow import threads
import  xc_common
#测试报告路径
report_path=globalconfig.report_path
#测试用例路径
TestCase_path=globalconfig.TestCase_path
#测试日志目录
Log_path=globalconfig.log_path

def AutoRun_ALL():
    """
    执行所有TC_开头的测试用例,并发送邮件
    """
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = now + "result"  # 拼接出测试报告的名称
    test_suite = unittest.defaultTestLoader.discover(TestCase_path, pattern='TC*.py')
    result = BeautifulReport(test_suite)
    result.report(filename=filename, description='线上环境自动化测试报告', log_path=report_path)
    fail_count=result.failure_count
    pass_count=result.success_count
    skipped_count=result.skipped

    if fail_count>=1:
        sendEmail = cc.Email()
        new_report = sendEmail.newReport(report_path)  # 在测试报告目录获取最新的测试报告
        #sendEmail.email_Attach(pass_count, fail_count, skipped_count, new_report, "自动化测试报告")
        os.remove(new_report)
    else:
        sendEmail = cc.Email()
        new_report = sendEmail.newReport(report_path)
        os.remove(new_report)

    # #如果操作系统是linux执行如下命令
    # if os.name=="posix":
    #     os.system("pkill -9 firefox")

def AutoRun_Single(TestCaseName):
    """
    执行单个测试用例,,并发送邮件,参数："TC_OkchemLogin.py"
    """
    #加载单个测试文件
    discover=unittest.defaultTestLoader.discover(TestCase_path,pattern=TestCaseName)

    now=time.strftime("%Y-%m-%d %H_%M_%S")#获取当前系统时间
    filename=now+"result"#拼接出测试报告的名称
    result = BeautifulReport(discover)
    result.report(filename=filename, description='线上环境自动化测试报告', report_dir='E:\BaiduNetdiskDownload\AutoRunFrame\Data\ReportResult',log_path=report_path)
    fail_count=result.failure_count
    pass_count=result.success_count
    skipped_count=result.skipped

    if fail_count>=1:
        sendEmail = cc.Email()
        new_report = sendEmail.newReport(report_path)  # 在测试报告目录获取最新的测试报告
        sendEmail.email_Attach(pass_count, fail_count, skipped_count, new_report, "信创报价系统自动化测试报告")
        #os.remove(new_report)
    else:
        sendEmail = cc.Email()
        new_report = sendEmail.newReport(report_path)
        sendEmail.email_Attach(pass_count, fail_count, skipped_count, new_report, "自动化测试报告")
        #os.remove(new_report)
    #如果操作系统是linux执行如下命令
    if os.name=="posix":
        os.system("pkill -9 firefox")

def AutoRun_Multi(TestCaseNames):
    """
    执行多个测试用例,,并发送邮件,参数样例：[TC_OkchemLogin,TC_OkchemS]
    """
    now = time.strftime("BCM自动化测试报告""%Y-%m-%d %H_%M_%S")  # 获取当前系统时间
    filename = now + "result"  # 拼接出测试报告的名称

    fail_count = 0
    pass_count = 0
    skipped_count = 0
    discover = unittest.TestSuite()
    for TestCaseName in TestCaseNames:
        TestCaseN = TestCaseName[0]
        TestCase_pathN = TestCase_path +"//"+ TestCaseName[1]
        discover.addTest(unittest.defaultTestLoader.discover(TestCase_pathN, pattern=TestCaseN,top_level_dir=TestCase_pathN))
    result = BeautifulReport(discover)
    result.report(filename=filename, description='BCM自动化测试报告', report_dir=report_path,log_path=Log_path)
    fail_count = fail_count + result.failure_count
    pass_count = pass_count + result.success_count
    skipped_count = skipped_count + result.skipped

    # sendEmail = cc.Email()
    # new_report = sendEmail.newReport(report_path)
    # new_reports = []
    # new_reports.append(new_report)
    # sendEmail.email_Attach(pass_count, fail_count, skipped_count, new_report, "自动化测试报告")

    #如果操作系统是linux执行如下命令
    if os.name=="posix":
        os.system("pkill -9 firefox")

def AutoRun_Part(TestCaseList):
    """
    执行部分测试用例,需要先导入对应的测试用例Py文件，列表参数样例：[TC_OkchemLogin.TestOkchemLogin，TC_OkchemS.XX]
    """
    testunit = unittest.TestSuite()
    for i in range(0,len(TestCaseList)):
        testunit.addTest(unittest.makeSuite(TestCaseList[i]))

    now=time.strftime("%Y-%m-%d %H_%M_%S")#获取当前系统时间
    filename=now+"result"#拼接出测试报告的名称

    result = BeautifulReport(testunit)
    result.report(filename=filename, description='线上环境自动化测试报告', log_path=report_path)
    fail_count = result.failure_count
    pass_count = result.success_count
    skipped_count = result.skipped

    if fail_count>=1:
        sendEmail = cc.Email()
        new_report = sendEmail.newReport(report_path)  # 在测试报告目录获取最新的测试报告
        sendEmail.email_Attach(pass_count, fail_count, skipped_count, new_report, "自动化测试报告")
        os.remove(new_report)
    else:
        sendEmail = cc.Email()
        new_report = sendEmail.newReport(report_path)
        os.remove(new_report)
    #如果操作系统是linux执行如下命令
    if os.name=="posix":
        os.system("pkill -9 firefox")

#多线程执行测试用例
# def add_case(case_path=TestCase_path,rule="TC*.py"):
#     discover=unittest.defaultTestLoader.discover(case_path, pattern=rule,top_level_dir=None)
#     return discover
#
# @threads(20)
# def run(testsuit):
#     result=BeautifulReport(testsuit)
#     result.report(filename="report.html", description='线上环境自动化测试报告', log_path=report_path)


if __name__=="__main__":
    #AutoRun_Part([TC_OkchemLogin.TestOkchemLogin,TC_OkchemSearch.TestOkchemSearch])
    #AutoRun_Single("TC_OdooHome.py")
    # AutoRun_Single("TC_QutoManage.py")
    # AutoRun_Multi(["TC_QutoManage.py"])
    #AutoRun_Multi(["TC_QutoLogin.py","TC_QutoHome.py","TC_QutoManage.py"])
    #AutoRun_Multi(["TC_QutoLogin.py"])
    #AutoRun_Multi("TC_BCM_Login.py")
    tests = xc_common.get_TestCases()
    AutoRun_Multi(tests)
    #AutoRun_Multi(["TC_BCM_Login.py","TC_Supply_Demand_Matching_Query.py"])
    #AutoRun_Multi(["TC_BCM_Login.py"])
    #AutoRun_ALL()
    # #多线程
    # cases=add_case()
    # for i in cases:
    #     run(i)
    # suit = unittest.TestSuite()
    # suit.addTest(TC_OkchemHome.TestOkchemHome("testOkchemHome_024"))
    # suit.addTest(TC_OkchemHome.TestOkchemHome("testOkchemHome_025"))
    # runner = unittest.TextTestRunner()
    # runner.run(suit)
    # while True:
    #     suit = unittest.TestSuite()
    #     suit.addTest(TC_OkchemHome.TestOkchemHome("testOkchemHome_030"))
    #     runner = unittest.TextTestRunner()
    #     runner.run(suit)