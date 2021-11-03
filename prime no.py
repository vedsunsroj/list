num=int(input("enter a number"))
i=1
sum=0
while i<=num:
    if num%i==0:
        sum+=1
    i+=1
if sum==2:
    print("prime",num)
else:
    print("not prime",num)



num= 1
while num<=100:
    count= 0
    i= 2
    while (i<=num//2):
        if num%i==0:
            count= count+1
        i= i+1
    if (count==0 and num!=1):
        print(num)
    num= num+1


n=[3,2,6,56,23,29,65,45,67]
i=0
b=[]
while i<len(n):
	j=1
	c=0
	while j<=(n[i]):
		if n[i]%j==0:
			c+=1
		j+=1
	if c==2:
		b.append(n[i])
	i+=1
print(b)

