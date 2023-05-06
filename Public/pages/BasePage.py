from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
import os
from config import globalconfig

class BasePage():
    """
    页面基类
    """
    def __init__(self):
        self.timeout=120
        try:
            #不启动浏览器进行测试
            # options = Options()
            # options.add_argument('-headless')
            # options.add_argument("--disable-gpu")
            # self.driver = webdriver.Firefox(firefox_options=options)
            #启动浏览器进行测试
            self.driver=webdriver.Firefox()
            #self.driver = webdriver.Chrome(ChromeDriverManager().install())
        except Exception:
            raise NameError("not FireFox")

    def open(self,url):
        self.driver.set_page_load_timeout(120)
        self.driver.set_script_timeout(120)
        self.driver.maximize_window()
        if url!="":
            try:
                self.driver.get(url)
            except TimeoutException:
                print("time out after 120 seconds when loading page")
                self.driver.execute_script('window.stop()')#当页面加载时间超过设定时间，通过执行Javascript来stop加载
        else:
            raise ValueError("Please input a url!")

    def findElement(self,element):
        try:
            type=element[0]
            value=element[1]
            if type=="id" or type=="ID" or type=="Id":
                elem=WebDriverWait(self.driver,self.timeout).until(EC.visibility_of_element_located((By.ID,value)))
                #elem=self.driver.find_element_by_id(value)
            elif type=="name" or type=="NAME" or type=="Name":
                elem = WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located((By.NAME,value)))
                #elem =self.driver.find_element_by_name(value)
            elif type == "class" or type == "CLASS" or type == "Class":
                elem = WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located((By.CLASS_NAME,value)))
                #elem =self.driver.find_element_by_class_name(value)
            elif type == "link_text" or type == "LINK_TEXT" or type == "Link_text":
                elem = WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located((By.LINK_TEXT,value)))
                #elem =self.driver.find_element_by_link_text(value)
            elif type == "xpath" or type == "XPATH" or type == "Xpath":
                elem = WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located((By.XPATH,value)))
                #elem =self.driver.find_element_by_xpath(value)
            elif type == "css" or type == "CSS" or type == "Css":
                elem = WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located((By.CSS_SELECTOR, value)))
                #elem =self.driver.find_element_by_css_selector(value)
            elif type == "tag_name" or type == "TAG_NAME" or type == "Tag_name":
                elem = WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located((By.TAG_NAME, value)))
            else:
                raise NameError("Please input a corrent type parameter!")
        except Exception:
            raise NameError("This element is not found"+str(element))
        return elem

    def type(self,element,text):
        element.send_keys(text)

    def click(self,element):
        element.click()

    def enter(self,element):
        element.send_keys(Keys.RETURN)

    def quit(self):
        self.driver.quit()

    def close(self):
        self.driver.close()

    def getTitle(self,element):
        #等待目标页面里面具体元素出现后，再获取页面的title
        self.findElement(element)
        return self.driver.title
        #WebDriverWait(self.driver, self.timeout).until_not(EC.title_is(""))

    def waitTitle(self,element):
        WebDriverWait(self.driver, self.timeout).until(EC.title_contains(element))

    def waitText(self,element):
        WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(element))

    def waitWindow(self,handles):
        WebDriverWait(self.driver, self.timeout).until(EC.new_window_is_opened(handles))

    def waitContainText(self,locator,text):
        WebDriverWait(self.driver, self.timeout).until(EC.text_to_be_present_in_element(locator,text))

    def getAttribute(self,element,attribute):
        return element.get_attribute(attribute)

    def getText(self,element):
        ele=self.findElement(element)
        return ele.text

    def display(self,id):
        self.driver=webdriver.Firefox()
        js='document.getElementById(list[id]).style.display="block"'
        self.driver.execute_script(js)

    def getPicture(self,screenname):
        self.driver.get_screenshot_as_file(screenname)

    def SelectValue(self,element,id):
        ele=self.findElement(element)
        ele.find_elements_by_tag_name("option")[id].click()

    def MousePause(self,element):
        ele=self.findElement(element)
        ActionChains(self.driver).move_to_element(ele).perform()
        sleep(2)

    def MouseClick(self,element):
        ele=self.findElement(element)
        ActionChains(self.driver).click(ele).perform()
        sleep(2)

    def execute_script(self,js):
        self.driver.execute_script(js)

    def scrollTo(self,element):
        target=self.findElement(element)
        self.driver.execute_script("arguments[0].scrollIntoView();",target)

    def getAllHandles(self):
        handles=self.driver.window_handles
        return handles

    def getCurrentHandle(self):
        handle=self.driver.current_window_handle
        return handle

    def switchHandle(self,i):
        handles=self.getAllHandles()
        self.driver.switch_to.window(handles[i])

# tt=BasePage()
# tt.open("https://www.okchem.com")
# tt.scrollTo(("xpath", "/html/body/footer/div/div[2]/a[2]/strong"))
# a1=tt.findElement(("xpath", "/html/body/footer/div/div[2]/a[2]/strong"))
# tt.click(a1)
# aa=tt.getTitle(("xpath", "/html/body/section[1]/div/div/a[2]"))
# print(aa)