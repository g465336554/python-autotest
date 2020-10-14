from threading import Thread
from selenium import webdriver
from time import ctime,sleep

# 测试用例
def test_baidu(brower, search):
    print('start:%s' %ctime())
    print('brower:%s ,'% brower)
    if brower == "ie":
        driver= webdriver.Ie()
    elif brower == "chrome":
        driver = webdriver.Chrome()
    elif brower == "ff":
        driver = webdriver.Firefox()
    else:
        print("brower参数有误，只能为ie、ff、chrome")
    driver.get('http://www.baidu.com')
    driver.find_element_by_id("kw").send_keys(search)
    driver.find_element_by_id("su").click()
    sleep(2)
    driver.quit()
if __name__ == '__main__':
    # 启动参数（指定浏览器与百度内容）
    lists = {'chrome':'threading','ie':'webdriver','ff':'python'}
    threads=[]
    files = range(len(lists))
    print(files)
    # 创建线程
    for brower, search in lists.items():
        t = Thread(target=test_baidu,args=(brower,search))
        threads.append(t)
    # 启动线程
    for t in files:
        threads(t).start()
    for t in files:
        threads(t).join()
    print('end:%s' %ctime())
