import operator
def  electionWinner(votes):
    pairDic={}
    totalPair=0
    for items in votes:
        #initialval=0
        if items in pairDic:
            pairDic[items]=pairDic[items]+1
        else:
            pairDic.update({items:1})

    #print pairDic

    a=[key for key, val in pairDic.iteritems() if val == max(pairDic.values())]
    #print a
    print sorted(a)

    for item in sorted(a):
        a=item

    return item





inp=['Alex','Michael','Harry','Dave','Michael','Victor','Harry','Alex','Mary','Mary']

res=electionWinner(inp)
print res