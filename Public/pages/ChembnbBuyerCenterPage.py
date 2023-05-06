from Public.pages.BasePage import BasePage

class ChembnbBuyerCenterPage(BasePage):
    BuyerCenter = ("xpath", "/html/body/div[1]/div/ul/li[1]/a/span[2]")
    MyIndependentApplication = ("xpath", "/html/body/div[1]/div/ul/li[1]/ul/li[6]/a")
    MyIndependentApplication_exp = ("xpath", "/html/body/div[2]/div[1]/div[1]/div/div[2]/ul/li[3]")
    MyGroupApplications = ("xpath", "//*[@id='content']/div[1]/div/div[1]/div/div[1]/div[2]/ul/li[2]/a")
    MyGroupApplications_exp = ("xpath", "//*[@id='customer-orders']/ul/li[3]")
    MyWishList = ("xpath", "//*[@id='content']/div/div/div[1]/div/div[1]/div[2]/ul/li[3]/a")
    MyWishList_exp = ("xpath", "//*[@id='customer-orders']/ul/li[3]")
    MyPoints = ("xpath", "//*[@id='content']/div/div/div[1]/div/div[1]/div[2]/ul/li[3]/a")
    MyPoints_exp = ("xpath", "//*[@id='customer-orders']/ul/li[3]")
    EditProfile = ("xpath", "//*[@id='content']/div/div/div[1]/div/div[2]/div[2]/ul/li[1]/a")
    EditProfile_exp = ("xpath", "//*[@id='customer-orders']/ul/li[3]")
    ChangePassword = ("xpath", "//*[@id='content']/div/div/div[1]/div/div[2]/div[2]/ul/li[2]/a")
    ChangePassword_exp = ("xpath", "//*[@id='customer-orders']/ul/li[3]")
    LogOut = ("xpath", "//*[@id='content']/div/div/div[1]/div/div[2]/div[2]/ul/li[3]/a")