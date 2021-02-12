T = int(input())
for tc in range(T):
    n = int(input())
    a = list(map(int, input().split('/n')))
    
    
    ans = 2 * (max(a) - min(a))
    print(ans)