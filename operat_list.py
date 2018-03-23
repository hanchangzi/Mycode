#!/usr/bin/python
# -*- coding: UTF-8 -*-
#列表的操作类
class operat_list:
    def __init__(self, a,b):
        self.a=a
        self.b=b
    #求交集
    def intersection(self):
        return list(set(self.a).intersection(set(self.b)))
    #求并集
    def union(self):
        return list(set(self.a).union(set(self.b)))
    #求差集
    def difference(self):
        return list(set(self.a).difference(set(self.b)))
