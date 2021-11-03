binary=[0,1,0]
binary.reverse()
i=0
sum=0
while i<len(binary):
	sum=(binary[i],2*i+sum)
	i+=1
print(sum)