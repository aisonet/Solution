import sys
sys.setrecursionlimit(1000000)

n = int(input())
tree= raw_input()
#print n, tree



# print n ,'\n','BT=', BT

def findMax(n, tree):
    BT = tree.split()


    #deserialize tree into node = [child1 index, child2 index, node value]

    x = len(BT)
    #print 'x=',x
    blankcount = 0
    for i in range(x):
        if BT[i] == '#':
            blankcount += 2
            continue
        a = int(BT[i])
        #print 'a',a , "blankcount",blankcount
        BT[i] = [i*2+1 - blankcount, i*2+2 - blankcount, a]
    #print(BT)

    #memoize
    memo = [[None, None] for node in range(x)]
    #print memo

    def state(node, selected):
        if node >= x:
            return 0
        if BT[node] == '#':
            return 0
        #check memo here
        if memo[node][selected] is not None:
            return memo[node][selected]
        left_child = BT[node][0]
        right_child = BT[node][1]
        if selected:
            memo[node][selected] = state(left_child, 0) + state(right_child, 0) + BT[node][2]
            return memo[node][selected]
        else:
            memo[node][selected] = max(state(left_child, 0), state(left_child, 1)) + max(state(right_child, 0), state(right_child, 1))
            return memo[node][selected]

    return(max(state(0, 0), state(0, 1)))

result=findMax(n, tree)
print result