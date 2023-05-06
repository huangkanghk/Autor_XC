from datetime import datetime

def baseUrl_dev():
    return "http://www.devokchem2.com"

def baseUrl_int():
    return "http://www.intokchem2.com"

def baseUrl_pre():
    return "https://www.preokchem.com"

def baseUrl_prod():
    return "https://www.okchem.com"

def getCurrentTime():
    #format = "%Y %m %d %H:%M:%S"
    format="%a %b %d %H:%M:%S %Y"
    return datetime.now().strftime(format)

# def timeDiff():
#     #format = "%Y %m %d %H:%M:%S"
#     format="%a %b %d %H:%M:%S %Y"
#     return datetime.strftime(endtime,format)-datetime.strftime(starttime,format)

#print(getCurrentTime())