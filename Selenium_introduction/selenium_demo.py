# -*- coding: utf-8 -*-
# @Time    : 2022/11/14 14:09
# @Author  : Carlos
import time


from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


# 导入模块
from selenium import webdriver

# 浏览器启动配置
def option_use(url):

    # ChromeOptions是chromedriver支持的浏览器启动选项。
    opt = webdriver.ChromeOptions()

    # 启动参数：
    # # 1.获取浏览器cookies储存的路径 浏览器搜索 ”Edge//version/ “  C:\Users\carlos\AppData\Local\Microsoft\Edge\User Data\Default
    # # 我们去掉后面的 \Default，然后在路径前加上「–user-data-dir=」就拼接出我们要的路径了。
    # profile_directory = r'--user-data-dir=C:\Users\carlos\AppData\Local\Microsoft\Edge\User Data'
    profile_directory = (r" user-data-dir=C:\Users\carlos\AppData\Local\Google\Chrome\User Data")  # 把数据传入程序
    opt.add_argument(profile_directory)

    # 设置为 headless 模式 无头浏览器
    # opt.add_argument('--headless')

    # 隐身模式(无痕模式)
    # opt.add_argument('incognito')

    # 禁用GPU
    opt.add_argument('--disable-gpu')

    # 设置窗口大小
    opt.add_argument("window-size=1024,768")

    # 彻底停用沙箱。
    opt.add_argument("--no-sandbox")

    # 防止网站发现我们使用模拟器 规避检测
    opt.add_experimental_option('excludeSwitches', ['enable-automation'])

    # 创建浏览器对象
    driver = webdriver.Chrome(chrome_options=opt)

    driver.get(url)

    time.sleep(1)

    return driver

# 选择框操作
def select_ues(wb):

    # 获取元素
    element1 = wb.find_element(By.XPATH, '//*[@id="OptionDate"]')  # select框对象

    # 获取文本值
    text = element1.text

    # 生成下拉框的实例对象  Select(元素)
    from selenium.webdriver.support.select import Select

    # 生成选择框对象
    select_obj=Select(element1)

    # 返回所有下拉框对象
    select_all=select_obj.options

    #通过索引选择
    select_obj.select_by_index(2)
    time.sleep(2)

    # 通过value选择
    select_obj.select_by_value("2021")
    time.sleep(2)

    #通过text文本选择
    select_obj.select_by_visible_text("2012年")
    time.sleep(2)

# 窗口操作
def handle_ues(wb):


    # 打开一个新的窗口
    wb.execute_script('window.open("https://www.endata.com.cn/BoxOffice/BO/Year/index.html")')


    # 切换窗口 索引切换
    wb.switch_to.window(wb.window_handles[-1])
    time.sleep(2)

    # 执行选择框操作
    select_ues(wb)

    #回退
    wb.back()
    time.sleep(2)

    # 前进
    wb.forward()
    time.sleep(2)

    # 刷新当前页面
    wb.refresh()
    time.sleep(1)

    wb.set_window_size(1000, 800)
    time.sleep(2)

    # 关闭当前窗口页面
    wb.close()

# 获取页面页面信息
def get_page_infomation(wb):

    # 切换到最后一页
    wb.switch_to.window(wb.window_handles[-1])

    # 获取页面标题
    title = wb.title

    # 生成当前页面快照并保存
    picture = wb.save_screenshot("页面快照.png")

    # 打印网页渲染后的源代码
    source_code = wb.page_source

    # 获取当前页面Cookie
    cookie = wb.get_cookies()

    # 获取当前url
    url = wb.current_url

    #打印
    print('页面信息获取成功')


def login(wb):


    # 点击登录
    wb.find_element(By.XPATH,'//section/section[2]/button/span').click()
    time.sleep(0.5)

    # 点击切换密码登录
    wb.find_element(By.XPATH,'//section/ul/li[2]').click()
    time.sleep(0.5)

    # 输入用户名密码
    wb.find_element(By.XPATH,'//section/form/div[1]/div/div/input').send_keys('13142392973')

    wb.find_element(By.XPATH,'//section/section/form/div[2]/div/div/input').send_keys('whm51921')

    # 点击登录
    wb.find_element(By.XPATH,'//section/section/div[2]/button').click()

    time.sleep(2)

# 基础用法
def basic_ues():
    url='https://ys.endata.cn/DataMarket/Index'

    # 调用配置函数
    wb=option_use(url)

    #页面最小化
    wb.minimize_window()
    time.sleep(1)
    #页面最大化
    wb.maximize_window()

    # 登录
    login(wb)

    # input 文本呢输入
    wb.find_element(By.XPATH,'//*[@id="app"]/header/section/section/section[1]/div/input').send_keys("独行月球66666")
    time.sleep(2)

    # 清空文本
    wb.find_element(By.XPATH, '//*[@id="app"]/header/section/section/section[1]/div/input').clear()
    wb.find_element(By.XPATH, '//*[@id="app"]/header/section/section/section[1]/div/input').send_keys("独行月球")

    # .click 元素点击 暂时搞不了，建议打断点，手动登录后
    # wb.find_element(By.XPATH,'//*[@id="app"]/header/section/section/section[1]/div/span/span/label/svg/use').click()
    time.sleep(0.5)
    wb.find_element(By.XPATH,'//span/span/label').click()
    time.sleep(3)

    wb.find_element(By.XPATH,'//section/section/ul/li/a/span').click()
    time.sleep(2)

    from selenium.webdriver import Keys
    # Keys.RETURN操作
    # wb.find_element(By.XPATH,'/html/body/section/section/main/div/div[1]/div/section/section[2]/section/div/label[2]/span').send_keys(Keys.RETURN)

    # 获取页面信息
    get_page_infomation(wb)

    # 窗口操作
    handle_ues(wb)

    print('运行成功')

    time.sleep(5)

    wb.quit()

    return wb

# 跳过验证码登录
def login_tomtoc():
    url='https://www.tomtoc.cn/'

    # 调用配置函数
    wb=option_use(url)

    #页面最小化
    wb.minimize_window()
    time.sleep(1)
    #页面最大化
    wb.maximize_window()
    time.sleep(5)

    # 关闭浏览器
    wb.quit()


# 切换 alert 窗口（弹窗）
def alert_handle():
    url='https://www.w3school.com.cn/tiy/t.asp?f=hdom_prompt'

    # 调用配置函数
    driver = option_use(url)

    # 切换进iframe
    driver.switch_to.frame("iframeResult")
    time.sleep(0.5)

    # 要让alert出现
    driver.find_element(By.XPATH,'//input[@type="button"]').click()

    # 切换到alert
    alert = driver.switch_to.alert


    # 在弹出框当中输入文本内容 还有问题
    # alert.send_keys("hello selenium")
    # time.sleep(2)

    # 获取当前弹框的文本内容
    text=alert.text
    print(text)


    # 切换到主文档

    # driver.switch_to.default_content()
    # print(driver.page_source)

    # 关闭浏览器
    driver.quit()

    # 切换到 confirm确认框
    # 与警告框不同，确认框还有取消按钮

    # 调用配置函数
    url = 'https://www.w3school.com.cn/tiy/t.asp?f=hdom_confirm'
    driver = option_use(url)


    time.sleep(1)

    # 切换进iframe
    driver.switch_to.frame("iframeResult")
    time.sleep(0.5)


    # 要让alert出现
    driver.find_element(By.XPATH,'//input[@type="button"]').click()

    # 切换到alert
    alert = driver.switch_to.alert

    # 获取当前弹框的文本内容
    text = alert.text
    print(text)

    #取消
    alert.dismiss()
    time.sleep(1)


    # 要让alert出现
    driver.find_element(By.XPATH,'//input[@type="button"]').click()

    # 获取当前弹框的文本内容
    text = alert.text
    print(text)

    # 确认
    alert.accept()
    time.sleep(1)


    time.sleep(10)
    driver.quit()


# 运行文件
# basic_ues()

# 验证跳过验证码登录
# login_tomtoc()

'''页面的弹出框2种：
1）右键元素定位
2）js弹框 – 由页面操作触发的。
WebDriver提供了一个API，用于处理JavaScript提供的三种类型的原生弹窗消息'''
# 切换 alert 窗口（弹窗）
# alert_handle()
wb=webdriver.Edge()

wb.get("https://www.baidu.com")

wb.get("https://www.csdn.net")

wb.execute_script("window.open('https://www.baidu.com')")




