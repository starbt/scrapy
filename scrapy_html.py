import urllib.request
url = 'http://www.douban.com'
webpage = urllib.request.urlopen(url)
data = webpage.read()
data = data.decode('UTF-8')
print(data)
