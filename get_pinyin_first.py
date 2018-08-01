# -*- coding: utf-8 -*-
# @Author: lim
# @Date:   2018-07-27 09:24:33
# @Last Modified by:   lim
# @Last Modified time: 2018-07-27 16:42:02


def get_cn_first_letter(_str,codec="UTF8"):

    """
    1 return a alphabet of Chinese by gbk index.
    2.over gbk index will return '' 
    3.alphabet and _ will return themselves """
    
    _str = _str.encode("GBK")
    
    if _str<b"\xb0\xa1" or _str>b"\xd7\xf9":
        hook = _str.decode('GBK')
        if hook not in 'abcdefghijklmnopqrstuvwxyz_':
            hook = ''
        return hook
    if _str<b"\xb0\xc4":
        return "a"
    if _str<b"\xb2\xc0":
        return "b"
    if _str<b"\xb4\xed":
        return "c"
    if _str<b"\xb6\xe9":
        return "d"
    if _str<b"\xb7\xa1":
        return "e"
    if _str<b"\xb8\xc0":
        return "f"
    if _str<b"\xb9\xfd":
        return "g"
    if _str<b"\xbb\xf6":
        return "h"
    if _str<b"\xbf\xa5":
        return "j"
    if _str<b"\xc0\xab":
        return "k"
    if _str<b"\xc2\xe7":
        return "l"
    if _str<b"\xc4\xc2":
        return "m"
    if _str<b"\xc5\xb5":
        return "n"
    if _str<b"\xc5\xbd":
        return "o"
    if _str<b"\xc6\xd9":
        return "p"
    if _str<b"\xc8\xba":
        return "q"
    if _str<b"\xc8\xf5":
        return "r"
    if _str<b"\xcb\xf9":
        return "s"
    if _str<b"\xcd\xd9":
        return "t"
    if _str<b"\xce\xf3":
        return "w"
    if _str<b"\xd1\x88":
        return "x"
    if _str<b"\xd4\xd0":
        return "y"
    if _str<b"\xd7\xf9":
        return "z"


def get_pinyin_name(word1,word2,flag):  
    """return all first alphabet of all Chinese"""

    pinyin = ''
    word = word1 + '_' + word2
    for i in word:
        pinyin+=get_cn_first_letter(i)
    if flag == '0':
        return pinyin.replace('-','_')+'_content.js'
    if flag == '1':
        return pinyin.replace('-','_')+'_source.js'



