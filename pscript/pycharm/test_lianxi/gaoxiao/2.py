#!/usr/bin/python
#coding:utf-8
import os
import json
import re
import pymongo
import requests
from config import *
from requests.exceptions import RequestException
from bs4 import BeautifulSoup
from urllib.parse import urlencode
from hashlib import md5
from  multiprocessing import Pool

MONGO_URL = '127.0.0.1'
MONGO_DB = 'toutiao'
MONGO_TABLE = 'toutiao'

Group_start = 1
Group_end = 20

KEY = '詹姆斯'

client = pymongo.MongoClient(MONGO_URL,connect=False)
db = client[MONGO_DB]
def get_page_index(offest,keyword):
    data = {
        'offset': offest,
        'format': 'json',
        'keyword': keyword,
        'autoload': 'true',
        'count': '20',
        'cur_tab': 1,
        'from': 'search_tab',
        'pd': 'synthesis'
    }

    url = 'https://www.toutiao.com/search_content/?' + urlencode(data)
    try:
        headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                   'accept-encoding': 'gzip, deflate, br', 'accept-language': 'zh-CN,zh;q=0.9',
                   'cache-control': 'max-age=0',
                   'cookie': 'tt_webid=6607376733821126151; tt_webid=6607376733821126151; WEATHER_CITY=%E5%8C%97%E4%BA%AC; tt_webid=6607376733821126151; UM_distinctid=1662fc5d1b478-04aa6684af3777-8383268-1fa400-1662fc5d1b556c; csrftoken=0e079708e36d9c1eeea96125f6b6309a; uuid="w:17e8c76a5628443999604cfc1482b920"; ccid=fba911a3338ceafebd52015ebe3fb4a9; CNZZDATA1259612802=1051770912-1538395942-https%253A%252F%252Fwww.google.com.hk%252F%7C1538488870; __tasessionId=g87q247qw1538490746687',
                   'referer': 'https://www.toutiao.com/search/?keyword=%E8%A1%97%E6%8B%8D',
                   'upgrade-insecure-requests': '1',
                   'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
                   }
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print("请求索引页出现错误")
        return None
def parse_page_index(html):
    data = json.loads(html)
    if data and 'data' in data.keys():
        for item in data.get('data'):
            yield item.get('article_url')
def get_page_detail(url):
    try:
        headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                   'accept-encoding': 'gzip, deflate, br', 'accept-language': 'zh-CN,zh;q=0.9',
                   'cache-control': 'max-age=0',
                   'cookie': 'tt_webid=6607376733821126151; tt_webid=6607376733821126151; WEATHER_CITY=%E5%8C%97%E4%BA%AC; tt_webid=6607376733821126151; UM_distinctid=1662fc5d1b478-04aa6684af3777-8383268-1fa400-1662fc5d1b556c; csrftoken=0e079708e36d9c1eeea96125f6b6309a; uuid="w:17e8c76a5628443999604cfc1482b920"; ccid=fba911a3338ceafebd52015ebe3fb4a9; CNZZDATA1259612802=1051770912-1538395942-https%253A%252F%252Fwww.google.com.hk%252F%7C1538488870; __tasessionId=g87q247qw1538490746687',
                   'referer': 'https://www.toutiao.com/search/?keyword=%E8%A1%97%E6%8B%8D',
                   'upgrade-insecure-requests': '1',
                   'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
                   }
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print("请求详情页出现错误",url)
        return None
def parse_page_datail(html,url):
    soup = BeautifulSoup(html,'lxml')
    title = soup.select('title')[0].get_text()
    print(title)
    images_pattern = re.compile('gallery: JSON.parse\("(.*?)"\),', re.S)
    result = re.search(images_pattern,html)
    if result:
        data = json.loads(result.group(1).replace('\\', ''))
        if data and 'sub_images' in data.keys():
            sub_images = data.get('sub_images')
            images = [item.get('url') for item in sub_images]
            for image in images:
                download_image(image)
            return {
                'title': title,
                'url':url,
                'images': images
            }
def download_image(url):
    print('正在下载',url)
    try:
        headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                   'accept-encoding': 'gzip, deflate, br', 'accept-language': 'zh-CN,zh;q=0.9',
                   'cache-control': 'max-age=0',
                   'cookie': 'tt_webid=6607376733821126151; tt_webid=6607376733821126151; WEATHER_CITY=%E5%8C%97%E4%BA%AC; tt_webid=6607376733821126151; UM_distinctid=1662fc5d1b478-04aa6684af3777-8383268-1fa400-1662fc5d1b556c; csrftoken=0e079708e36d9c1eeea96125f6b6309a; uuid="w:17e8c76a5628443999604cfc1482b920"; ccid=fba911a3338ceafebd52015ebe3fb4a9; CNZZDATA1259612802=1051770912-1538395942-https%253A%252F%252Fwww.google.com.hk%252F%7C1538488870; __tasessionId=g87q247qw1538490746687',
                   'referer': 'https://www.toutiao.com/search/?keyword=%E8%A1%97%E6%8B%8D',
                   'upgrade-insecure-requests': '1',
                   'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
                   }
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            save_image(response.content)
        return None
    except RequestException:
        print("请求图片出错",url)
        return None

def save_image(content):
    file_path = '{0}/{1}.{2}'.format(os.getcwd(),md5(content).hexdigest(),'jpg')
    if not os.path.exists(file_path):
        with open(file_path,'wb') as f:
            f.write(content)
            f.close()
def save_to_mongo(result):
    """存储文件到数据库"""
    if db[MONGO_DB].insert(result):
        print('存储成功', result)
        return True
    return False

def main(offset):
    html = get_page_index(offset,KEY)
    for url in parse_page_index(html):
        html = get_page_detail(url)
        if html:
            result = parse_page_datail(html,url)
            if result:
                save_to_mongo(result)

if __name__ == '__main__':
    groups = [x * 20 for x in range(Group_start,Group_end + 1)]
    pool = Pool()
    pool.map(main,groups)