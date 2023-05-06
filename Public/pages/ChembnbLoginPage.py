from Public.pages.BasePage import BasePage
from Public.common import DoExcel

class ChembnbLoginPage(BasePage):
    url = DoExcel.File_Location().get_parameter("Chembnb地址", User_Table="ChembnbLogin")
    SignIn_LinkText = ("link_text", "Sign In")
    Username_Id = ("id", "username")
    Password_Id = ("id", "password")
    SignIn_Btn = ("id", "btnSignup")
    BuyerLogin_exp= ("xpath", "//*[@id='navigation']/li[1]/a/span[2]")
    Register = ("xpath", "//*[@id='navigation']/li[2]/a")
    Register_exp = ("xpath", "//*[@id='content']/div/div/h3")
    Forgotpasswd = ("xpath", "//*[@id='loginForm']/div[2]/div/a")
    Forgotpasswd_exp = ("xpath", "//*[@id='content']/div/h3")
    Logo=("xpath", "//*[@id='navbar']/div/div/a[1]/img")
    Logo_exp=("xpath", "/html/body/header/div[2]/ul/li/a")

    def ChembnbBuyerLogin(self,usrname,password):
        self.open(self.url)
        ele=self.findElement(self.SignIn_LinkText)
        self.click(ele)
        ele1=self.findElement(self.Username_Id)
        self.type(ele1,usrname)
        ele2=self.findElement(self.Password_Id)
        self.type(ele2,password)
        ele3 = self.findElement(self.SignIn_Btn)
        self.click(ele3)