from Public.pages.BasePage import BasePage
from time import sleep
from Public.common import DoExcel

class OdooHomePage(BasePage):
    url = DoExcel.File_Location().get_parameter("中国站地址")
    home = ("xpath", "//*[@id='app']/div/form/div[1]/div/div/input")
    home_ele=("xpath", "//*[@id='app']/div/form/div[2]/div/div/input")
    #
    # platformservice = ("xpath", "/html/body/div[1]/div[2]/ul/li[2]/a/span/")
    # platformservice_exp=("xpath", "/html/body/div[2]/div")
    #
    # customercase = ("xpath", "/html/body/div[1]/div[2]/ul/li[3]/a/span")
    # customercase_exp=("xpath", "/html/body/div[1]/div[2]/div")
    #
    # memberbenefits = ("xpath", "/html/body/div[1]/div[2]/ul/li[4]/a/span")
    # memberbenefits_exp=("xpath", "/html/body/div[2]/div/span")
    #
    # exhibition = ("xpath", "/html/body/div[1]/div[2]/ul/li[5]/a/span")
    # exhibition_exp = ("xpath", "/html/body/div[2]/div/span")
    #
    # news = ("xpath", "/html/body/div[1]/div[2]/ul/li[6]/a/span")
    # news_exp = ("xpath", "/html/body/div[2]/div/span")
    #
    # aboutus = ("xpath", "/html/body/div[1]/div[2]/ul/li[7]/a/span")
    # aboutus_ele = ("xpath", "/html/body/div[1]/div[2]/div/a")
    #
    # login_rukou = ("xpath", "//*[@id='loginAndRegister']/div[1]/a")
    # email_input = ("xpath", "//*[@id='username']")
    # password_input = ("xpath", "//*[@id='password']")
    # login_btn = ("xpath", "//*[@id='loginForm']/div/div[5]/div/button")
    # touxiang = ("xpath", "//*[@id='userLogo']")
    # nicheng = ("xpath", "//*[@id='username']")