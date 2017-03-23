#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
    测试html的解析
"""

# 安装以下第三方库 
# pip install beautifulsoup4

# 参考网址：
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html
# http://cuiqingcai.com/1319.html

# from __future__ import unicode_literals
from bs4 import BeautifulSoup
import os, sys
import xml.dom.minidom

# 读取一个html文件
# BeautifulSoup("html文件", "html解释器")

base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
soup = BeautifulSoup(open(os.path.join(base_path,"test" , "wechat.html")), "lxml")


        

# # 整个html文档内容
# # print soup.title

# # 获取title的值
# print soup.title.string

# # 获取h2中a的值
# print soup.h2.a.string

# # 获取h3中a的值
# print soup.h3.a.string.strip()

# # 获取h3的属性
# print soup.h3.attrs



def get_attrs(i, strip=False,encoding = None):
    for j in i.children:
        if j.name:
            if strip:
                j = j.string.strip()
            if encoding:
                j.string.encode(encoding)
            return j

def format_attrs(html_tag):
    r={}
    try:
        r["level"] = str(len(html_tag)-len(html_tag.strip())+1)
        t = html_tag.encode("utf-8")
        print t
        t = t.strip().split(":")
        for item in t:
            if item in ["click","longclick"]:
                r["action"] = item.encode("utf-8")
            elif "=" not in item:      
                r["menu"] = item.encode("utf-8")
            else:
                tmp = item.split("=")
                r[tmp[0]] = tmp[1]
    except:
        print "============"
        pass

    return r




doc = xml.dom.minidom.Document()
root = doc.createElement("root") # 根节点

# 因为所有的节点都是body的子节点，所以获取body子节点
for c in soup.body.children:
    if not c.name:
        continue

    if c.name == "h1": # 根节点
        root.setAttribute('app', get_attrs(c)) # 添加APP名称属性
        doc.appendChild(root)

    if c.name == "h2": # 一级菜单
        one_node = doc.createElement('node')
        one_node_attrs = format_attrs(get_attrs(c))
        for key, value in one_node_attrs.iteritems():
            one_node.setAttribute(key, value)
        root.appendChild(one_node)

    if c.name == "h3":
        format_menu_dict = format_attrs(get_attrs(c))
        print format_menu_dict["level"]
        if format_menu_dict["level"] == "2": #二级菜单
            print "erji"
            two_node = doc.createElement('node')
            two_node_arrts = format_attrs(get_attrs(c))
            for key, value in two_node_arrts.iteritems():
                two_node.setAttribute(key, value)
            one_node.appendChild(two_node)
        if format_menu_dict["level"] == "3": # 三级菜单
            three_node = doc.createElement('node')
            three_node_arrts = format_attrs(get_attrs(c))
            for key, value in three_node_arrts.iteritems():
                two_node.setAttribute(key, value)
            two_node.appendChild(three_node)
        if format_menu_dict["level"] == "4": # 四级菜单
            four_node = doc.createElement('node')
            four_node_arrts = format_attrs(get_attrs(c))
            for key, value in four_node_arrts.iteritems():
                two_node.setAttribute(key, value)
            three_node.appendChild(four_node)
        if format_menu_dict["level"] == "5": # 五级菜单
            pass
        if format_menu_dict["level"] == "6": # 六级菜单
            pass


# root.setAttribute("app", "微信")
# doc.appendChild(root)
# node_1 = doc.createElement('node')
# node_1.setAttribute('menu','sdfs')
# node_1.setAttribute('action','click')

# node_2 = doc.createElement('node')
# node_2.setAttribute('menu','+')
# node_2.setAttribute('action','click')
# node_2.appendChild(doc.createTextNode("测试"))
# node_1.appendChild(node_2)
# root.appendChild(node_1)

# t=doc.createElement('node')
# t.setAttribute('menu','我')
# t.setAttribute('action','click')
# root.appendChild(t)




fp = open('test.xml', 'w')
doc.writexml(fp, indent='\t', addindent='\t', newl='\n', encoding="utf-8")