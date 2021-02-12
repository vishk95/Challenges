def absolute(time):
    hr = int(time[0:2])%12
    min = int(time[3:5])/60
    ap = time[6:8]
    if ap == "PM" :
        hr += 12
    return hr+min

T = int(input())
for tc in range(T):
    
    cheftime = absolute(input())
    n = int(input())
    for i in range(n):
        frndtime = input()
        strt = absolute(frndtime[0:8])
        endt = absolute(frndtime[9:17])
        if strt <= cheftime <= endt : 
            print ("1",end="")
        else :
            print ("0",end="")
    print("")
    

