#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : step1_word_crop_preprocessing.py
# @Author: MoonKuma
# @Date  : 2019/3/25
# @Desc  : read data from *.zip, save url into url dict, removing non-chinese characters and save content

import os
import zipfile
from urllib.parse import unquote
from utils.man_string import filter_string,select_reg
from utils.file_io import get_file_name, save_iterable
import traceback

default_path = 'E:/PythonProject/Web_Spider/file_saved/zh.moegirl_1W.zip'
file_save_path = 'data/formal_data/test1'
start = '\'url\': \''
end = '\', \'content\''

# some message are regarded as redundant
msg_redundant = ['萌娘百科万物皆可萌的百科全书你好～！欢迎来到萌娘百科！如果您是第一次来到这里，点这里加入萌娘百科欢迎具有翻译能力的同学～有意者请点→需要翻译的条目←如果您在萌娘百科上发现某些内容错误空缺，请勇于修正添加！编辑萌娘百科其实很容易！觉得萌娘百科有趣的话，请推荐给朋友哦～萌娘百科群欢迎加入，加入时请写明【萌娘百科自己的】～萌娘百科群组已经建立，请点此加入！',
                 '萌娘百科，万物皆可萌的百科全书！',
                 '转载请以链接形式标注源地址，并写明转自萌娘百科。',
                 '导航、搜索',
                 '萌娘百科欢迎您参与完善本条目☆欢迎正在阅读这个条目的您协助编辑本条目。编辑前请阅读入门或条目编辑规范，并查找相关资料。萌娘百科祝您在本站度过愉快的时光。',
                 '基本资料',
                 '萌娘百科萬物皆可萌的百科全書你好～！歡迎來到萌娘百科！如果您是第一次來到這裡，點這裡加入萌娘百科歡迎具有翻譯能力的同學～有意者請點→需要翻譯的條目←如果您在萌娘百科上發現某些內容錯誤空缺，請勇於修正添加！編輯萌娘百科其實很容易！覺得萌娘百科有趣的話，請推薦給朋友哦～',
                 '萌娘百科群歡迎加入，加入時請寫明【萌娘百科自己的】～萌娘百科群組已經建立，請點此加入！',
                 '']

def merge_data_file(data_file_path=default_path, save_path=file_save_path):
    save_name_dict = os.path.join(save_path, get_file_name(data_file_path) + '-dict.txt')
    save_name_data = os.path.join(save_path, get_file_name(data_file_path) + '-data.txt')
    save_name_error = os.path.join(save_path, get_file_name(data_file_path) + '-error.txt')
    word_set = set()
    error_set = set()
    with open(save_name_data,'w', encoding='utf-8') as data_save:
        with zipfile.ZipFile(data_file_path) as z_file:  # to ensure closure
            name_list = z_file.namelist()
            for name in name_list:
                try:
                    title, clean_a = _handel_one_file(z_file, name)
                    if title is not None and title!="":
                        word_set.add(title)
                    if clean_a is not None and clean_a!="":
                        str2wri = clean_a.strip() + '\n'
                        data_save.write(str2wri)
                except:
                    msg = '[ERROR] in file:' + name
                    error_set.add(name)
                    print(msg, traceback.format_exc())
    save_iterable(file_path=save_name_dict, iterable=word_set, split='\n')
    save_iterable(file_path=save_name_error, iterable=error_set, split='\n')


def _handel_one_file(z_file,name):
        title = None
        clean_a = None
        print('processing:', name)
        if str(name).endswith('.txt'):  # if data
            a_read = z_file.read(name).decode('utf-8')
            # save into word set
            title = None
            if a_read.find(start) and a_read.find(end) and a_read.find(end) > a_read.find(start) + len(start):
                url = a_read[a_read.find(start) + len(start): a_read.find(end)]
                array = url.split('/')
                title = unquote(array[len(array) - 1])
                title = select_reg(title,splitter='')
            # clean current line
            clean_a = filter_string(a_read)
            for red in msg_redundant:
                clean_a = clean_a.replace(red, '')
            clean_a = select_reg(clean_a)
        return title, clean_a


