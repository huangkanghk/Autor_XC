import requests
from bs4 import BeautifulSoup
import os,time,re
import shutil

def validateTitle(title):
    rstr = r"[ \/\\\:\*\?\"\<\>\|]"  # '/ \ : * ? " < > |'
    new_title = re.sub(rstr, "", title)  # 替换为下划线
    return new_title

main_url='http://pic.netbian.com/4kfengjing'
all_url = 'http://pic.netbian.com/4kfengjing'
main_url1='http://pic.netbian.com'


#http请求头
#"Mozilla/5.0 (X11; Linux x86_64)"
# Hostreferer = {
#     'User-Agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
#     'Referer':'http://pic.netbian.com'
#                }
Picreferer = {
    'User-Agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
    'Referer':'http://pic.netbian.com',
    'Cookie':'__cfduid=d5ae3439cf74d06a3dffb3685726ead121550726645; __guid=216607383.2501759259810721300.1550726646837.557; yjs_id=a667d5e2706c66b0c75dd10a82f424c7; Hm_lvt_14b14198b6e26157b7eba06b390ab763=1550917436; bdshare_firstime=1550927614714; zkhanecookieclassrecord=%2C53%2C; ctrl_time=1; Hm_lvt_526caf4e20c21f06a4e9209712d6a20e=1552986728,1553437842,1553482690,1553763105; PHPSESSID=4e5d3623f8237386ef8b62d9b24c92a5; zkhanmlusername=%C7%B3%B3%AA%C4%C7%D0%FD%C2%C9; zkhanmluserid=1065715; zkhanmlgroupid=3; zkhanmlrnd=Hn7ZyMjCcwgIPv2OjQZ8; zkhanmlauth=c53422d552f144f7ee6573665a27a2f8; Hm_lpvt_526caf4e20c21f06a4e9209712d6a20e=1553763115; monitor_count=6; security_session_verify=f6f883cad3be707c0be85badbdb18754'
}
Hostreferer=Picreferer
#此请求头破解盗链

start_html = requests.get(all_url,headers = Hostreferer)

#保存地址
path = 'D:\\WallpaperPicture\\4K\\风景\\'

#找寻最大页数
soup = BeautifulSoup(start_html.text,"html.parser",from_encoding='gbk')
page = soup.find('div',class_='page').find_all('a')
max_page = page[6].text
print('列表最大页数：'+max_page)

same_url = 'http://pic.netbian.com/4kfengjing/index_'
break_flag = False
for n in range(1,int(max_page)+1):
    if break_flag==True:
        break
    if n==1:
        ul=main_url
    else:
        ul = same_url + str(n)+'.html'
    start_html = requests.get(ul, headers = Hostreferer)
    start_html.encoding=start_html.apparent_encoding
    soup = BeautifulSoup(start_html.text,"html.parser")
    all_a = soup.find('ul',class_='clearfix').find_all('a',target='_blank')
    for a in all_a:
        if break_flag==True:
            break
        title = a.get_text() #提取文本
        if(title != ''):
            print("准备扒取："+validateTitle(title))

            #win不能创建带？的目录
            if (os.path.exists(path + validateTitle(title))):
                    #print('目录已存在')
                    flag=1
            else:
                os.makedirs(path + validateTitle(title))
                flag=0
            os.chdir(path + validateTitle(title))
            #图片详情地址
            pic_id =a['href'].split(r'/')[-1].split(r'.')[0]
            pic_url='http://pic.netbian.com/downpic.php?id={}&classid=59'.format(pic_id)
    #         html = requests.get(href,headers = Hostreferer)
    #         mess = BeautifulSoup(html.text,"html.parser",from_encoding="gbk")
    #         pic_max = mess.find('a',id='img').find_all('img')
    #         pic_max = len(pic_max) #最大图片数
    #         #print(pic_max)
            if(flag == 1 and len(os.listdir(path+validateTitle(title)))) >=1:
                print('存在已下载文件，跳过')
                continue
    #         for num in range(0,int(pic_max)):
    #             pic = href
    #             html = requests.get(pic,headers = Hostreferer)
    #             mess = BeautifulSoup(html.text,"html.parser",from_encoding="gbk")
    #             pic_url = mess.find('a',id='img').find_all('img')
    #             print(main_url1+pic_url[num]['src'])
    #             #exit(0)
            html = requests.get((pic_url),headers = Picreferer)
            file_name = validateTitle(title)+".jpg"
            try:
                f = open(file_name, 'wb')
                f.write(html.content)
                file_size = os.path.getsize(file_name)
                f.close()
                if int(file_size)<200:
                    print("达到服务器下载上限，停止下载")
                    break_flag = True
                    shutil.rmtree(path + validateTitle(title))
                    break
                else:
                    print('成功下载')
            except:
                print("没有正常下载，先跳过")
    print('第',n,'页完成')