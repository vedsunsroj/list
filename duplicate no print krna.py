t = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
i=0
b=[]
while i<len(t):
    if t[i]not in b:
        b.append(t[i])
        j=0
        c=0
        while j<len(t):
            if t[i]==t[j]:
            	c=c+1
            j=j+1
        print(t[i],":",c)
    i=i+1