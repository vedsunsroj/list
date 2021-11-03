p=[1,2,3,4,5,6,7,8,9]
i=0
sum=0
while i<len(p):
	if p[i]%2==0:
		sum=sum+p[i]
	i=i+1
print(sum)