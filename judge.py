#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
输入：predect的list，real的list
数据示例：predect[[count_fp,count_cp,count_lp],[...,...,...]]
输出：最终的precision
"""
def judge(predict, real):
    precision = []
    count=[]
    cp = []
    for i in range(len(predict)):
        predict[i]=[int(j) for j in predict[i].strip().split(' ')]
        real[i] = [int(z) for z in real[i].strip().split(' ')]
        dev_f = abs(predict[i][0] - real[i][0]) / (predict[i][0] + 5)  # 转发
        dev_c = abs(predict[i][1] - real[i][1]) / (predict[i][1] + 5)  # 评论
        dev_l = abs(predict[i][2] - real[i][2]) / (predict[i][2] + 2)  # 点赞
        precision.append(1 - 0.5 * dev_f - 0.25 * dev_c - 0.25 * dev_l)
        precision[i] = int(precision[i] - 0.8 + 1) #改进的符号函数
        if sum(real[i]) < 100:
        	count.append(sum(real[i]) + 1 )
        else:
       		count.append(101)
       	cp.append(precision[i]*count[i])
    precision_f = sum(cp) / sum(count)
    return precision_f
