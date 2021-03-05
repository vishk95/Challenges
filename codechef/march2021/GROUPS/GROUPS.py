T = int(input())
for tc in range(T):
	a = input()
	flag = "0"
	ans = 0
	
	for i in a:
	    if i == "1" and flag == "0" :
	        ans = ans+1
	    flag = i
	print(ans)