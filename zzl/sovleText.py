#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import sys
import chardet
from types import InstanceType
reload(sys)
sys.setdefaultencoding('utf8')
import Main
#将文件分词处理,一个类别的文件写入一个文件
def eachFile(filepath,writepath):
    f2=open(writepath,"wb")
    pathDir =  os.listdir(filepath)
    for allDir in pathDir:
        child = os.path.join('%s%s' % (filepath, allDir))
        f1=open(child,"rb")
        st=Main.cuttext2words(child)
        #print chardet.detect(st)
        f2.write(st+"\n")
        print child
#所有文件写入一个文件
def eachFile2(filepath,writepath):
    b = open(writepath,'wb')
    pathDir =  os.listdir(filepath)
    for allDir in pathDir:
        child = os.path.join('%s%s' % (filepath, allDir))
        f1=open(child,"r+")
        data=f1.readlines()
        f1.close()
        for line in data:  
            line_decode=line
            b.write(line_decode)
#所有标签写入一个文件
def eachFile3(filepath,writepath):
    f=open(writepath,"wb")
    pathDir =  os.listdir(filepath)
    num=1
    for allDir in pathDir:
        child = os.path.join('%s%s' % (filepath, allDir))
        f1=open(child,"r+")
        g=len(f1.readlines())
        f1.close()
        print(g)
        for i in range(g):
           f.write(str(num)+"\n")
        num+=1
        print child
#st="1"
#f2=open("/home/zzl/濡楀矂娼�/dataset2/"+st,"wb") 
def solvetext(datapath,writepath,num):
    for a in range(1,num):
        st=str(a)
        filepath=datapath+st+'/'
        Writepath=writepath+st
        eachFile(filepath,Writepath)
    
    eachFile2(writepath,"/home/zzl/桌面/data")
    eachFile3(writepath,"/home/zzl/桌面/label")

#solvetext("/home/zzl/桌面/EMdata/", "/home/zzl/桌面/dataset3/",8)
