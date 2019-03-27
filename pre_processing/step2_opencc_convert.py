#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : step1_opencc_convert.py
# @Author: MoonKuma
# @Date  : 2019/3/26
# @Desc  : try use opencc in the cmd window directly

import os
from utils import file_io

# note the patten difference of this file, it differs from windows to linux
default_data = 'E:\\PythonProject\\Word2Vector_test\\data\\formal_data\\test1\\zh.moegirl_1W-data.txt'
default_dict = 'E:\\PythonProject\\Word2Vector_test\data\\formal_data\\test1\zh.moegirl_1W-dict.txt'
default_conf = 'E:\\PythonProject\\opencc-1.0.4-win32\\opencc-1.0.4\\share\\opencc'
default_list = [default_data, default_dict]


def opencc_convert(target_file, conf_path, conf_type='t2s.json'):
    file_array = file_io.get_file_name(target_file, fetch='all')
    result_file = os.path.join(file_array[0], (file_array[2] + '-opencc' + file_array[3]))
    conf_file = os.path.join(conf_path, conf_type)
    if os.path.exists(target_file):
        if os.path.exists(conf_file):
            cmd = 'opencc -i %TARGET_FILE_PATH% -o %RESULT_PATH% -c %CONF_PATH%'
            cmd = cmd.replace('%TARGET_FILE_PATH%', target_file).replace('%RESULT_PATH%',
                                                                    result_file).replace('%CONF_PATH%', conf_file)
            print('Start open-cc converting, cmd:', cmd)
            os.system(cmd)
        else:
            print('[ERROR] config file not exist:', conf_file)
    else:
        print('[ERROR] target file not exist:', target_file)


def execute(data_file_list = default_list, conf_path=default_conf, conf_type='t2s.json'):
    for target_file in data_file_list:
        opencc_convert(target_file, conf_path, conf_type=conf_type)
    pass

