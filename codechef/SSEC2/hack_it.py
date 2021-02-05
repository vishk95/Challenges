def correction(i):
    res = ""
    for digit in range(len(i)):
        i[digit] = str(int(i[digit]) - 2)
    
    print(int(res.join(i)))
    
if __name__ == '__main__':
    n = int(input().strip())
    passwords = []
    for _ in range(n):
        passwords.append(list(input().strip()))
    
    for i in passwords:
        correction(i)
