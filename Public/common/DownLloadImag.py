from selenium import webdriver
import time
from PIL import Image

base_url = '***********'
browser = webdriver.Chrome()
browser.maximize_window()
browser.implicitly_wait(10)
browser.get(base_url)
browser.save_screenshot("D:/pic.png")#可以修改保存地址
# # (2)基操
# browser.find_element_by_name("username").send_keys("gxx")
# browser.find_element_by_name("password").send_keys("123456")
# time.sleep(2)
# (3)获取图片验证码坐标
code_ele = browser.find_element_by_xpath("//*[@id='app']/div/div[1]/form/div[3]/div/div/div[2]/div/img")
print("验证码的坐标为：", code_element.location)#控制台查看{'x': 1086, 'y': 368}
print("验证码的大小为：", code_element.size)# 图片大小{'height': 40, 'width': 110}
# (4)图片4个点的坐标位置
left = code_ele.location['x']#x点的坐标
top = code_ele.location['y']#y点的坐标
right = code_ele.size['width']+left#上面右边点的坐标
down = code_ele.size['height']+top#下面右边点的坐标
image = Image.open('D:/pic.png')
# (4)将图片验证码截取
code_image = image.crop((left, top, right, height))
code_image.save('D:/pic1.png')#截取的验证码图片保存为新的文件
