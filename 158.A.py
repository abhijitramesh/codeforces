p,q=(map(int,input().split(' ')))
c = 0
my_list = list(map(int,input().split(' ')))
for i in range(len(my_list)):
	if(my_list[i]>=my_list[q]) and my_list[i]>0:
		c+=1
print(c)