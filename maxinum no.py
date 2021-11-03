number=[2,42,14,10]
i=0
m=0
while i<len(number):
	if number[i]>m:
		m=number[i]
	i=i+1
print(m)


n=[2,4,6,7,34,45,103,304,87,56]
i=0
m=0
while i<len(n):
	if n[i]>m:
		m=n[i]
	i+=1
print(m)
j=0
sm=0
while j<len(n):
	if n[j]!=m:
		if n[j]>sm:
			sm=n[j]
	j+=1
print(sm)
c=0
tm=0
while c<len(n):
	if n[c]!=m and n[c]!=sm:
		if n[c]>tm:
			tm=n[c]
	c+=1
print(tm)



n= [50, 40, 23, 70, 56, 12, 5, 10, 7]
i=0
m=0
while i<len(n):
    if n[i]>m:
        m=n[i]
    i+=1
print(m)