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

from __future__ import unicode_literals
from bs4 import BeautifulSoup
import os, sys

# 读取一个html文件
# BeautifulSoup("html文件", "html解释器")

base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
soup = BeautifulSoup(open(os.path.join(base_path,"test" , "wechat.html")), "lxml")

# 整个html文档内容
# print soup.title

# 获取title的值
print soup.title.string

# 获取h2中a的值
print soup.h2.a.string

# 获取h3中a的值
print soup.h3.a.string

# 获取h3的属性
print soup.h3.attrs

# 遍历子节点
for c in soup.body.children:
    print c