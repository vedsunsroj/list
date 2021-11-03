b=[2,4,5,7,7,8,88,99,0,55,44,4,4,3,6,555,66,66,8]
a=[]
for i in b:
	if i not in a:
		a.append(i)
		c=a
		for i in range(len(c)):
			for j in range (i+1, len(c)):
				if c[i]>c[j]:
					c[i],c[j]=c[j],c[i]
print(c)

b=[2,4,5,2,7,7,8,88,99,0,55,44,4,4,3,6,555,66,66,8]
a=[]
for i in b:
	if i not in a:
		a.append(i)
print(a)