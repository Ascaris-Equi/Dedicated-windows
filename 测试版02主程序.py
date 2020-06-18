import sys
import os
import pywintypes
import win32api
import win32process
import urllib.request
import time

文件路径 = (sys._getframe().f_code.co_filename) 
程序名 = os.path.basename(文件路径)
所在路径 = 文件路径.replace(程序名,'')
地址后缀 = 'p.exe' 
地址前缀 = 'fg' 

def file_name(file_dir):   
    L=[]   
    for root, dirs, files in os.walk(file_dir):  
        for file in files:  
            if os.path.splitext(file)[1] == '.exe':  
                L.append(os.path.join(root, file))  
    return L  

file_name(所在路径).sort( key=None, reverse=False)
del file_name(所在路径)[-2:]
版本号 = 800
尝试号 = 所在路径+地址前缀+str(版本号)+地址后缀
i = 0
for i in range(500):
    if 尝试号 in file_name(所在路径):
        break
    i = i + 1
    版本号 = 版本号 - 1
    尝试号 = 所在路径+地址前缀+str(版本号)+地址后缀

for i in range(10):
    地址前缀 = 'fg'
    程序名 = 所在路径+地址前缀+str(版本号)+地址后缀
    win32process.CreateProcess(程序名, '', None, None, 0, win32process.CREATE_NO_WINDOW, None, None, win32process.STARTUPINFO())
    print(程序名 + '正在启动，请耐心等待1分钟左右')
    time.sleep(45)
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/76.0.1')]
    aa=('https://www.google.com')
    print('正在检查网络是否连接，请稍后')
    tempUrl = aa

    try :
	    opener.open(tempUrl)
	    n = 1
    except urllib.error.HTTPError:
	    n = 0
    except urllib.error.URLError:
	    n = 0

    if (n == 0):
        进程名 = 'fg'+str(版本号)+地址后缀
        os.system('%s%s' % ("taskkill /F /IM ",进程名))
        版本号 = int(版本号) - 1
        print('网络尚未连接，请稍等，接下来为您试验上一个版本'+str(版本号))

    if (n == 1):
        print('网络已经连接，实验完毕，请重启您的计算机')
        os.system('pause')
        sys.exit()
    i = i+1
print('对不起，请尝试其他方式进行实验')
os.system('pause')
