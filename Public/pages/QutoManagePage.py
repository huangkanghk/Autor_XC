from Public.pages.BasePage import BasePage
from time import sleep
from Public.common import DoExcel

class QutoManagePage(BasePage):

    homeName = ("xpath", "//*[@id='tags-view-container']/div/div[1]/div/span[2]")

    qutoText = ("xpath", "//*[@id='app']/div/div[2]/section/div/form/div/div[1]/label")
    searchButton = ("xpath", "//*[@id='app']/div/div[2]/section/div/form/div/div[10]/div/button[1]")
    resetButton = ("xpath", "//*[@id='app']/div/div[2]/section/div/form/div/div[10]/div/button[2]")

    quotSearchT = ("xpath","//*[@id='app']/div/div[2]/section/div/form/div/div[1]/div/div/input")
    quotCount = ("xpath","//*[@id='app']/div/div[2]/section/div/div[3]/div/span[1]")

    qutoCreate = ("xpath", "//*[@id='app']/div/div[2]/section/div/div[1]/div[1]/button/span")
    TimeText =("xpath","/html/body/div[2]/div/div[1]/span")

    quotData =("xpath","/html/body/div[2]/div/div[2]/form/div/div/div/input")
    quotSure = ("xpath","/html/body/div[2]/div/div[3]/div/button[1]")
    quotCancle = ("xpath", "/html/body/div[2]/div/div[3]/div/button[2]")
    createQu = ("xpath", "//*[@id='app']/div/div[2]/section/div/div[1]/div[1]/div[1]/button/span")
