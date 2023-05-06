from Public.pages.BasePage import BasePage
from time import sleep
import json,redis
from Public.common import DoExcel

class BCMLoginPage(BasePage):


    itcode = ("xpath", "//*[@id='login']")
    itpw = ("xpath", "//*[@id='password']")
    loginButton = ("xpath","/html/body/div/main/div/div/div/form/div[3]/button")

    def BCMLogin(self,username,password):
        Username=self.findElement(self.itcode)
        self.type(Username,username)
        Password=self.findElement(self.itpw)
        self.type(Password,password)
        self.click(self.findElement(self.loginButton))
