a=[["g","f","g"],["i","s"],["b","e","s","t"]]
i=0
while i<len(a):
	j=0
	while j<len(a[i]):
		print(a[i] [j],end=" ")
		j=j+1
	i=i+1



a=[["i","f","g"],["i","s"],["b","e","s","t"]]
i=0
while i<len(a):
	j=0
	while j<len(a[i]):
		if i==0:
			if j==2:
				print(" ",end=" ")
		print(a[i][j],end=" ")
		j+=1
	print(end=" ")
	i+=1