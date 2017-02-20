#! -*- coding:utf-8 -*-

def string_to_int(s:str) -> int:
    try:
        return int(s)
    except:
        return -1
