#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : word2vector_test.py
# @Author: MoonKuma
# @Date  : 2019/3/21
# @Desc  : relative method test

# environment

# jieba Chinese word segmentation
# # pip install jieba
# testing
import jieba

seg_list = jieba.cut("我来到北京清华大学", cut_all=True)
print("Full Mode: " + "/ ".join(seg_list))  # 全模式

# gensim NLP
# # conda install -c conda-forge gensim


# OPEN CC
# OPEN CC is for translate tradition chinese characters into modern chinese characters
# OPEN CC in windows requires compiling, you may wants to download a compiled version
# after installation
# test
# opencc --help
# opencc -i TARGET_FILE_PATH -o RESULT_PATH -c CONF_PATH

# the following works on cmd
# opencc -i E:\PythonProject\Word2Vector_test\data\formal_data\test1\zh.moegirl_1W-data.txt -o E:\PythonProject\Word2Vector_test\data\formal_data\test1\zh.moegirl_1W-data-simpled.txt -c E:\PythonProject\opencc-1.0.4-win32\opencc-1.0.4\share\opencc\t2s.json
