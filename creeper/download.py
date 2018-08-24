# urllib2 requests
import urllib.request as urllib2
import http.cookiejar as cookielib

url = 'http://www.baidu.com'

print('第一种方法')

response = urllib2.urlopen(url)
code = response.getcode()
html = response.read()

print(code)

# 创建Request对象
print('第一种方法')
request =  urllib2.Request(url)
request.add_header('User-Agent', 'Mozilla/5.0')
response2 = urllib2.urlopen(request)

print(response2.getcode())

print('第三种方法')
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)

response3 = urllib2.urlopen(url)
code = response3.getcode()
html = response3.read()

print(code)
print(len(html))