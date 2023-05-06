import requests
from bs4 import BeautifulSoup
import os

main_url='http://pic.netbian.com/4kfengjing'
all_url = 'http://pic.netbian.com/4kfengjing'
main_url1='http://pic.netbian.com'


#http请求头
#"Mozilla/5.0 (X11; Linux x86_64)"
Hostreferer = {
    'User-Agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
    'Referer':'http://pic.netbian.com'
               }
Picreferer = {
    'User-Agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
    'Referer':'http://pic.netbian.com'
}
#此请求头破解盗链

start_html = requests.get(all_url,headers = Hostreferer)

#保存地址
path = 'D:\\WallpaperPicture\\4k\\风景'

#找寻最大页数
soup = BeautifulSoup(start_html.text,"html.parser",from_encoding='gbk')
page = soup.find('div',class_='page').find_all('a')
max_page = page[6].text
print('列表最大页数：'+max_page)

same_url = 'http://pic.netbian.com/4kfengjing/index_'
for n in range(1,int(max_page)+1):
    if n==1:
        ul=main_url
    else:
        ul = same_url + str(n)+'.html'
    start_html = requests.get(ul, headers = Hostreferer)
    start_html.encoding=start_html.apparent_encoding
    soup = BeautifulSoup(start_html.text,"html.parser")
    all_a = soup.find('ul',class_='clearfix').find_all('a',target='_blank')
    for a in all_a:
        title = a.get_text() #提取文本
        if(title != ''):
            print("准备扒取："+title.strip().replace('\n', '').replace('\r','').replace(' ', ''))

            #win不能创建带？的目录
            if (os.path.exists(path + title.strip().replace('\n', '').replace('\r','').replace(' ', ''))):
                    #print('目录已存在')
                    flag=1
            else:
                os.makedirs(path + title.strip().replace('\n', '').replace('\r','').replace(' ', ''))
                flag=0
            os.chdir(path + title.strip().replace('\n', '').replace('\r','').replace(' ', ''))
            #图片详情地址
            href =main_url1+a['href']
            html = requests.get(href,headers = Hostreferer)
            mess = BeautifulSoup(html.text,"html.parser",from_encoding="gbk")
            pic_max = mess.find('a',id='img').find_all('img')
            pic_max = len(pic_max) #最大图片数
            #print(pic_max)
            if(flag == 1 and len(os.listdir(path+title.strip().replace('\n', '').replace('\r','').replace(' ', ''))) >= int(pic_max)):
                print('已经保存完毕，跳过')
                continue
            for num in range(0,int(pic_max)):
                pic = href
                html = requests.get(pic,headers = Hostreferer)
                mess = BeautifulSoup(html.text,"html.parser",from_encoding="gbk")
                pic_url = mess.find('a',id='img').find_all('img')
                print(main_url1+pic_url[num]['src'])
                #exit(0)
                html = requests.get((main_url1+pic_url[num]['src']),headers = Picreferer)
                file_name = pic_url[num]['src'].split(r'/')[-1]
                f = open(file_name,'wb')
                f.write(html.content)
                f.close()
            print('完成')
    print('第',n,'页完成')