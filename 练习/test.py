import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
# data=bytes(urllib.parse.urlencode({'hello':'world'}),encoding='utf8')

# response=urllib.request.urlopen('http://httpbin.org/post',data=data)
# print(response.read().decode('utf8'))
# print(response.status)

def askURL(url):
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
    }

    data=bytes(urllib.parse.urlencode({'hello':'world'}),encoding='utf8')

    req=urllib.request.Request(url,data=data,headers=headers)
    response=urllib.request.urlopen(req)
    print(response.read().decode('utf8'))

# data=urllib.request.urlopen('http://www.baidu.com')
# html=open('./baidu.html','rb')
# htm=html.read()
# bs=BeautifulSoup(htm,'html.parser')
# a=bs.a.attrs
# print(a)
askURL('http://baidu.com')