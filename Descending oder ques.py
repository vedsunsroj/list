a=[8,9,56,67,87,45,33,23,46,98]
i=0
while i<len(a):
	j=0
	while j<len(a):
		if a[i]>a[j]:
			a[i],a[j]=a[j],a[i]
		j+=1
	i+=1
print(a)