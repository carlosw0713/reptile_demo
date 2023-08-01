from bs4 import BeautifulSoup

text='''
<title>你好啊</title>
<div class='info' float='left'>Welcome to SXT</div>
<div id='outfo' float='right'>
    <span>Good Good Study</span>
    <a href='www.bjsxt.cn'></a>
    <strong><!--没用--></strong>
</div>
'''

soup=BeautifulSoup(text,'html.parser')



# find(标签, 属性=值) # 单个、第一个
str1=soup.find('div')
str3=soup.find('a',href='www.bjsxt.cn')

# find_all(标签, 属性=值) # 多个、所有
str2=soup.find_all('div')

# 存在特殊字符的写法
str4=soup.find('div',class_='info')
str5=soup.find('div',attrs={'id':'outfo'})

# 获取属性值
str6=soup.find('div').get('class')
str7=soup.find_all('div')[1]['id']

# 注释
str10=type(soup.find('div',class_='info').text)

# soup对象
str11=soup.a
str12=soup.strong.string

# 获取文本内容
str8=soup.find('div',class_='info').text
str9=soup.find('div',class_='info').string

print("运行成功")

# 4.从bs对象中查找数据


# print(page.find_all("td",valign="top",width="99"))
# print(page.find_all("span",class_="zaikan")) # 为避嫌标签名class重复,只能class_
# print(page.find_all("span",attrs={"class":"zaikan"})) # 和上一行是一个意思. 此时可以避免class
