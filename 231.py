a=int(input())
flag = 0
for i in range(a):
	my_list = list(map(int,input().split()))
	if my_list.count(1)>=2:
		flag+=1
print(flag)
