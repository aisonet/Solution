def ransom_note(magazine, rasom):

    #print magazine
    #print rasom
    ans=bool
    if (1<=len(magazine)<=30000 & 1<=len(max(magazine,key=len))<=5 &
        1 <= len(rasom) <= 30000 & 1 <= len(max(rasom, key=len)) <= 5):
        for items in rasom:
            if items in magazine:
                print len(items)
                magazine.remove(items)
                ans=True

    else: ans=False

        #print ans
    return ans



m, n = map(int, raw_input().strip().split(' '))
magazine = raw_input().strip().split(' ')
ransom = raw_input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if (answer):
    print "Yes"
else:
    print "No"

