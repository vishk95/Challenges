N = int(input())

i = 10
while (i > 0) :
    if (N%i == 0) :
        break
    else :
        i -= 1
        
print(i)