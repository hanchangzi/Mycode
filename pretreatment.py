#-*- coding: UTF-8 -*-
import time
import numpy as np
import jieba
import re
import jieba
#一个数据预处理类
class pretreatment:
    #readpath是原始文件的路径,writepath是写入文件的路径,separator是原始文件中的分隔符
    def __init__(self,readpath,writepath,separator):
        self.data=open(readpath,'r+',encoding='UTF-8').readlines()
        self.writepath=writepath
        self.separator=separator
    #对字符串进行预处理，删除标点符号,网址链接(以http/https为开始,一直删除到不是英文字符或者数字字符为止)
    def solvestring(self,string):
        list=string.split(' ')
        List=[]

        for m in list:
            #去除[]以及其中间内容
            if m.count('[')>0 and m.count(']')>0:
                n0 = re.search('\[', m).span()[0]
                n1 = re.search('\]', m).span()[1]
                mm=m[0:n0]+m[n1:len(m)]
                if mm.count('http')==0:
                    List.append(mm)
                    continue
                else:
                    m=mm
            # 去除链接以http/https开头
            if m.count('http')>0:
                url=m
                item = re.search('https*', url).span()
                n0 = item[0]
                n1 = item[1]
                n = len(url)
                for i in range(n1, len(url)):
                    if ord(url[i]) < 128 or url[i].isdigit() or url[i]=='/' or url[i]==':' or url[i]=='.':
                        continue
                    else:
                        n = i
                        break
                m = url[0:n0] + url[n:len(url)]
                List.append(m)
                continue

            List.append(m)
        #去除符号
        line = re.sub('[^\w\u4e00-\u9fff]+', ' ', '.'.join(List))
        #字符串是以空格为间隔,如果一个位置里面只有一个字符,为数字或者英文字母,则删除他
        list=line.split(' ')
        for a in list:
            if len(a)==1 and (ord(a)<128 or a.isdigit()):
                list.remove(a)
        line=' '.join(list)
        return line
    #对数据进行分词，这里采用得是精确模式
    def cutwords(self, text):
        #停用词典
        stopdict = {'的': 1, '得': 1, '地': 1, '你': 1, '我': 1, '他': 1, '你们': 1, '我们': 1, '他们': 1, '了': 1, '吧': 1}
        list = []

        seg_list = jieba.cut(text)
        for m in seg_list:
            if stopdict.get(m, -1) == -1 and m.count(' ') == 0:
                list.append(m)
        return ' '.join(list)
    #转换整个数据集  method代表要处理得方法，pre是预处理，cut是分词，ALL是pre和cut都进行一次
    def transfer(self,method):
        wfile=open(self.writepath,'w+',encoding='UTF-8')
        for da in self.data:
            d = da.split(self.separator)
            if method=='pre':#预处理，去除符号以及url
                d[len(d) - 1] = self.solvestring(d[len(d) - 1].strip())
            if method=='cut':#对数据进行分词
                d[len(d) - 1] = self.cutwords(d[len(d) - 1].strip())
            if method=='ALL':#将所有操作进行一次
                d[len(d) - 1] = self.solvestring(d[len(d) - 1].strip())
                d[len(d) - 1] = self.cutwords(d[len(d) - 1].strip())
            m='|'.join(d[0:len(d)])
            wfile.write(m+'\n')
