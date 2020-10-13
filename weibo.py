from selenium import webdriver
import time

# 注意这里使用了我本机的谷歌浏览器驱动
browser = webdriver.Chrome(
    executable_path='/Users/chenqionghe/.wdm/drivers/chromedriver/79.0.3945.36/mac64/chromedriver')
# 设置用户名、密码
username = "你的用户名"
password = "你的密码"

# 打开微博登录页
browser.get('https://passport.weibo.cn/signin/login')
browser.implicitly_wait(5)
time.sleep(1)

# 填写登录信息：用户名、密码
browser.find_element_by_id("loginName").send_keys(username)
browser.find_element_by_id("loginPassword").send_keys(password)
time.sleep(1)

# 点击登录
browser.find_element_by_id("loginAction").click()
time.sleep(1)

# 通过人机验证，找到那个小点点击一下
browser.find_element_by_class_name("geetest_radar_tip").click()

# 打开我们的中公题库君的首页
browser.get('https://m.weibo.cn/u/5430882137')

# 加关注
follow_button = browser.find_element_by_xpath('//div[@class="m-add-box m-followBtn"]')
follow_button.click()
time.sleep(1)
# 这时候弹出了选择分组的框，定位取消按钮
group_button = browser.find_element_by_xpath('//a[@class="m-btn m-btn-white m-btn-text-black"]')
group_button.click()
time.sleep(1)

# 这时候我们就关注成功了，好，接下来，我们给题库君点赞和评论一下
# 找到第二条微博，因为第一条微博都是置顶的
second_weibo = browser.find_element_by_xpath("//div[@class='card m-panel card9 weibo-member card-vip'][3]")
second_weibo.text
js = "arguments[0].scrollIntoView();"
# 将下拉滑动条滑动到当前div区域
browser.execute_script(js, second_weibo)

# 给第二条微博点赞
selector = "//div[@class='card m-panel card9 weibo-member card-vip'][2]//footer/div[@class='m-diy-btn m-box-col m-box-center m-box-center-a'][3]"
a = browser.find_element_by_xpath(selector)
a.click()

# 定位第二条微博的评论处,点击
selector = "//div[@class='card m-panel card9 weibo-member card-vip'][2]//footer/div[@class='m-diy-btn m-box-col m-box-center m-box-center-a'][2]"
a = browser.find_element_by_xpath(selector)
text = a.text
a.click()

# 输出评论内容
wishes = "I’m super saiyan, best wishes to you !"
if text == '评论':
    # 光标定位到发表评论处
    comment = browser.find_element_by_tag_name('textarea')
    comment.click()
    # 输入评论内容
    comment.send_keys(wishes)
    time.sleep(1)
    # 定位发送按钮
    sendBtn = browser.find_element_by_class_name('m-send-btn')
else:
    # 光标定位到发表评论处
    focus = browser.find_element_by_css_selector('span[class="m-box-center-a main-text m-text-cut focus"]')
    focus.click()
    # 点击评论
    comment = browser.find_element_by_tag_name('textarea')
    comment.click()
    # 输入评论内容
    comment.send_keys(wishes)
    # 定位发送按钮
    sendBtn = browser.find_element_by_class_name('btn-send')

# 发表评论
sendBtn.click()