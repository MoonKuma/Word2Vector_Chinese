#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : jieba_segmentation.py
# @Author: MoonKuma
# @Date  : 2019/3/25
# @Desc  : loading dicts and segmentate sentences


import jieba

# dict file
dict_file = 'data/formal_data/test1/zh.moegirl_1W-dict.txt'
jieba.load_userdict(dict_file)


# allow multi-processing
jieba.enable_parallel(4)

# data file
