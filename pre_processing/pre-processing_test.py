#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : pre-processing_test.py
# @Author: MoonKuma
# @Date  : 2019/3/25
# @Desc  : testing method used in pre-processing


# read
import zipfile
import json
from urllib.parse import unquote
import string
import jieba


file_path = 'E:/PythonProject/Web_Spider/file_saved/zh.moegirl_1W.zip'
#with zipfile.ZipFile(file_path) as a_zip:

a_zip = zipfile.ZipFile(file_path)

name_list = a_zip.namelist()

a_read = a_zip.read(name_list[1]).decode('utf-8')

# save out url
start = '\'url\': \''
end = '\', \'content\''

url = a_read[a_read.find(start)+len(start): a_read.find(end)]

array = url.split('/')

title = unquote(array[len(array)-1])  # save this for further segmentation

# remove non-chinese

printable = set(string.printable)  # this returns all ascii codes

# filter(func, iterable) : filter the iterable based on func

filter_line = filter(lambda x: x not in printable, a_read)

content = ''.join(filter_line)  # python 3 return an iterable

# now content contains all chinese characters and quotes

seg_list = jieba.cut(content, cut_all=True)
print("Full Mode: " + "/ ".join(seg_list)) # don't worry, jieba will omit the quotes by itself

# but maybe, more knowledge in the dict for better segmentation


