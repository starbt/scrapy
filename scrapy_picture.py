import urllib.request
import socket
import re
import sys
import os
targetDir = r'/home/xcv/learning_python/scrapy/picture'

def destFile(path):
    if not os.path.isdir(targetDir):
        os.mkdir(targetDir)
    pos = path.rindex('/')
    t = os.path.join(targetDir, path[pos+1:])
    return t

if __name__ == '__main__':
    #weburl = 'https://www.douban.com/'
    weburl = 'http://image.baidu.com/'
    webheader = {
        'Connection':'Keep-Alive',
        'Accept':'text/html, application/xhtml+xml,*/*',
        'Accept-Language':'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
        'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0',
        'Host':'www.douban.com',
        'DNT':'1'
    }
    req = urllib.request.Request(url=weburl, headers=webheader)
    webpage = urllib.request.urlopen(req)
    contentBytes = webpage.read()

    #pic_links = re.findall(r'(https:[^\s]*?(jpg|png|gif))', str(contentBytes))
    #print(pic_links)
    for link, t in set(re.findall(r'(https:[^\s]*?(jpg|png|gif))', str(contentBytes))):
        print(link)
        try:
            urllib.request.urlretrieve(link, destFile(link))
        except:
            print('失败')
