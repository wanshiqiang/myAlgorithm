from urllib.parse import urlunparse

data = ['http','www.baidu.com','index.html','user','a=6','comment']
print(urlunparse(data))


from urllib.parse import urlencode
params = {
    'name':'germey',
    'age':22
}
base_url = "http://www.baidu.com?"
url = base_url + urlencode(params)
print(url)

from urllib.parse import parse_qs,parse_qsl,urlparse

url = "http://www.baidu.com?name=germey&age=22"
result = urlparse(url)
print("urlparse:"+str(result))
paramsDict = parse_qs(result.query)
paramsTup = parse_qsl(result.query)
print("parse_qs:",type(paramsDict),paramsDict)
print("parse_qsl:",type(paramsTup),paramsTup)


from urllib.parse import quote,unquote

keyword = "莲花"
url = 'https://www.baidu.com/s?wd='+quote(keyword)
print(url)


url = "https://www.baidu.com/s?wd=%E8%8E%B2%E8%8A%B1"
print(unquote(url))



print("============测试robotparser==============")

from urllib.robotparser import RobotFileParser

rp = RobotFileParser()
rp.set_url("https://www.jianshu.com/robots.txt")
rp.read()
print(rp.read())
print(rp.can_fetch('*','https://www.jianshu.com/p/b67554025d7d'))
print(rp.can_fetch('*','https://www.jianshu.com/p/7833e651857d'))