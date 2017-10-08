#模拟登录
import urllib.request
weburl = 'http://www.douban.com'
webheader = {
    'Connection':'Keep-Alive',
    'Accept':'text/html, application/xhtml+xml,*/*',
    'Accept-Language':'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0',
    'Host':'www.douban.com',
    'DNT':'1'
}
req = urllib.request.Request(url=weburl, headers=webheader)
webPage = urllib.request.urlopen(req)
data = webPage.read()
data = data.decode('UTF-8')
print(data)
