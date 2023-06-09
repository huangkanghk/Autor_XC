from Public.pages.BasePage import BasePage
from time import sleep
from Public.common import DoExcel

class OkchemHomePage(BasePage):
    url = DoExcel.File_Location().get_parameter("PRE地址")

    ForBuyer_link=("xpath","/html/body/header/div[1]/div/ul/li[1]/a")
    ProductDictory=("xpath","/html/body/header/div[1]/div/ul/li[1]/div/div[1]/div/a[1]")
    ProductDictory_exp = ("xpath", "/html/body/section[1]/div/div/a[2]")
    PostBuyingRequest=("xpath",'/html/body/header/div[1]/div/ul/li[1]/div/div[1]/div/a[3]')
    PostBuyingRequest_exp = ("xpath", '//*[@id="requestForm"]/h3')
    GroupBuying = ("xpath", '/html/body/header/div[1]/div/ul/li[1]/div/div[1]/div/a[4]')
    GroupBuying_exp = ("xpath", '//*[@id="navbar"]/div/div/a[2]')
    TradeServices = ("xpath", '/html/body/header/div[1]/div/ul/li[1]/div/div[2]/div/h4/a')
    TradeServices_exp = ("xpath", '/html/body/section/div/div/span')
    Sourcing= ("xpath", '/html/body/header/div[1]/div/ul/li[1]/div/div[2]/div/a[1]')
    Sourcing_exp = ("xpath", '/html/body/section[1]/div/div/span')
    FactoryAudit = ("xpath", '/html/body/header/div[1]/div/ul/li[1]/div/div[2]/div/a[2]')
    FactoryAudit_exp = ("xpath", '/html/body/section/div/div/span')
    SampleCollection = ("xpath", '/html/body/header/div[1]/div/ul/li[1]/div/div[2]/div/a[3]')
    SampleCollection_exp = ("xpath", '/html/body/section[1]/div/div/span')
    InspectionService = ("xpath", '/html/body/header/div[1]/div/ul/li[1]/div/div[2]/div/a[4]')
    InspectionService_exp = ("xpath", '/html/body/section/div/div/span')
    CreditSeller = ("xpath", '/html/body/header/div[1]/div/ul/li[1]/div/div[2]/div/a[5]')
    CreditSeller_exp = ("xpath", '/html/body/section/div/div/span')
    PaymentSolution = ("xpath", '/html/body/header/div[1]/div/ul/li[1]/div/div[2]/div/a[6]')
    PaymentSolution_exp = ("xpath", '/html/body/section[1]/div/div/span')
    BuyerGuide = ("xpath", '/html/body/header/div[1]/div/ul/li[1]/div/div[3]/div/a[1]')
    BuyerGuide_exp = ("xpath", '//*[@id="tagBuyerGuide"]/a')
    OverseasOffices = ("xpath", '/html/body/header/div[1]/div/ul/li[1]/div/div[3]/div/a[2]')
    OverseasOffices_exp = ("xpath", '//*[@id="__next"]/div/div[2]/div[1]/div/span[2]')

    ForSeller_link = ("xpath", '/html/body/header/div[1]/div/ul/li[2]/a')
    GlobalExports = ("xpath", '/html/body/header/div[1]/div/ul/li[2]/div/div[1]/div/a[1]')
    GlobalExports_expo = ("xpath", '/html/body/div[2]/div/span')
    IncreaseSales = ("xpath", '/html/body/header/div[1]/div/ul/li[2]/div/div[1]/div/a[2]')
    IncreaseSales_exp = ("xpath", '/html/body/div[1]/div/section/ul/li[1]/span')
    SearchBuyLead = ("xpath", '/html/body/header/div[1]/div/ul/li[2]/div/div[1]/div/a[3]')
    SearchBuyLead_exp = ("xpath", '/html/body/section[1]/div/p[1]')
    FindPotentialBuyers = ("xpath", '/html/body/header/div[1]/div/ul/li[2]/div/div[1]/div/a[4]')
    FindPotentialBuyers_exp = ("xpath", '/html/body/section[1]/div/p[1]/b')
    LocateTargetBuyers = ("xpath", '/html/body/header/div[1]/div/ul/li[2]/div/div[1]/div/a[5]')
    LocateTargetBuyers_exp = ("xpath", '/html/body/section/div/div/span')
    SupplierGuide = ("xpath", '/html/body/header/div[1]/div/ul/li[2]/div/div[2]/div/a[1]')
    SupplierGuide_exp = ("xpath", '//*[@id="tagSellerGuide"]/a')
    OverseaOffices_Seller = ("xpath", '/html/body/header/div[1]/div/ul/li[2]/div/div[2]/div/a[2]')

    TradeShows= ("xpath", '/html/body/header/div[1]/div/ul/li[3]/a')

    IndustryNews=("xpath",'/html/body/header/div[1]/div/ul/li[4]/a')
    IndustryNews_exp = ("xpath", '/html/body/section[1]/div/div/a[2]')

    Lanage= ("xpath", '/html/body/header/div[1]/div/div[1]/div')
    Lange_es = ("xpath", '//*[@id="lanSelector"]/li[1]/a')
    Lange_es_exp = ("xpath", '/html/body/header/div[2]/ul/li/a')
    Lange_pt = ("xpath", '//*[@id="lanSelector"]/li[2]/a')
    Lange_ru = ("xpath", '//*[@id="lanSelector"]/li[3]/a')

    all_category=("xpath",'/html/body/header/div[2]/ul/li/a')
    first_category= ("xpath", '/html/body/header/div[2]/ul/li/ul/li[1]/a')
    sub_category = ("xpath", '/html/body/header/div[2]/ul/li/ul/li[1]/ul/li[1]/div/a[1]')
    sub_category_exp = ("xpath", '/html/body/section[1]/div/div/a[2]')

    PostBuyingRequest_sum = ("xpath", '/html/body/header/div[2]/a/span')
    PostBuyingRequest_sum_exp = ("xpath", '//*[@id="requestForm"]')
    LikeProduct_img = ("xpath", "//ul[@class='homeLike-list']/li[1]/a/div[1]/img")
    LikeProduct_img_exp = ("xpath", '/html/body/section[1]/div/div/a[2]')

    LatestBuyingRequest = ("xpath", '/html/body/section[2]/div/div[2]/h3[2]/a/span')
    LatestBuyingRequest_exp = ("xpath", '/html/body/section[1]/div/p[1]')
    JoinNow = ("xpath", '/html/body/div[1]/div/a')
    JoinNow_exp = ("xpath", '/html/body/div[1]/div/section/ul/li[1]/span')
    Chembnb_more = ("xpath", '/html/body/section[4]/div/div/div[1]/ul/li/a')
    Chembnb_more_exp = ("xpath", '/html/body/section[4]/div/div/div[1]/ul/li/a')
    Chembnb_img = ("xpath", "/html/body/section[4]/div/div/div[2]/div/div[1]/ul/li[1]/a/div[1]")
    Chembnb_img_exp = ("xpath", "//a[@href='/group-buying']")

    TradeShows_more = ("xpath", '/html/body/section[6]/div/div/div[1]/ul/li/a')
    TradeShows_more_exp = ("xpath", '/html/body/section[6]/div/div/div[1]/ul/li/a')
    TradeShows_select = ("xpath", '/html/body/section[6]/div/div/div[2]/div[2]/span[1]')
    TradeShows_img = ("xpath", "/html/body/section[2]/div/div/div[1]/form/div[2]/ul/li[1]/a/div/img[1]")
    TradeShows_img_two = ("xpath", "/html/body/section[6]/div/div/div[2]/div[1]/div[2]/ul/li[1]/a/div[1]/img")
    TradeShows_exp = ("xpath", "/html/body/section/div/div/a[2]")

    NewsMore = ("xpath", '/html/body/section[7]/div/div/div[1]/ul/li/a')
    News_img = ("xpath", "/html/body/section[7]/div/div/div[2]/ul/li[1]/a/img")
    News_img_exp = ("xpath", '/html/body/section[1]/div/div/a[2]')

    ProductDirectory_footer = ("xpath", '/html/body/footer/div[1]/div[1]/div[1]/ul/li[2]/a')
    PostBuyingRequest_footer = ("xpath", '/html/body/footer/div[1]/div[1]/div[1]/ul/li[4]/a')
    GroupBuying_footer = ("xpath", '/html/body/footer/div[1]/div[1]/div[1]/ul/li[5]/a')
    TradeServices_footer = ("xpath", '/html/body/footer/div[1]/div[1]/div[1]/ul/li[6]/a')
    BuyerGuide_footer = ("xpath", '/html/body/footer/div[1]/div[1]/div[1]/ul/li[7]/a')
    GlobalExports_footer = ("xpath", '/html/body/footer/div[1]/div[1]/div[2]/ul/li[2]/a')
    IncreaseSales_footer = ("xpath", '/html/body/footer/div[1]/div[1]/div[2]/ul/li[3]/a')
    SearchBuylead_footer = ("xpath", '/html/body/footer/div[1]/div[1]/div[2]/ul/li[4]/a')
    FindPotentialBuyers_footer = ("xpath", '/html/body/footer/div[1]/div[1]/div[2]/ul/li[5]/a')
    LocateTargetBuyers_footer = ("xpath", '/html/body/footer/div[1]/div[1]/div[2]/ul/li[6]/a')
    SupplierGuide_footer = ("xpath", '/html/body/footer/div[1]/div[1]/div[2]/ul/li[7]/a')
    AboutOkchem_footer = ("xpath", '/html/body/footer/div[1]/div[1]/div[3]/ul/li[2]/a')
    ContactUs_footer = ("xpath", '/html/body/footer/div[1]/div[1]/div[3]/ul/li[3]/a')
    Chinasite_footer = ("xpath", '/html/body/footer/div[1]/div[1]/div[3]/ul/li[4]/a')
    Chinasite_footer_exp = ("xpath", '/html/body/div[1]/div/ul/li[1]/a/span')
    OverseasOffices_footer = ("xpath", '/html/body/footer/div[1]/div[1]/div[3]/ul/li[5]/a')
    OurPartnerMore_footer = ("class", 'partner-more')
    OurPartnerMore_footer_more = ("xpath", '/html/body/section[1]/div/div/span')
    SupplierHome=("xpath","/html/body/section[3]/div/div/ul/li/a/p")
    #SupplierHome_exp = ("xpath", "/html/body/section[1]/div/div/a[2]")

    OverseasOffices_home = ("xpath", "/html/body/div[2]/div/span")

    showroom_detail = ("xpath", "/html/body/section[1]/div/div/a[2]")
    showroom_a=("xpath", "/html/body/footer/div/div[2]/a[1]/strong")
    showroom_b = ("xpath", "/html/body/footer/div/div[2]/a[2]/strong")
    showroom_c = ("xpath", "/html/body/footer/div/div[2]/a[3]/strong")
    showroom_d = ("xpath", "/html/body/footer/div/div[2]/a[4]/strong")
    showroom_e = ("xpath", "/html/body/footer/div/div[2]/a[5]/strong")
    showroom_f = ("xpath", "/html/body/footer/div/div[2]/a[6]/strong")
    showroom_g = ("xpath", "/html/body/footer/div/div[2]/a[7]/strong")
    showroom_h = ("xpath", "/html/body/footer/div/div[2]/a[8]/strong")
    showroom_i = ("xpath", "/html/body/footer/div/div[2]/a[9]/strong")
    showroom_j = ("xpath", "/html/body/footer/div/div[2]/a[10]/strong")
    showroom_k = ("xpath", "/html/body/footer/div/div[2]/a[11]/strong")
    showroom_l = ("xpath", "/html/body/footer/div/div[2]/a[12]/strong")
    showroom_m = ("xpath", "/html/body/footer/div/div[2]/a[13]/strong")
    showroom_n = ("xpath", "/html/body/footer/div/div[2]/a[14]/strong")
    showroom_o = ("xpath", "/html/body/footer/div/div[2]/a[15]/strong")
    showroom_p = ("xpath", "/html/body/footer/div/div[2]/a[16]/strong")
    showroom_q = ("xpath", "/html/body/footer/div/div[2]/a[17]/strong")
    showroom_r = ("xpath", "/html/body/footer/div/div[2]/a[18]/strong")
    showroom_s = ("xpath", "/html/body/footer/div/div[2]/a[19]/strong")
    showroom_t = ("xpath", "/html/body/footer/div/div[2]/a[20]/strong")
    showroom_u = ("xpath", "/html/body/footer/div/div[2]/a[21]/strong")
    showroom_v = ("xpath", "/html/body/footer/div/div[2]/a[22]/strong")
    showroom_w = ("xpath", "/html/body/footer/div/div[2]/a[23]/strong")
    showroom_x = ("xpath", "/html/body/footer/div/div[2]/a[24]/strong")
    showroom_y = ("xpath", "/html/body/footer/div/div[2]/a[25]/strong")
    showroom_z = ("xpath", "/html/body/footer/div/div[2]/a[26]/strong")
    showroom_num = ("xpath", "/html/body/footer/div/div[2]/a[27]/strong")
    casno_1 = ("xpath", "/html/body/footer/div[1]/div[4]/a[1]/strong")
    india=("xpath", "/html/body/footer/div[1]/div[1]/div[3]/ul/li[6]/a")
    india_exp = ("xpath", "/html/body/div[1]/header/section[1]/div/div/div[1]/p[1]/a")
    casno_detail = ("xpath", "/html/body/section[1]/div/div/span[2]")
    findsupplier = ("xpath", "/html/body/header/div[1]/div/ul/li[1]/div/div[1]/div/a[2]")
    findsupplier_footer = ("xpath", "/html/body/footer/div/div[1]/div[1]/ul/li[3]/a")
    findsupplier_exp = ("xpath", "/html/body/section/div/div/span[2]")



    def LoginOkchemHome(self):
        self.open(self.url)





