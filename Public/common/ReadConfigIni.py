import configparser
import codecs
import os

class ReadConfigIni():
    """
    实例化configparser
    """
    def __init__(self,filename):
        self.cf=configparser.ConfigParser()
        self.cf.read(filename)

    #读操作
    def getConfigValue(self,config,name):
        value=self.cf.get(config,name)
        return value


# **************************
# 调式一下
# **************************
# file_path=os.path.split(os.path.realpath(__file__))[0]
# print file_path
# read_config=ReadConfigIni(os.path.join(file_path,'Config.ini'))
# print read_config
# value=read_config.getConfigValue('url','PROD')
# print value