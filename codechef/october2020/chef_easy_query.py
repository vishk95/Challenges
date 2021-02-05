def chef_free(queries, q):
    if queries[0]>=q:
            tasks_left = queries[0] - q
    else:
        tasks_left = 0
    i = 1

    while (tasks_left>0):
        if i < len(queries):
            if queries[i]+tasks_left >= q:
                tasks_left = queries[i] + tasks_left - q
            else:
                tasks_left = 0
        
            i += 1
        else:
            i = (tasks_left//q)+1
            tasks_left = 0
    
    return(i+1)

if __name__ == '__main__':
    T = int(input())
    res = []
    for _ in range(T):
        n, k = map(int, input().split())
        queries_per_days = list(map(int, input().split()))
        res.append(chef_free(queries_per_days, k))

    for o in res:
        print(o)
    

        
        


        
