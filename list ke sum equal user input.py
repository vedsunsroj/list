number=int(input("enter s number"))
n=[10,11,12,13,14,15,16,17,18,19]
sum=0
i=0
while i<len(n):
	sum=sum+n[i]
	print(sum)
	i+=1
if number==sum:
	print("equl")
else:
	print("nhi")