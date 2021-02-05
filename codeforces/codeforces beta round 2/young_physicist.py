def isEquilibrium(a, t):
    x, y, z = 0, 0, 0
    for i in range(t):
        x += a[i][0]
        y += a[i][1]
        z += a[i][2]
    if (x or y or z):
        print("NO")
    else:
        print("YES")

if __name__ == '__main__':
    T = int(input())
    vectors = []
    for _ in range(T):
        vectors.append(list(map(int, input().split())))
    
    isEquilibrium(vectors, T)