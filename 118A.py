a = input()
a = a.lower()
b = []
for i in range(len(a)):
	if a[i]== 'a' or a[i]=='e' or a[i]=='o' or a[i] == 'u':
		True
	else:
		b.append('.'+a[i])
print(''.join(b))