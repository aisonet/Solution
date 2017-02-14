def makeDict(a,b, foo, li, un):
    arrayDic={}
    for items in foo:
        #initialval=0
        if items in arrayDic:
            arrayDic[items]=arrayDic[items]+1
        else:
            arrayDic.update({items:1})


    print arrayDic
    res=0
    for items in li:
        if items in arrayDic:
            cnt= arrayDic[items]
            #print cnt
            res+=cnt
    #print res

    ures = 0
    for ite in un:
        if ite in arrayDic:
            cnt = arrayDic[ite]
            # print cnt
            ures += cnt
    #print ures
    print res-ures

a,b= map(int, raw_input().strip().split(' '))
n = map(int, raw_input().strip().split(' '))
A = map(int, raw_input().strip().split(' '))
B = map(int, raw_input().strip().split(' '))

if ((1 <= a <= pow(10, 5)) & (1 <= b <= pow(10, 5)) & 1 <= max(n), max(A), max(B) <= pow(10, 9)):
    makeDict(a,b,n,A,B)
else:pass

