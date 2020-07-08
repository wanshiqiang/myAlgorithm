# urllib

## urlopen()

import urllib.request

response = urllib.request.urlopen("https://www.baidu.com/")

html = response.read()
print("response.read()的类型和值",type(html),html,sep="-----》")
print("------------------------------")
print("response.read().decode('utf-8')的类型和值",type(html.decode('utf-8')),html.decode('utf-8'),sep="-----》")
print("response.getheaders的类型和值",type(response.getheaders),response.getheaders,sep="----->")
print("response.getheader(name)的类型和值",type(response.getheader('server')),response.getheader('server'),sep="----->")
print("response.status的类型和值",type(response.status),response.status,sep="----->")
print("response.version的类型和值",type(response.version),response.version,sep="----->")
print("response.reason的类型和值",type(response.reason),response.reason,sep="----->")


data = bytes(urllib.parse.urlencode({'word':'hello'}),encoding='utf-8')
response2 = urllib.request.urlopen('http://httpbin.org/post',data=data)
print(response2.read())


import urllib.request

myRequest = urllib.request.Request("https://www.baidu.com")
response = urllib.request.urlopen(myRequest)
print("=============独立构造request请求=========================")
print(response.read().decode('utf-8'))

from urllib import request,parse

url = "http://httpbin.org/post"
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'Host':'httpbin.org',
}
dict = {
    'name':'Germey'
}
data = bytes(parse.urlencode(dict),encoding='utf-8')
myRequest = urllib.request.Request(url=url,headers=headers,data=data,method="POST")
response = request.urlopen(myRequest)
print("=============独立构造request2请求=========================")
print(response.read().decode('utf-8'))


print("=============HTTPCookieProcessor的使用=========================")
import http.cookiejar, urllib.request

cookie = http.cookiejar.CookieJar()
# 将创建的空的cookieJar对象传给handler
handler = urllib.request.HTTPCookieProcessor(cookie)
# 利用handler构建opener
opener = urllib.request.build_opener(handler)
response = opener.open('https://www.baidu.com')
for item in cookie:
    print(item.name+"="+item.value)


print("=============HTTPCookieProcessor的使用2：cookie生成文件格式=========================")
filename = "cookies.txt"
# cookie = http.cookiejar.MozillaCookieJar(filename=filename)
cookie = http.cookiejar.LWPCookieJar(filename=filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
opener.addheaders = [headers]
response = opener.open("https://www.baidu.com")
cookie.save(ignore_discard=True,ignore_expires=True)


print("=============HTTPCookieProcessor的使用3：读取并利用保存的Cookies文件=================")
myCookie = http.cookiejar.LWPCookieJar()
myCookie.load('cookies.txt',ignore_discard=True,ignore_expires=True)
handler = urllib.request.HTTPCookieProcessor(myCookie)
opener = urllib.request.build_opener(handler)
opener.addheaders = [headers]
response = opener.open("https://www.baidu.com")
print(response.read().decode('utf-8'))
print(response.getheaders())


from urllib import request,error

try:
    response = request.urlopen('https://www.hahaha.com/haha.html')
except error.HTTPError as e:
    print(e.reason,e.code,e.headers,sep="\n")
except error.URLError as e:
    print(e.reason)
else:
    print("请求成功")


from urllib.parse import urlparse

result = urlparse('https://www.baidu.com/index.html;user?id=5#comment')
print(type(result),result,sep="\n")


from urllib.parse import urlunparse

data = ['http','www.baidu.com','index.html','user','a=6','comment']
print(urlunparse(data))