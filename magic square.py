e = [
    [8, 3, 4],
    [1, 5, 9],
    [6, 7, 2]
]
i=0
r1,r2,r3,c1,c2,c3,d1,d2=0,0,0,0,0,0,0,0
while i<len(e):
	r1=r1+e[0][i]
	r2=r2+e[1][i]
	r3=r3+e[2][i]
	c1=c1+e[i][0]
	c2=c2+e[i][1]
	c3=c3+e[i][2]
	d1=d1+e[i][i]
	d2=d2+e[i][2-i]
	i+=1
if r1==r2==r3==c1==c2==c3==d1==d2:
	print("magic square")
else:
	print("not")
