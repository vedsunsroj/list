s = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
c=[]
b=[]
sum=0
sum1=0
a=0
while i<len(s):
		if s[i]%2==0:
			c.append(s[i])
			sum=sum+s[i]
		else:
			 b.append(s[i])
			 sum1=sum1+s[i]
		i=i+1
print('sum of even',sum)
print('sum of odd',sum1)
print("total list sum",sum+sum1)
print('average of even',sum/len(c))
print("average of odd",sum1/len(b))
print("average of all list",(sum+sum1)/len(s))
print(len(s))
print("even number length",len(c))
print("odd number length",len(b))



a=[20,18,17,5,7,8,9,99,66,6]
i=0
sum=0
avg=0
count=0
while i<len(a):
	sum=sum+a[i]
	avg=sum/len(a)
	count=count+len(a)
	i=i+1
print(sum)
print(avg)
print(count)


