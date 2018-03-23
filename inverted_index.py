#!/usr/bin/python
# -*- coding: UTF-8 -*-
#构建倒排索引，readpath是数据路径，writepath是倒排索引文件的路径，sparator是分隔符  倒排索引中有用户id，微博id，和三个数的和，以空格分隔
class inverted_index:
    def __init__(self,readpath,writepath,separator):
        self.data=open(readpath,'r+',encoding='UTF-8').readlines()
        self.writepath=writepath
        self.separator=separator
    def transfer(self):
        wfile=open(self.writepath,'w+',encoding='UTF-8')
        worddict={}
        m=0
        for da in self.data:
            dd=da.strip().split('|')
            d=dd[len(dd)-1].split(' ')
            num=str(int(dd[3])+int(dd[4])+int(dd[5]))
            um=dd[0]+' '+dd[1]+' '+num
            for m in d:
                if worddict.get(m,0)==0:
                    list=[]
                    list.append(um)
                    worddict[m]=list
            else:
                    worddict[m].append(um)
        for m in worddict.items():
            s=m[0]+' '+str(m[1])+'\n'
            wfile.write(m)