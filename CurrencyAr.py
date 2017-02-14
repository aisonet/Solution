

def  arbitrage(quotes):
    finaList=[]
    for items in quotes:

        #print items
        primary=100000
        for num in items.split(' '):

            #print num
            primary=primary/float(num)

            # finalResult=primary/float(num)
            # finalResult/float(num)
        #print primary


        if  primary > 100000:
            result= int(primary)-100000
            finaList.append(result)
        else:
            finaList.append('0')

    return finaList







a= ['1.1837 1.3829 0.6102', '1.1234 1.2134 1.2311']
listA= arbitrage(a)
