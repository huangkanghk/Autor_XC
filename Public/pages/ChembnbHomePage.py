from Public.pages.BasePage import BasePage

class ChembnbHomePage(BasePage):
    HotSearchKey = ("xpath", "//*[@id='content']/div[1]/div[1]/div/div/div[1]/p/a[1]")
    HotSearchKey_exp = ("xpath", "//*[@id='content']/div[1]/div[3]/div/p/strong")

    PostBuyingRequest = ("xpath", "//*[@id='content']/div[1]/div[1]/div/div/div[2]/div/a[1]")
    PostBuyingRequest_exp = ("xpath", "//*[@id='requestForm']/h3")

    IncreaseSales = ("xpath", "//*[@id='content']/div[1]/div[1]/div/div/div[2]/div/a[2]")
    IncreaseSales_exp = ("xpath", "/html/body/div[1]/div/section/ul/li[1]/span")

    BecomeOurPartner=("xpath", "//*[@id='content']/div[1]/div[1]/div/div/div[2]/div/a[3]")

    GroupBuyingImage = ("xpath", "//*[@id='content']/div[1]/div[4]/div[1]/div/div[1]/img")
    GroupBuyingImage_exp = ("xpath", "//*[@id='focusButtonId']")

    MiniOffice = ("xpath", "//*[@id='footer']/div/div[1]/ul/li[2]/a")
    MiniOffice_exp = ("xpath", "/html/body/section[1]/div/div/span")

    CreditLoan = ("xpath", "//*[@id='footer']/div/div[1]/ul/li[3]/a")
    CreditLoan_exp = ("xpath", "/html/body/section[1]/div/div/span")

    ContactUs = ("xpath", "//*[@id='footer']/div/div[2]/ul/li[2]/a")
    ContactUs_exp = ("xpath", "/html/body/section[2]/div/div/div[2]/div/div[1]")