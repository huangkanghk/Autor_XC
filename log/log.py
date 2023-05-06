import logging
import os
import time
from config import globalconfig

log_path=globalconfig.log_path

class Logger():

    def __init__(self,logger,CmdLevel,FileLevel):
        """

        :param logger:
        :param CmdLevel:
        :param FileLevel:
        """
        self.logger=logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        fmt=logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

        #设定日志文件的名称
        #存放在log类所在的当前目录
        self.LogFileName=os.path.join("{0}.log".format(time.strftime("%Y-%m-%d")))
        #讲日志存放在指定的日志路径下
        self.LogFileName =os.path.join(log_path,"{0}.log".format(time.strftime("%Y-%m-%d")))

        #设置控制台日志
        sh=logging.StreamHandler()
        sh.setFormatter(fmt)
        sh.setLevel(CmdLevel)

        #设置文件日志
        fh=logging.FileHandler(self.LogFileName)
        fh.setFormatter(fmt)
        fh.setLevel(FileLevel)

        self.logger.addHandler(sh)
        self.logger.addHandler(fh)

    def debug(self,message):
        self.logger.debug(message)

    def info(self,message):
        self.logger.info(message)

    def war(self,message):
        self.logger.warning(message)

    def error(self,message):
        self.logger.error(message)

    def cri(self,message):
        self.logger.critical(message)

# # ==============测试一下，正式环境可以注释掉===============
# if __name__=="__main__":
#     logger=Logger("FOX",CmdLevel=logging.INFO,FileLevel=logging.ERROR)
#     logger.debug("debug message")
#     logger.info("info message")
#     logger.war("warn message")
#     logger.cri("critical message")

