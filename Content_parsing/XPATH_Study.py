# -*- coding: utf-8 -*-
# @Time    : 2022/9/19 18:17
# @Author  : Carlos

from lxml import etree
xml = """
<book>
    <id>1</id>
    <name>野花遍地香</name>
    <price>1.23</price>
    <nick>臭豆腐</nick>
    <author>
        <nick id="10086">周大强</nick>
        <nick id="10010">周芷若</nick>
        <nick class="joy">周杰伦</nick>
        <nick class="jolin">蔡依林</nick>
        <div>
            <nick>热热热热热1</nick>
        </div>
        <span>
            <nick>热热热热热2</nick>
        </span>
    </author>
    <partner>
        <nick id="ppc">胖胖陈</nick>
        <nick id="ppbc">胖胖不陈</nick>
    </partner>
</book>
"""
tree=etree.HTML(str(xml))
tree=etree.XML(xml)

result1=tree.xpath("//book/author/nick") #元素值
result2=tree.xpath("//book/author/nick/text()") # text()获取元素文本
result3=tree.xpath("//book/author//nick/text()") # //相对路径下所有
result4=tree.xpath("//book/author/*/nick/text()") # *通配符，代表任意标签下
result9=tree.xpath("//book/author//nick[2]/text()") # nick[2]表示第二个

print(f"1{result1}\n"
      f"2{result2}\n"
      f"3{result3}\n"
      f"4{result4}\n"
      f"9{result9}")

result5=tree.xpath("//author")
for it in result5:
      print(it)
      result6=it.xpath("./nick/@id") # @id,表示获取id的属性值
      result7=it.xpath("./nick/text()")  # text()获取元素文本
      print(f"6{result6}\n"
            f"7{result7}\n")