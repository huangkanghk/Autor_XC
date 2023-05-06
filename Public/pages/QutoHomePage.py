from Public.pages.BasePage import BasePage
from time import sleep
from Public.common import DoExcel

class QutoHomePage(BasePage):

    homeName = ("xpath", "//*[@id='breadcrumb-container']/span/span/span[1]/span")

    qutoText =  ("xpath", "//*[@id='app']/div/div[2]/section/div/div[1]/div/div/div[1]/div/div[2]/div")
    shareText = ("xpath", "//*[@id='app']/div/div[2]/section/div/div[1]/div/div/div[3]/div/div[2]/div")
    createText =  ("xpath", "//*[@id='app']/div/div[2]/section/div/div[1]/div/div/div[2]/div/div[2]/div")

    qutoNum = ("xpath","//*[@id='app']/div/div[2]/section/div/div[1]/div/div/div[1]/div/div[2]/span")
    shareNum = ("xpath","//*[@id='app']/div/div[2]/section/div/div[1]/div/div/div[3]/div/div[2]/span")
    quotInut = ("xpath","'//*[@id='app']/div/div[2]/section/div/form/div/div[1]/div/div/input")

    #统计展示信息
    quotCountMsg = ("xpath", "//*[@id='tab-first']")
    loginCountMsg = ("xpath", "//*[@id='tab-second']")
    qutoTitle1 = ("xpath", "//*[@id='pane-first']/div/div[1]/div[3]/div[1]/div[1]/div[1]/span")
    qutoTitle2 = ("xpath", "//*[@id='pane-first']/div/div[1]/div[3]/div[1]/div[2]/div[1]/span")
    qutoTitle3 = ("xpath", "//*[@id='pane-first']/div/div[1]/div[3]/div[1]/div[3]/div[1]/span")
    qutoTitle4 = ("xpath", "//*[@id='pane-first']/div/div[1]/div[3]/div[1]/div[4]/div[1]/span")
    qutoTitle5 = ("xpath", "//*[@id='pane-first']/div/div[1]/div[3]/div[1]/div[5]/div[1]/span")

    title3Buttn = ("xpath", "//*[@id='pane-first']/div/div[1]/div[3]/div[1]/div[3]/div[1]/div/button/i")
    title4Buttn = ("xpath", "//*[@id='pane-first']/div/div[1]/div[3]/div[1]/div[4]/div[1]/div/button/i")
    title5Buttn = ("xpath", "//*[@id='pane-first']/div/div[1]/div[3]/div[1]/div[5]/div[1]/div/button/i")

    year = ("xpath", "//*[@id='pane-first']/div/div[1]/div[1]/div/div/div/div/div[1]/input")
    years = ("xpath", "/html/body/div[2]/div[1]/div[1]/ul")

    myQuoted =("xpath", "//*[@id='app']/div/div[2]/section/div/div[1]/div/div/div[1]/div/div[2]/div")
    searchQuot =("xpath","//*[@id='app']/div/div[2]/section/div/form/div/div[1]/label")

    shareQuot =("xpath","//*[@id='app']/div/div[2]/section/div/div[1]/div/div/div[3]/div/div[2]/div")
    reciveShare =("xpath","//*[@id='tab-tabShareFrom']")

    createQu =("xpath","//*[@id='app']/div/div[2]/section/div/div[1]/div/div/div[2]/div/div[2]/div")
    createQuot =("xpath","//*[@id='app']/div/div[2]/section/div/div[1]/div[1]/div[1]/button/span")