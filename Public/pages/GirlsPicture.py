from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO
import traceback
import urllib.request
import requests
import os.path
import ctypes
import random
import time

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36"}
def down_pic(url, path):
    try:
        req = urllib.request.Request(url, headers=headers)
        data = urllib.request.urlopen(req).read()
        with open(path, 'wb') as f:
            f.write(data)
            f.close()
    except Exception as e:
        print(str(e))

def save_img(img_url,dirname):
    #保存图片到磁盘文件夹dirname中
    try:
        if not os.path.exists(dirname):
            print ('文件夹',dirname,'不存在，重新建立')
            #os.mkdir(dirname)
            os.makedirs(dirname)
        #获得图片文件名，包括后缀
        basename = os.path.basename(img_url)
        #拼接目录与文件名，得到图片路径
        filepath = os.path.join(dirname, basename)
        #下载图片，并保存到文件夹中
        # 如果不加上下面的这行出现会出现urllib2.HTTPError: HTTP Error 403: Forbidden错误
        # 主要是由于该网站禁止爬虫导致的，可以在请求加上头信息，伪装成浏览器访问User-Agent,具体的信息可以通过火狐的FireBug插件查询
        #urllib.request.urlretrieve(img_url,filepath)
        opener = urllib.request.build_opener()
        opener.addheaders = [('User-Agent',
                              'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
        urllib.request.install_opener(opener)
        urllib.request.urlretrieve(img_url, dirname)
    except IOError as e:
        print ('文件操作失败',e)
    except Exception as e:
        print ('错误 ：',e)
    print("Save", filepath, "successfully!")


path = 'D:\youzi4/'
num = 1
content = 'http://www.youzi4.cc/mm/'  #
# 爬取具体图片连接
while True:
    html = '.html'
    max = 100
    print(num)
    for n in range(1, max):
        url = content + str(num) + '/' + str(num) + '_' + str(n) + html  # mm/x/x_num.html
        webdata = requests.get(url).text
        #soup = BeautifulSoup(webdata, 'html.parser')
        soup = BeautifulSoup(webdata, 'lxml')
        try:
            link = soup.select("img.IMG_show")
            jpg = link[0].get('src')  # 定位后是一个列表，尽管只有列表只有一个，他还是一个列表，所以需要定位到[0]
            pic = requests.get(jpg)
            print(pic)
            #save_img(pic.url,path)
            image = Image.open(BytesIO(pic.content))
            print("d")
            image.save(path + str(num) + '_' + str(n) + '.jpg')
            print("完成：", n)
        except IndexError:
            break
        except OSError:
            traceback.print_exc()
            #print("失败IOError")
            #continue

    print('下载完成！')
    num += 1
