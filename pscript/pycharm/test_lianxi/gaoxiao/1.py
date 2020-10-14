# -*- coding: utf-8 -*-  
import requests
from bs4 import BeautifulSoup
from pyquery import PyQuery as pq
from lxml import etree
def geu_page(url):
    try:
        res = requests.get(url,timeout=4)
        res.encoding = 'utf-8'
        if res.status_code == 200:
            html = res.text
            return html.encode("utf-8")
    except Exception as e:
        for i in range(3):
            print(url,e)
            res = requests.get(url,timeout=4)
            res.encoding = 'utf-8'
            if res.status_code == 200:
                html = res.text
                return html.encode('utf-8')
def get_index(url):
    html = geu_page(url)
    html = BeautifulSoup(html,'lxml')
    datas = html.find_all('ul')
    data = datas[2]
    data = BeautifulSoup(str(data),'lxml')
    for  urls in data.find_all('a'):
        yield 'http://www.runoob.com' + urls.get('href')

def get_data(url):
    html = geu_page(url)
    doc = pq(html)
    datas = etree.HTML(html)
    title = doc('#content h1').text()
    print('正在下载'+":"+title)
    data = doc('#content p')
    name = pq(data[1]).text()
    num = pq(data[2]).text()
    n = data[3].text
    data = datas.xpath('//div[@class="hl-main"]/span/text()')
    code = ''.join(data)
    with open(r'pythpn习题100例.txt','a+',encoding='utf-8') as f:
        f.write(title+'\n')
        f.write(name+'\n')
        f.write(num+'\n')
        f.write(n+'\n')
        f.write(code)
        f.write('\r\n')
def main():
    url = r'http://www.runoob.com/python/python-100-examples.html'
    for i in get_index(url):
        get_data(i)

if __name__ == '__main__':
    main()