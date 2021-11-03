# list1=[1,2,3,[4,5],6,7,[8,9],10]
# i=1
# a=[]
# sum=0
# while i<len(list1):
#     sum=sum+list[i]
#     i+=1
#     print(sum) 


# list=[1,2,3,[4,5],6,[7,8],9,10]
# i=0
# sum=0
# while i<=list:
# 	j=0
# 	while j<len(list[i]):
# 		sum=sum+list[i][j]
# 		j+=1
# 	i+=1
# print(sum)


m=[[2,3,76,8,9],[4,5,7,8],[6,5,6]]
i=0
sum=0
while i<len(m):
	j=0
	while j<len(m):
		sum=(sum+m[i][j])
		j+=1
	print(sum)
	i+=1
