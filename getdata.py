#!/usr/bin/python
# -*- coding: UTF-8 -*-
#这个类是得到你想要的数据，比如对于训练数据，一共有7个类别，你想要获得前三个类别的所有数据，你就只需要传入数据的路径和0，2这两个区间的点,separator是数据分割符
#最后的数据以list[string]形式返回，
class getdata:
    def __init__(self, readpath,left,right,separator):
        self.data=open(readpath,'r+',encoding='UTF-8').readlines()
        self.left=left
        self.right=right
        self.separator=separator
    def transfer(self):
        list=[]
        for da in self.data:
            d=da.strip().split('|')
            s=''
            for i in range(self.left,self.right+1):
                s+=d[i]+' '
            s.strip()
            list.append(s)
        return list