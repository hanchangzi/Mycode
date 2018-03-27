#!/usr/bin/python
# -*- coding: UTF-8 -*-
#将加密的字符串转换为int
def code2int(readpath1,readpath2,writepath1,writepath2,se):
    w1 = open(writepath1, 'w+', encoding='UTF-8')
    w2 = open(writepath2, 'w+', encoding='UTF-8')
    data1 = open(readpath1, 'r+', encoding='UTF-8').readlines()
    data2 = open(readpath2, 'r+', encoding='UTF-8').readlines()
    n1 = 1  # 记录uid序号
    n2 = 1  # 记录mid序号
    dict1 = {}  # 记录uid的字典
    dict2 = {}  # 记录mid的字典
    #处理data1
    for m in data1:
        d = m.strip().split(se)
        if dict1.get(d[0], 0) == 0:
            dict1[d[0]] = n1
            n1 += 1
        d[0]=str(dict1[d[0]])
        if dict2.get(d[1], 0) == 0:
            dict2[d[1]] = n2
            n2 += 1
        d[1] = str(dict2[d[1]])
        m1='|'.join(d)
        w1.write(m1[0:len(m1)-1]+'\n')
    #处理data2
    for m in data2:
        d = m.strip().split(se)
        if dict1.get(d[0], 0) == 0:
            dict1[d[0]] = n1
            n1 += 1
        d[0]=str(dict1[d[0]])
        if dict2.get(d[1], 0) == 0:
            dict2[d[1]] = n2
            n2 += 1
        d[1] = str(dict2[d[1]])
        m1='|'.join(d)
        w2.write(m1[0:len(m1)-1]+'\n')