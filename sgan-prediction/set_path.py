#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 16:01:33 2021

@author: yuanwang
"""

# -*- coding: utf-8 -*-

# readme
# https://www.jianshu.com/p/527e5116cb77
# https://blog.csdn.net/moshanghuakai_pang/article/details/80213078

import sys
import os

def GetProjectPath():
    return os.path.dirname(os.path.abspath(__file__))

if __name__ == "__main__":
    
    # os.path模块主要用于文件的属性获取
    project_dir = os.path.dirname(os.path.abspath(__file__))   # refers to application_top
    
    # 获取当前目录下虽有文件夹,并添加至环境中
    list_file = os.listdir(project_dir)
    for dir in list_file:
        if dir.count('.') == 0:
            print(dir)
            # 拼接环境
            dir_child = os.path.join(project_dir, dir)
            # 添加库到环境中
            sys.path.append(dir_child)
    
    
    print(' new path:\n ---------------------- ')
    for path in sys.path:
        print(path)