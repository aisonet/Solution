import sys
sys.setrecursionlimit(1000000)

n = int(input())
tree= raw_input()
print n, tree

BT = tree.split()

print n , BT


#deserialize tree into node = [child1 index, child2 index, node value]

x = len(BT)
blankcount = 0
for i in range(x):
    if BT[i] == '#':
        blankcount += 2
        continue
    a = int(BT[i])
    BT[i] = [i*2+1 - blankcount, i*2+2 - blankcount, a]
#print(BT)

#memoize
memo = [[None, None] for node in range(x)]

def wee(node, selected):
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
        memo[node][selected] = wee(left_child, 0) + wee(right_child, 0) + BT[node][2]
        return memo[node][selected]
    else:
        memo[node][selected] = max(wee(left_child, 0), wee(left_child, 1)) + max(wee(right_child, 0), wee(right_child, 1))
        return memo[node][selected]

print(max(wee(0, 0), wee(0, 1)))