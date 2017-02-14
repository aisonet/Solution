def number_needed(al, bl):

    alSet=set(al)
    blSet=set(bl)
    diff= alSet^blSet

    for items in sorted(diff):
        print items




a = raw_input().strip()
al = map(int, raw_input().strip().split(' '))
b = raw_input().strip()
bl = map(int, raw_input().strip().split(' '))
number_needed(al, bl)
