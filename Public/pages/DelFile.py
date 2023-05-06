import urllib.request
import requests
import os.path
import ctypes
import random
import time,shutil

filter=[".jpg"]

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
        urllib.request.urlretrieve(img_url,filepath)
    except IOError as e:
        print ('文件操作失败',e)
    except Exception as e:
        print ('错误 ：',e)
    print("Save", filepath, "successfully!")

    return filepath

# 请求网页，跳转到最终 img 地址
def get_img_url(raw_img_url = "https://area.sinaapp.com/bingImg/"):
    r = requests.get(raw_img_url)
    img_url = r.url # 得到图片文件的网址
    print('img_url:', img_url)
    return img_url

# 设置图片绝对路径 filepath 所指向的图片为壁纸
def set_img_as_wallpaper(filepath):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, filepath, 0)

def get_file_name(file_dir):
    Result=[]
    #root:当前目录路径；dirs：当前路径下所有子目录；files：当前路径下所有非目录子文件
    for root,dirs,files in os.walk(file_dir):
        for file in files:
            apath=os.path.join(root,file)
            ext=os.path.splitext(apath)[1]  # 获取文件后缀 [0]获取的是除了文件名以外的内容
            if ext in filter:
                Result.append(apath)
        return Result

def get_picture_count(file_dir):
    count=0
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if file.endswith('jpg'):
                count+=1
        return count

def list_all_files(rootdir):
    import os
    _files = []
    list = os.listdir(rootdir) #列出文件夹下所有的目录与文件
    for i in range(0,len(list)):
           path = os.path.join(rootdir,list[i])
           if os.path.isdir(path):
              _files.extend(list_all_files(path))
           if os.path.isfile(path):
              _files.append(path)
    return _files


def main():
    dirname = "D:\WallpaperPicture\\4k\\影视\\"          # 获取图片的目录
    sum_filename=list_all_files(dirname)                 # 获取目录下所有图片
    sum_count=len(sum_filename)
    print(sum_count)# 获取图片总个数
    for i in range(0,sum_count):
      len1=os.path.getsize(sum_filename[i])
      print(len1)
      if len1<100:
        os.remove(sum_filename[i])
main()