#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : step0_solving_environment.py
# @Author: MoonKuma
# @Date  : 2019/3/21
# @Desc  : relative method test

"""
# Solving Environment

# 1. jieba: word segmentation
# https://github.com/fxsjy/jieba
# install
# pip install jieba

# testing
import jieba
seg_list = jieba.cut("我来到北京清华大学", cut_all=True)
print("Full Mode: " + "/ ".join(seg_list))


2. gensim: NLP
# https://radimrehurek.com/gensim/tutorial.html
# install
# conda install -c conda-forge gensim

# testing
import gensim
import numpy as np
numpy_matrix = np.random.randint(10, size=[5, 2])  # random matrix as an example
corpus = gensim.matutils.Dense2Corpus(numpy_matrix)


3. OPEN-CC: convert tradition chinese into simple one
# https://github.com/BYVoid/OpenCC
# install
# OPEN CC in windows requires compiling, you may wants to download a compiled version
# win32 version download: https://pan.baidu.com/s/165qBfhMNXCnO6TZ_KJaYoA  nn3r
# testing
import os
os.system('opencc --help')
# # for use
# opencc -i %TARGET_FILE_PATH% -o %RESULT_PATH% -c %CONF_PATH%

"""

import jieba
import gensim
import os
import numpy as np

# jieba
seg_list = jieba.cut("我来到北京清华大学", cut_all=True)
print("Full Mode: " + "/ ".join(seg_list))

# gensim
numpy_matrix = np.random.randint(10, size=[5, 2])  # random matrix as an example
corpus = gensim.matutils.Dense2Corpus(numpy_matrix)

# open-cc
os.system('opencc --help')