#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : jieba_segmentation.py
# @Author: MoonKuma
# @Date  : 2019/3/25
# @Desc  : loading dicts and segmentate sentences


import jieba
import time
from utils import file_io
import os
import traceback

default_data = 'data/formal_data/test1/zh.moegirl_1W-data-opencc.txt'
default_dict = 'data/formal_data/test1/zh.moegirl_1W-dict-opencc.txt'


def jieba_cut(data_file, dict_file, test_times=10):

    file_array = file_io.get_file_name(data_file, fetch='all')
    result_file = os.path.join(file_array[0], (file_array[2] + '-jieba' + file_array[3]))


    # try add dict in the following way

    with open(dict_file, 'r', encoding='utf-8') as dict_file_op:
        for line in dict_file_op.readlines():
            line = line.strip()
            try:
                if len(line)<=5:
                    jieba.add_word(line)
            except:
                print('[WRONG ADDING]', line)
                print(traceback.format_exc())

    # only posix system(linux) allow multi-processing
    # jieba.enable_parallel(4)

    t1 = time.time()
    msg = 'data_file:' + data_file
    msg += '\ndict_file:' + dict_file
    msg += '\nsave_file:' + result_file
    msg += '\nStart processing, this may cost some time, please wait...'
    print(msg)
    count_down=test_times
    with open(data_file, "r", encoding='utf-8') as data_content:
        with open(result_file, "w", encoding='utf-8') as result:
            line = data_content.readline()
            while line:
                line = line.strip()
                words = jieba.cut(line)
                string_list = list()
                for word in words:
                    if word!='' and word!=' ':
                        string_list.append(word)
                if len(string_list)>0:
                    str2wri = ' '.join(string_list) + '\n'
                    result.write(str2wri)
                if test_times>0:
                    count_down -= 1
                    if count_down<0:
                        break
                line = data_content.readline()

    t2 = time.time()
    tm_cost = t2-t1
    print('Finished! time cost: %s second' % str(tm_cost))


def execute(data_file=default_data, dict_file=default_dict, test_times=10):
    jieba_cut(data_file, dict_file, test_times=test_times)


