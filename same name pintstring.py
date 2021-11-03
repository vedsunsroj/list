a="sunita"
b="weather"
list=[]
i=0
while i<len(a):
    if a[i] in b:
        list.append(a[i])
    i=i+1
print(list)