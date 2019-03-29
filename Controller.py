#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : Controller.py
# @Author: MoonKuma
# @Date  : 2019/3/25
# @Desc  : Controller is for testing each method

from pre_processing import step1_word_crop_preprocessing
from pre_processing import step2_opencc_convert,step3_jieba_segmentation
from word2vector_test import gensim_test
import time

# test word crop pre-processing

# step1_word_crop_preprocessing.merge_data_file()
# step2_opencc_convert.execute()

# step3_jieba_segmentation.execute(test_times=-1)

# test gensim
# gensim_test.genism_test()

# test gensim add on
# gensim_test.genism_add_on()


default_path = 'E:/PythonProject/Web_Spider/file_saved/zh.moegirl_1W.zip'
file_save_path = 'data/formal_data/test1'

test_data_path2 = 'E:/PythonProject/Web_Spider/file_saved/zh.moegirl_200000.zip'
test_file_save_path = 'data/formal_data/test2'

default_conf = 'E:\\PythonProject\\opencc-1.0.4-win32\\opencc-1.0.4\\share\\opencc'


def process_pipeline(data_file_path=default_path, save_path=file_save_path, opencc_config_path=default_conf):
    # test process pipeline
    t0 = time.time()
    print('[Start]data_file_path=',data_file_path,',save_path=',file_save_path,'opencc_config_path=',opencc_config_path)

    save_name_dict, save_name_data = step1_word_crop_preprocessing.merge_data_file(data_file_path=data_file_path,
                                                                                   save_path=save_path)
    print('[step1_word_crop_preprocessing finished] save_name_dict=', save_name_dict, ',save_name_data=',
          save_name_data,',time cost:',time.time()-t0)

    opencc_data, opencc_dict = step2_opencc_convert.execute(data_file=save_name_data, dict_file=save_name_dict,
                                                            conf_path=opencc_config_path)
    print('[step2_opencc_convert finished] opencc_data=', opencc_data, ',opencc_dict=',opencc_dict,',time cost:',
          time.time()-t0)

    jieba_result = step3_jieba_segmentation.execute(data_file=opencc_data, dict_file=opencc_dict, test_times=-1)
    print('[step3_jieba_segmentation finished] jieba_result=', jieba_result,',time cost:',time.time()-t0)

    gensim_test.genism_test(jieba_result)
    print('[gensim_test finished]',',time cost:',time.time()-t0)


process_pipeline(data_file_path=test_data_path2,save_path=test_file_save_path)