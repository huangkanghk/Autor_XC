from Public.pages.BasePage import BasePage
from time import sleep
import json,redis
from Public.common import DoExcel

class QutoLoginPage(BasePage):

    title = ("TAG_NAME", "title")
    text = ("xpath", "//*[@id='app']/div/form/h3")
    loginName =  ("xpath", "//*[@id='app']/div/form/div[1]/div/div/input")
    userID = ("xpath", "//*[@id='0']/a")
    pw = ("xpath", "/html/body/div[2]/div/div[1]/div[1]/div[2]/div/div/div/input")
    table =("class","o_data_row")
    vcodeInput = ("xpath", "//*[@id='app']/div/form/div[3]/div/div[1]/input")
    vcodeImg = ("xpath","//*[@id='app']/div/form/div[3]/div/div[2]/img")
    loginButton = ("xpath", "//*[@id='app']/div/form/div[4]/div/button")
    tip =  ("xpath", "//*[@id='app']/div/form/span")

     #提示信息
    userTip = ("xpath", "//*[@id='app']/div/form/div[1]/div/div[2]")
    pwTip = ("xpath", "//*[@id='app']/div/form/div[2]/div/div[2]")
    vcodeTip = ("xpath", "//*[@id='app']/div/form/div[3]/div/div[3]")

    #底部日期信息
    tdate = ("xpath","//*[@id='app']/div/div[1]/span")

    #登录错误提示信息
    vcoedError = ("xpath","/html/body/div[2]/p")

    homeName = ("xpath", "//*[@id='breadcrumb-container']/span/span/span[1]/span")

    def QutoLogin(self,username,password):

        Username=self.findElement(self.loginName)
        self.type(Username,username)
        Password=self.findElement(self.pw)
        self.type(Password,password)
        self.click(self.findElement(self.loginButton))
