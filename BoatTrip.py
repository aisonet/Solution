#!/bin/python

import sys


n,c,m = raw_input().strip().split(' ')
n,c,m = [int(n),int(c),int(m)]
p = map(int, raw_input().strip().split(' '))

maxTransport= c*m
maxMan=max(p)
#print maxMan

#print n, c , m , p
ans=bool
if maxMan<=maxTransport:
    ans=True
else:
    ans=False

# for items in p:
#     if items<=maxTransport:
#         ans=True
#     else:
#         ans=False
#         break

if ans:
    print "Yes"
else:print "No"



