from selenium import webdriver
from time import sleep
from Public.pages.BasePage import BasePage

class OkchemLoginPage(BasePage):
    SignIn_LinkText=("link_text","Sign In")
    Username_Id=("id","username")
    Password_Id=("id","password")
    SignIn_Btn=("id","identification")
    ForgotPw_Link=("xpath",'//*[@id="loginForm"]/div[5]/a[1]')
    Register_Link = ("xpath",'//*[@id="loginForm"]/div[5]/a[2]')
    Logo_Image=("xpath","/html/body/section[1]/div/div/h1/a/img")
    Nicheng=("xpath","/html/body/header/div[1]/div/div[2]/p/a")
    Nicheng_mem = ("xpath", "/html/body/header/div[1]/div/div[2]/p/a")
    Forgotpw_title=("xpath","/html/body/section[2]/div/div/h3")
    Register_title = ("xpath", "/html/body/section[2]/div/h2")
    Home_category = ("xpath", "/html/body/header/div[2]/ul/li/a")

    def OkchemLogin(self,username,password):
        Login=self.findElement(self.SignIn_LinkText)
        self.click(Login)
        Username=self.findElement(self.Username_Id)
        self.type(Username,username)
        Password=self.findElement(self.Password_Id)
        self.type(Password,password)
        self.click(self.findElement(self.SignIn_Btn))

    def ClickFogotPassword(self):
        Login=self.findElement(self.SignIn_LinkText)
        self.click(Login)
        Forgotpassword=self.findElement(self.ForgotPw_Link)
        self.click(Forgotpassword)

    def ClickRegister(self):
        Login=self.findElement(self.SignIn_LinkText)
        self.click(Login)
        Register=self.findElement(self.Register_Link)
        self.click(Register)

    def ClickOkchemLogo(self):
        Login=self.findElement(self.SignIn_LinkText)
        self.click(Login)
        Okchemlogo=self.findElement(self.Logo_Image)
        self.click(Okchemlogo)
