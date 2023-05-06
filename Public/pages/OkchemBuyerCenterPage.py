from Public.pages.BasePage import BasePage
from Public.pages.OkchemLoginPage import OkchemLoginPage
from time import sleep
from Public.common import DoExcel

class OkchemBuyerCenterPage(BasePage):
    url = DoExcel.File_Location().get_parameter("PRE地址")

    Nicheng_link=("xpath","/html/body/header/div[1]/div/div[2]/p/a")
    Home_exp=("xpath","/html/body/section[2]/div/div/div[2]/section/div[1]/h3")

    Wishlist_link=("xpath","/html/body/section[2]/div/div/div[1]/div[1]/div[2]/h4")
    FavoriteProduct_link=("xpath",'/html/body/section[2]/div/div/div[1]/div[1]/div[2]/ul/li[1]/a')
    FavoriteProduct_exp = ("xpath", '/html/body/section[2]/div/div/div[2]/div[1]/div/table/thead/tr/td[1]')

    FavoriteSupplier_link=("xpath",'/html/body/section[2]/div/div/div[1]/div[1]/div[2]/ul/li[2]/a')
    FavoriteSupplier_exp = ("xpath", '/html/body/section[2]/div/div/div[2]/div/div/table/thead/tr/td[1]')

    MyInquiry_link=("xpath","/html/body/section[2]/div/div/div[1]/div[1]/div[3]/h4/a")
    MyInquiry_exp = ("xpath", "/html/body/section[2]/div/div/div[2]/div/h3")

    MyMessage_link = ("xpath", "/html/body/section[2]/div/div/div[1]/div[1]/div[4]/h4/a")
    MyMessage_exp = ("xpath", "/html/body/section[2]/div/div/div[2]/div/ul/h3")

    MyBuyingRequest_link = ("xpath", "/html/body/section[2]/div/div/div[1]/div[1]/div[5]/h4/a")
    MyBuyingRequest_exp = ("xpath", "/html/body/section[2]/div/div/div[2]/div/h3")

    MyServiceOrder_link = ("xpath", "/html/body/section[2]/div/div/div[1]/div[1]/div[6]/h4/a")
    MyServiceOrder_exp = ("xpath", "/html/body/section[2]/div/div/div[2]/div/h3")

    MyCreditSeller_link = ("xpath", "/html/body/section[2]/div/div/div[1]/div[1]/div[8]/h4/a")
    MyCreditSeller_exp = ("xpath", "/html/body/section[2]/div/div/div[2]/div[1]/h3[1]")

    MyRefer_link = ("xpath", "/html/body/section[2]/div/div/div[1]/div[1]/div[9]/h4/a")
    MyRefer_exp = ("xpath", "/html/body/section[2]/div/div/div[2]/div[1]/p")

    EditMyAccount_link = ("xpath", "/html/body/section[2]/div/div/div[1]/div[1]/div[10]/h4")
    MyProfile_link = ("xpath", "/html/body/section[2]/div/div/div[1]/div[1]/div[10]/ul/li[2]/a")
    MyProfile_exp = ("xpath", "/html/body/section[2]/div/div/div[2]/div/h3/span")

    MyPreference_link = ("xpath", "/html/body/section[2]/div/div/div[1]/div[1]/div[10]/ul/li[2]/a")
    MyPreference_exp = ("xpath", "/html/body/section[2]/div/div/div[2]/div/h3/span")

    ChangePassword_link = ("xpath", "/html/body/section[2]/div/div/div[1]/div[1]/div[10]/ul/li[3]/a")
    ChangePassword_exp = ("xpath", '//*[@id="passwordForm"]/h3')

    Logout_link = ("xpath", "/html/body/section[2]/div/div/div[1]/div[1]/div[11]/h4/a")
    Logout_exp = ("xpath", "/html/body/header/div[2]/ul/li/a")


    def LoginBuyerCenter(self,username,password):
        self.open(self.url)
        Login=self.findElement(OkchemLoginPage.SignIn_LinkText)
        self.click(Login)
        Username=self.findElement(OkchemLoginPage.Username_Id)
        self.type(Username,username)
        Password=self.findElement(OkchemLoginPage.Password_Id)
        self.type(Password,password)
        self.click(self.findElement(OkchemLoginPage.SignIn_Btn))
        Sign=self.findElement(self.Nicheng_link)
        self.click(Sign)
