T = int(input())
for tc in range(T):
    n = int(input())
    a = list(map(int, input().split(' ')))
    
    
    ans = 2 * (max(a) - min(a))
    print(ans)