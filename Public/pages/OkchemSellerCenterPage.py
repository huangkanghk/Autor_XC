from Public.pages.BasePage import BasePage
from Public.pages.OkchemLoginPage import OkchemLoginPage
from time import sleep
from Public.common import DoExcel

class OkchemSellerCenterPage(BasePage):
    url = DoExcel.File_Location().get_parameter("PRE地址")

    Lanage_text = ("xpath", "/html/body/header/div/ul/li[2]/div/span")
    Lanage_en = ("xpath", "/html/body/header/div/ul/li[2]/div/ul/li[1]/a")

    Store_Manage = ("xpath", "/html/body/div[2]/div/div[1]/ul/li[1]/div")
    Store_Setting = ("xpath", "/html/body/div[2]/div/div[1]/ul/li[1]/ul/li[1]/a")
    Store_Setting_exp = ("xpath", "/html/body/div[2]/div[1]/ol/li[3]")
    Store_MuliLanage = ("xpath", "/html/body/div[2]/div/div[1]/ul/li[1]/ul/li[2]/a")
    Store_MuliLanage_exp = ("xpath", "/html/body/div[2]/div[1]/div[2]/ol/li[3]")

    Product_Manage = ("xpath", "/html/body/div[2]/div[1]/div[1]/ul/li[2]/div")
    Release_Product = ("xpath", "/html/body/div[2]/div[1]/div[1]/ul/li[2]/ul/li[1]/a")
    Release_Product_exp = ("xpath", "/html/body/div[2]/div/ol/li[3]")
    Product_List = ("xpath", "/html/body/div[2]/div[1]/div[1]/ul/li[2]/ul/li[2]/a")
    Product_List_exp = ("xpath", "/html/body/main/div/ol/li[3]")
    Product_Setting = ("xpath", "//*[@id='productPanelCollapse']/div/ul/li[3]/a")
    Product_Setting_exp = ("xpath", "/html/body/main/div/ol/li[3]")

    Quote_Manage = ("xpath", "//*[@id='mainSidebarPanelGroup']/div[3]/div[1]/h4/a")
    Inquiry_Quote = ("xpath", "//*[@id='quotationManagementPanelCollapse']/div/ul/li[1]/a")
    Inquiry_Quote_exp = ("xpath", "/html/body/main/div/ol/li[3]")
    PostBuyingRequest_Quote = ("xpath", "//*[@id='quotationManagementPanelCollapse']/div/ul/li[2]/a")
    PostBuyingRequest_Quote_exp = ("xpath", "/html/body/main/div/ol/li[3]")

    Message_Manage = ("xpath", "//*[@id='mainSidebarPanelGroup']/div[4]/div[1]/h4/a/span")
    My_Message = ("xpath", "//*[@id='messagePanelCollapse']/div/ul/li/a")
    My_Message_exp = ("xpath", "/html/body/main/div/ol/li[3]")

    Service_Manage=("xpath", "//*[@id='mainSidebarPanelGroup']/div[5]/div[1]/h4/a/span")
    MyService_Order = ("xpath", "//*[@id='servicePanelCollapse']/div/ul/li[1]/a")
    MyService_Order_exp = ("xpath", "/html/body/main/div/ol/li[3]")
    MyMembership = ("xpath", "//*[@id='servicePanelCollapse']/div/ul/li[2]/a")
    MyMembership_exp = ("xpath", "/html/body/div[2]/div/ol/li[2]")

    Report_Manage=("xpath", "//*[@id='mainSidebarPanelGroup']/div[6]/div[1]/h4/a")
    MyReport_Order = ("xpath", "//*[@id='reportPanelCollapse']/div/ul/li/a")
    MyReport_Order_exp = ("xpath", "/html/body/main/div/ol/li[3]")

    Header_Icon=("xpath", "//*[@id='mainHeaderLogout']")
    Profile_Change = ("xpath", "//*[@id='mainHeaderLogout']/div/ul/li[1]/a")
    Profile_Change_exp = ("xpath", "/html/body/div[2]/div/ol/li[2]")
    Password_Change = ("xpath", "//*[@id='mainHeaderLogout']/div/ul/li[2]/a")
    Password_Change_exp = ("xpath", "/html/body/div[2]/div/ol/li[2]")
    Subaccount_Manage = ("xpath", "//*[@id='mainHeaderLogout']/div/ul/li[3]/a")
    Subaccount_Manage_exp = ("xpath", "/html/body/div[2]/div/ol/li[2]")
    Logout=("xpath", "//*[@id='mainHeaderLogout']/div/ul/li[4]/a")
    Logout_exp = ("xpath", "/html/body/header/div[2]/ul/li/a")

    Nicheng_link=("xpath","/html/body/header/div[1]/div/div[2]/p/a")

    def LoginSellerCenter(self,username,password):
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
