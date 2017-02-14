def number_needed(a, b):
    aSet=list(a)
    bSet=list(b)
    virA= aSet
    virB= bSet

    diffList=[]
    diffList1 = []
    diffListComm=[]

    for elemnts in aSet:
        if elemnts in virB:
            diffListComm.append(elemnts)
            virB.remove(elemnts)
        else:
            diffList.append(elemnts)
    for items in diffListComm:
        virB.append(items)
    for elem in bSet:
        if elem in virA:
            virA.remove(elem)
        else:
            diffList1.append(elem)
    return len(diffList1)+len(diffList)

a = raw_input().strip()
b = raw_input().strip()

print number_needed(a, b)
