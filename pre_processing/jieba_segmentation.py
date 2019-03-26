#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : jieba_segmentation.py
# @Author: MoonKuma
# @Date  : 2019/3/25
# @Desc  : loading dicts and segmentate sentences


import jieba
import time


def jieba_cut(data_file, dict_file, save_file):
    # save file
    # save_file = 'data/formal_data/test1/zh.moegirl_1W-saved.txt'
    # dict file
    # dict_file = 'data/formal_data/test1/zh.moegirl_1W-dict.txt'
    jieba.load_userdict(dict_file)

    # allow multi-processing
    jieba.enable_parallel(4)

    # data file
    # data_file = 'data/formal_data/test1/zh.moegirl_1W-data-simpled.txt'
    t1 = time.time()
    msg = 'data_file:' + data_file
    msg += '\ndict_file:' + dict_file
    msg += '\nsave_file:' + save_file
    msg += '\nStart processing, this may cost some time, please wait...'
    print(msg)
    content = open(data_file, "rb").read()
    words = "/ ".join(jieba.cut(content))
    t2 = time.time()
    tm_cost = t2-t1
    log_f = open(save_file, "wb")
    log_f.write(words.encode('utf-8'))
    print('Finished! Speed %s bytes/second' % (len(content)/tm_cost))


def execute(data_file, dict_file, save_file):
    jieba_cut(data_file, dict_file, save_file)


