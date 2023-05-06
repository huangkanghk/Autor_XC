from Public.pages.BasePage import BasePage
from time import sleep
from Public.common import DoExcel

class OkchemSearchPage(BasePage):
    url = DoExcel.File_Location().get_parameter("PRE地址")
    Search_input=("id","keyword")
    SearchType=("id","searchType")
    SearchBtn=("id","searchButton")
    ProductName=("xpath",'//*[@id="myTab"]/li[1]/a')
    SupplierName=("xpath",'//*[@id="myTab"]/li[2]/a')
    NewName=("xpath","/html/body/section[1]/div/div/a[2]")

    def SelectSearchType(self,type="product"):
        if type=="Suppliers" or type=="suppliers":
            self.SelectValue(self.SearchType,1)
        elif type=="News" or type=="news":
            self.SelectValue(self.SearchType, 2)
        else:
            self.SelectValue(self.SearchType, 0)

    def Search(self,content,type):
        self.open(self.url)
        sleep(5)
        self.SelectSearchType(type)
        ele=self.findElement(self.Search_input)
        self.type(ele,content)
        self.findElement(self.SearchBtn).click()
        sleep(5)


