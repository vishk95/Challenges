(N, H, x) = map(int, input().split(' '))


T = list(map(int, input().split(' ')))

if (x+max(T) >= H):
    print("YES")
else:
    print("NO")