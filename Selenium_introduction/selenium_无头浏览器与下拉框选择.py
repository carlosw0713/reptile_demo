# -*- coding: utf-8 -*-
# @Time    : 2022/10/11 17:14
# @Author  : Carlos

# 让浏览器在后台进行不在进程中显示
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# 选择框的类方法
from selenium.webdriver.support.select import Select

from selenium.webdriver.edge.options import Options


# 无头浏览器 准备好参数配置   不用记  要用的时候 到时候粘过来
opt = Options()
opt.add_argument('--headless')
opt.add_argument('disbale-gpu')  # 不显示
driver=webdriver.Edge(options=opt)  # #把参数配置设置到浏览器中


# 进入年度票房首页
driver.get('https://www.endata.com.cn/BoxOffice/BO/Year/index.html')
time.sleep(0.5)

# 生成下拉框的实例对象  Select(元素)
select_year=Select(driver.find_element(By.XPATH,'//*[@id="OptionDate"]'))
'''

options ——提供所有的选项的列表，其中都是选项的WebElement元素
all_selected_options ——提供所有被选中的选项的列表，其中也均为选项的WebElement元素
first_selected_option ——提供第一个被选中的选项，也是下拉框的默认值

select_by_index(index) ——通过选项的顺序，第一个为 0
select_by_value(value) ——通过value属性
select_by_visible_text(text) ——通过选项可见文本
'''

#  options 返回所有的选择项
print(f'所有选项：{select_year.options}')

# 网页的文本值
body=driver.find_element(By.XPATH,'//*[@id="TableList"]').text

# 通过索引选择
select_year.select_by_index(0)
print(f"\n索引0的网页文本值：{body}")
time.sleep(0.5)

# 通过value选择
select_year.select_by_value("2018")
print(f"\nvalue为2018的网页文本值：{body}")
time.sleep(0.5)

#通过text文本选择
select_year.select_by_visible_text("2008年")
print(f"\n文本值为2008年的网页文本值：{body}")
#
# 关闭浏览器
driver.close()




