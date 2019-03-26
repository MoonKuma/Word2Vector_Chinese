#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : man_string.py
# @Author: MoonKuma
# @Date  : 2019/3/26
# @Desc  : string related methods



import string

def filter_string(string_line, ban_list=list(string.printable)):
    """
    :param string_line: string to filter
    :param ban_list: characters need to be removed
    :return: filtered string
    """
    filter_line = filter(lambda x: x not in ban_list, string_line)
    return ''.join(filter_line)

