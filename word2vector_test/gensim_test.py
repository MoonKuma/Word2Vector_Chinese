#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : gensim_test.py
# @Author: MoonKuma
# @Date  : 2019/3/27
# @Desc  : test the simplest usage of genism

from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
import multiprocessing
from utils import file_io
import os

default_target_file = 'data/formal_data/test1/zh.moegirl_1W-data-opencc-jieba.txt'
default_model = 'data/formal_data/test1/zh.moegirl_1W-data-opencc-jieba-model1.txt'


def genism_test(target_file=default_target_file):
    # the original version on training w2v
    file_array = file_io.get_file_name(target_file, fetch='all')
    result_file_1 = os.path.join(file_array[0], (file_array[2] + '-model1' + file_array[3]))
    result_file_2 = os.path.join(file_array[0], (file_array[2] + '-model2' + file_array[3]))
    model = Word2Vec(LineSentence(target_file), size=200, window=5, min_count=5, workers=multiprocessing.cpu_count())
    model.save(result_file_1)
    model.wv.save_word2vec_format(result_file_2, binary=False)


# test reading
def test_model_result(model_file=default_model, test_words=u"娘"):
    # testing result of model
    model = Word2Vec.load(model_file)
    for element in model.wv.most_similar(test_words):
        print(element[0],element[1])


# add on training
def genism_add_on(model_file=default_model, target_file=default_target_file):
    file_array = file_io.get_file_name(target_file, fetch='all')
    result_file_1 = os.path.join(file_array[0], (file_array[2] + '-add_on-model1' + file_array[3]))
    result_file_2 = os.path.join(file_array[0], (file_array[2] + '-add_on-model2' + file_array[3]))
    # add on training
    model = Word2Vec.load(model_file)
    # you need to count out the sentences of add on crops
    examples = file_io.count_lines(target_file)
    # also the epochs need to be specified
    model.train(LineSentence(target_file), total_examples=examples, epochs=model.iter)
    model.save(result_file_1)
    model.wv.save_word2vec_format(result_file_2, binary=False)

