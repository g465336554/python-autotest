"""
try:
    open("abc.txt",'r+')
    print("aa")
except BaseException:
    print("异常了")

try:
    #open("abc.txt",'r+')
    print(aa)
except BaseException as msg:
    print("异常了！！！")


try:
    aa = "异常测试："
    print("a")
except BaseException as msg:
    print(msg)
else:
    print("没有异常!!!")
"""
# s='hello{}! my name is {}.'.format('world','python')
# print (s)
# str=['hello','world']
# print(type(str))
# str1= ' '.join(str)
# print(type(str1))
# str2= '_'.join(str1)
# print(str1)
# print(str2)
# a = {'c': '1', 'b': '2'}
# z = {'n': 'hello', 'm': 'world'}
# print(type(a))
# print(a['c'])
# print(a.keys())
# print(a.values())
# x = {**a, **z}
# print(x)
# print("loop{:.2f}".format(3.1415926))
# counter = 0
# while counter <=4:
#     print('loop{}'.format(counter))
#     counter += 1
# l = []
# for i in range(1, 11):
#     l.append(i**2)
# print(l)

# filename = "D:\/pscript/test.txt"
# try:
#     fp = open (filename, "r+")
#     print(fp.read())
#     fp.close()
# except Exception as e:
#     print("文件打开失败, %s 文件不存在" % filename  )
#
#列推到
# some_list =  [1,2,3,4,5,6]
# another_list = [x+1 for x in some_list]
# # print(another_list)
# import asyncio
# import time
#
# async def shop(delay, what):
#     print(what)
#     await asyncio.sleep(delay)
#     print("...出来了")
#
# async def main():
#     task1 = asyncio.create_task(shop(8, '女朋友看衣服..'))
#     task2 = asyncio.create_task(shop(5, '体验手机..'))
#
#     print(time.ctime(), "开始逛街")
#     await task1
#     await task2
#     print(time.ctime(), "结束.")
# asyncio.run(main())
#
# some_list = [1,2,3,4,5,6,6,8,8,10]
# wvwn_set = {x for x in some_list if x % 2 ==0 }
# print(wvwn_set)
#
# d = {x:x%2 ==0 for x in range (1,11)} #字典推导
# print(d)
# import random
#
# a = random..choice([1, 2, 3, 4])
#
# print(a)

# import math
# import random
# y = random.choice([1, 20, 9, 10])
# print(y)
# if y == 9:
#     x = 10
# else:
#     x = 20
# print(x)

# import random
# b=random.randrange(1,10000)
# print(b)
# from  random import randrange
# b=randrange(10)
# list1 = ["packers", "49ers"]
# list2 = ["lu", "na"]
# for teama, teamb in zip(list1, list2):
#     print(teama +"  " + teamb)
# print(b)
#
# list1 = ["a","j",'m']
# list2 = [1,3,55]
# c=dict (zip (list1,list2))
# print(c)
# teams = ["aaaa","bbnnb","asdjasjdasjd","asdjkl"]
# for index, team in enumerate(teams):
#     print (index, team)
# seq = ['one', 'two', 'three']
# for index,element in enumerate(seq):
#     print(index,element)
# from itertools import combinations
# list1 = ["aaaa","bbnnnn","bbbbbbb"]
# for i in  combinations (list1,2):
#     print(i)

# from itertools import permutations
# els_list = [1, 2, 3, 4, 5]
# for els in permutations(els_list, 3):
# #     print(els)
# from collections import Counter  #统计元素出现次数
# c= Counter("hello world ,hahahahao")
# print(c)
# d=c.most_common(2)
# print(d)
# print(c.most_common(2))
# from collections import Counter
# nums=[1,2,2,3,4,4,5.5,7,8,9,8,9]
# print(Counter(nums).most_common(2))
# for i in range (10): 输出结果横向显示
#     print (i,end=",")
# import itertools
# from  itertools import  chain
# test= [[1,-2],[-9,9],[7,0],[44,'a']]
# print(list(itertools.chain.from_iterable(test)))
# test1 = chain("aaa","bbbbb","asd")
# print (list(test1))
# list1= [1,2,3,4,5,6,7]
# list2 = [4,5,6,7,8,9]
# d = set (list1).intersection( set (list2))
# print(d)
# f = set (list1).difference(set(list2))
# g = set (list1).symmetric_difference(set(list2))
# print("f:",f,"g:",g)

# li = [11,22,33,44,55,66,77,11,22,33]
# set = set(li)
# print(set)
# print(type(set))
# li = list (set)
# print(li)
# print(type(li))
#
from time import  sleep,ctime
import threading
# 音乐播放器
def music (func, loop):
    for i in range(loop):
        print("I was listening to %s!%s"% (func, ctime()))
        sleep(2)
# 视频播放器
def movie(func, loop):
    for i in range (loop):
        for i in range(loop):
            print("I was at the %s! %s"% (func, ctime()))
            sleep(5)
# 创建线程
threads = []
#创建线程t1，并添加到线程数组
t1 = threading.Thread(target=music, args= ('爱情买卖',2))
threads.append(t1)
#创建线程t2，并添加到线程数组
t2 = threading.Thread(target= movie, args= ('阿凡达',2))
threads.append(t2)

if __name__ == '_main_':
    # 启动线程
    for t in threads:
        t.start()
        # 守护线程
    for t in threads:
        t.join()
    print('all end:%s'% ctime())
