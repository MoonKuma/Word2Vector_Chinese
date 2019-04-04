#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : gensim_test.py
# @Author: MoonKuma
# @Date  : 2019/3/27
# @Desc  : test the simplest usage of genism

import gensim
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
import multiprocessing
from utils import file_io
import os

default_target_file = 'data/formal_data/test1/zh.moegirl_1W-data-opencc-jieba.txt'
default_model = 'data/formal_data/test1/zh.moegirl_1W-data-opencc-jieba-model1.txt'
model2_file = 'data/formal_data/test2/zh.moegirl_200000-data-opencc-jieba-model1.txt'

def genism_test(target_file=default_target_file):
    # the original version on training w2v
    file_array = file_io.get_file_name(target_file, fetch='all')
    result_file_1 = os.path.join(file_array[0], (file_array[2] + '-model1' + file_array[3]))
    result_file_2 = os.path.join(file_array[0], (file_array[2] + '-model2' + file_array[3]))
    model = Word2Vec(LineSentence(target_file), size=200, window=5, min_count=5, workers=multiprocessing.cpu_count())
    model.save(result_file_1)
    model.wv.save_word2vec_format(result_file_2, binary=False)
    gensim.models.KeyedVectors.load_word2vec_format


# test reading
current_model = None
def test_model_result(model_file=default_model, test_words=u"喜欢", reset=False):
    # testing result of model
    global current_model
    if current_model is None or reset:
        current_model = Word2Vec.load(model_file)
    for element in current_model.wv.most_similar(positive=test_words):
        print(element[0],element[1])
    current_model.wv.get_keras_embedding()
#
test_model_result(model_file=model2_file,test_words=u"可爱")

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


