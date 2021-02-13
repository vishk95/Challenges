def check(big, small):
    big[:] = (value for value in big if value != 0)
    if big == small :
        return True
    else :
        return False

T = int(input())
for tc in range(T):
    
    n = int(input())
    w = list(map(int, input().split(' ')))
    l = list(map(int, input().split(' ')))
    hits = 0

    wsort = w.copy()
    
    wsort.sort()
    wres = w.copy()
    wres.extend([0]*50)

    smallerfrogpos = w.index(min(w))

    for i in range (1,n) :
        ifrogw = wsort[i]
        ifrogpos = w.index(ifrogw)
        ihop = l[ifrogpos]
        jpos = ifrogpos
        
        while jpos <= smallerfrogpos :
            hits += 1
            jpos += ihop

        temp = wres[ifrogpos]
        wres[ifrogpos] = wres[jpos]
        wres[jpos] = temp
        
        smallerfrogpos = jpos

        if check(wres.copy(), wsort) :
            break
    print(hits)