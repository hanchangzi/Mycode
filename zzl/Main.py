#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017骞�11鏈�13鏃�
@author: zzl
'''
import jieba  
import jieba.posseg as pseg  
import time
import chardet
import sovleText
#设定为默认的utf8编码
import sys
from types import InstanceType
reload(sys)
sys.setdefaultencoding('utf8')
print sys.getdefaultencoding()
#将文本分词,返回一个字符串
def cuttext2words(path):
    #停用词
    stopwords = {}.fromkeys(['的','你','我','他'])
    swlist=[]
    for m in stopwords:
        swlist.append(m.encode('utf8'))
    #读取数据
    f1=open(path,"rb")
    data=f1.readlines()
    st=""
    for w in data:
        st+=w
    segs = jieba.cut(st, cut_all=False)#分词
     #去除非汉字的词
    def Chinese(str):
        if u'\u4e00' <= str <= u'\u9fff':
            return True
        return False
    final = ''
    print "---------------------------------------"
    for seg in segs:
        seg=seg.encode('utf8')
        if Chinese(seg):
            final+=seg+" "
    #print chardet.detect(final.strip())
    return final.strip()
sovleText.solvetext("/home/zzl/桌面/EMdata/", "/home/zzl/桌面/dataset3/",8)