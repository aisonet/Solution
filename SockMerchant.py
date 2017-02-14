#!/bin/python

import sys
def NoOfpairs(c):
    pairDic={}
    totalPair=0
    for items in c:
        #initialval=0
        if items in pairDic:
            pairDic[items]=pairDic[items]+1
        else:
            pairDic.update({items:1})
    #print pairDic

    for key,val in pairDic.items():
        #print key, val
        pair=val/2
        totalPair+=pair


    print totalPair



n = int(raw_input().strip())
c = map(int,raw_input().strip().split(' '))
NoOfpairs(c)

