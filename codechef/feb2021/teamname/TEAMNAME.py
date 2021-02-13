T = int(input())
for tc in range(T):
    
    n = int(input())
    s = list(map(str, input().split(' ')))
    result = set()

    for firstname in s :
        for lastname in s :
            if firstname == lastname :
                continue
            else :
                if firstname[0] != lastname[0] and firstname[1:] != lastname[1:] :
                    result.add((firstname, lastname))
    
    print(len(result))