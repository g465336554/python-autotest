# -*- coding: utf-8 -*-  
import urllib.request
url = "https://tieba.baidu.com/p/6310762577"
request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
#获取内容数据
html=response.read()#read(方法)
#设置内容为utf-8编码
html=html.decode("utf-8")
print(html)

