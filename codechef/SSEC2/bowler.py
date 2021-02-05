if __name__ == '__main__':
    T = int(input())
    arr = []
    for _ in range(T):
        arr.append(list(map(int, input().split())))
    
    for i in range(T):
        if arr[i][1]*arr[i][2]<arr[i][0]:
            print("-1")
        else:
            for j in range(arr[i][0]):
                print((j%arr[i][1])+1, end=" ")
            print("")