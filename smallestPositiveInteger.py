def solution(A):
    allPos=frozenset((value for value in A if 0 < value < 1000000))
    if allPos:
        minVal = min(allPos)
        start = 0 if minVal < len(A) else minVal
        if minVal + len(A) + 1 < 1000000:
            return next((start + i for i in xrange(1, len(A) + 2) if not start + i in allPos), 1)
    return 1

A = [ 1, 3, 6, 4, 1, 2,-1, -3]
print solution(A)

