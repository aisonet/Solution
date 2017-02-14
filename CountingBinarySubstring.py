
import sys
import os

# Complete the function below.

def  counting(s):
    allLetter=list(s)
    count=0
    str=''
    n=0
    maxi=len(allLetter)
    #print maxi

    for n in range(0,maxi):
        print n
        print allLetter[n], allLetter[n+1]

        if allLetter[n]!=allLetter[n+1]:

            count=+1

    print 'CNT: ',count


    return allLetter




try:
    _s = raw_input()
except:
    _s = None

res = counting(_s)
print res
