a = input()
b = input()
flag = 0
a = a.lower()
b = b.lower()
for i in range(len(a)):
	if a[i]<b[i]:
		print("-1")
		flag = 1
	elif a[i]>b[i]:
		print("1")
		flag = 1
if flag == 0:
	print("0")

