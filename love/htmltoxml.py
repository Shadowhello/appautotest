#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# from __future__ import unicode_literals
import os
import sys
import json
import time
from mylog import log
import utils
from bs4 import BeautifulSoup
import xml.dom.minidom


"""
使用实际的绝对路径
python manage.py htmltoxml /appautotest/files/vivo/html.json

把html.json里面配置的html文件全部转换成xml文件，放到xml目录下
同时，生成xml.json文件，记录xml目录下所有的xml文件

"""

# 流程
# 1 读取argv，获取配置html.json里 "update_app"信息
# 2 根据"update_app"的信息，依次解析里面的html


class HtmlToXML(object):

    def __init__(self, json_path_file):
        self._html_path = json_path_file.replace(os.path.basename(json_path_file),"")
        self._xml_path = os.path.join(self._html_path, '..', 'xml')
        self._json_path = json_path_file
        self._menu_level = "1"
        self._json_data = {}
        self._update_app = {}
        self._current_app=""
        

    def get_attrs(self,tag, strip = True):
        for tag_c in tag.children:
            if tag_c.name:
                if strip:
                    self._menu_level = str(len(tag_c.string) - len(tag_c.string.strip()) + 1)
                    return tag_c.string.strip().encode("utf-8")
                else:
                    return tag_c.string
    
    def format_attrs(self, tag_string):
        menu_dict = {}
        try:
            for item in tag_string.split(":"):
                if utils.PhoneElement.POINT in item:
                    menu_dict[item.split("=")[0]] = item.split("=")[1]
                    continue
                if item in utils.Action.USER_ACTION:
                    menu_dict["action"] = item
                elif "=" in item:
                    for attr in item.split(","):
                        tmp = attr.split("=")
                        if tmp[0] in utils.PhoneElement.KEY:
                            menu_dict[tmp[0]] = tmp[1]
                        else:
                            log.error("{0} key error, you can use this keys : {1}".format(tmp[0], str(utils.PhoneElement.KEY)))
                else:
                    menu_dict['menu'] = item
        except BaseException as e:
            log.error(str(e))

        return menu_dict


    def read_json_conf(self):
        if not os.path.exists(self._json_path):
            log.error("File '{0} not exists !".format(self._json_path))
            self.help()
            return False
        
        self._json_data = utils.FileOperation.load_json(self._json_path)
        html_path = self._json_data["info"]["path"]
        update_app = self._json_data["update_app"] or self._json_data["all_app"]
        if not update_app:
            log.error("JSON data is None")
            return False

        self._update_app = update_app

    
    def write_run_file(self,times=1):
        xml_list = utils.FileOperation.get_xml_files(self._xml_path)
        xml_count = len(xml_list)
        case_list=[]

        for xml in xml_list:
            case_list.append({"case":xml, "loop":times})
        data = {
            "info":{
                "count": xml_count,
                "time": utils.get_current_date() + " " + utils.get_current_time(),
                "loop": times
            },
            "cases": case_list
        }

        utils.FileOperation.store_json(os.path.join(self._xml_path, "run.json"), data)


    def write_xml(self):
        for html_file in self._update_app.keys():
            self._current_app = html_file
            html_file_path = os.path.join(self._html_path, self._update_app[html_file]['name'])
            xml_file_path = os.path.join(self._xml_path, html_file+".xml")
            soup = BeautifulSoup(open(html_file_path), "lxml")
            doc = xml.dom.minidom.Document()
            root = doc.createElement("root") # 根节点

            for c in soup.body.children:
                if not c.name:
                    continue

                if c.name == "h1": # 根节点
                    root.setAttribute('app', self.get_attrs(c)) # 添加APP名称属性
                    doc.appendChild(root)

                if c.name == "h2": # 一级菜单
                    one_node = doc.createElement('node')
                    one_node_attrs = self.format_attrs(self.get_attrs(c))
                    for key, value in one_node_attrs.iteritems():
                        one_node.setAttribute(key, value)
                    root.appendChild(one_node)

                if c.name == "h3":
                    format_menu_dict = self.format_attrs(self.get_attrs(c))
                    # print self._menu_level
                    if self._menu_level == "2": #二级菜单
                        # print "erji"
                        two_node = doc.createElement('node')
                        two_node_arrts = self.format_attrs(self.get_attrs(c))
                        for key, value in two_node_arrts.iteritems():
                            two_node.setAttribute(key, value)
                        one_node.appendChild(two_node)
                    if self._menu_level == "3": # 三级菜单
                        three_node = doc.createElement('node')
                        three_node_arrts = self.format_attrs(self.get_attrs(c))
                        for key, value in three_node_arrts.iteritems():
                            three_node.setAttribute(key, value)
                        two_node.appendChild(three_node)
                    if self._menu_level == "4": # 四级菜单
                        four_node = doc.createElement('node')
                        four_node_arrts = self.format_attrs(self.get_attrs(c))
                        for key, value in four_node_arrts.iteritems():
                            four_node.setAttribute(key, value)
                        three_node.appendChild(four_node)
                    if self._menu_level == "5": # 五级菜单
                        pass
                    if self._menu_level == "6": # 六级菜单
                        pass

            fp = open(xml_file_path, 'w')
            doc.writexml(fp, indent='\t', addindent='\t', newl='\n', encoding="utf-8")
            log.info("write "+html_file+".xml"+" success")


def translate(argv):
    h = HtmlToXML(argv)
    h.read_json_conf()
    h.write_xml()
    h.write_run_file()

