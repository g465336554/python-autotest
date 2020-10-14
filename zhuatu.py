# -*- coding: utf-8 -*-

# 爬虫是python的一个方向，从网络上批量获取数据的
'''
1.能够连接到网络的库，能够找到目标网站
'''
import requests
import re
url ='https://www.tukuppt.com/yinxiao/'
requests.get(url)
data = requests.get(url)
# print(data.text)

# <Response [200]> 登陆状态吗
reg = """<a class="title" target="_blank" href=".*?">(.*?)</a>"""
names = re.findall(reg,data.text)
print(names)

# 获取audio
reg1 = '<source src="(.*?)" type="audio/mpeg">'
audios = re.findall(reg1,data.text)
print(audios)

for audio,name in zip (audios,names):
    music = requests.get('http:'+url)
    with open('./gaoxiao/%s.mp3' % name,'wb')as file:
        file.write((music.content))
    print('s%下载成'%name)