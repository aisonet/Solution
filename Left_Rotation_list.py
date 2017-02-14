
def array_left_rotation(a, n, k):
    li = a
    liFirst = li[:k]
    del li[:k]
    for items in liFirst:
        li.append(items)
    print li
    print ' '.join(str(x) for x in li)

n, k = map(int, raw_input().strip().split(' '))
a = map(int, raw_input().strip().split(' '))
answer = array_left_rotation(a, n, k);

