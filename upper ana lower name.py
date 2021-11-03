list=["somi","SUNITA","BUDANIA","chaudhary"]
i=0
a=[]
b=[]
# while i<len(list):
#     if list[i].upper():
#         a.append(list[i])
#     else:
#         b.append(list[i])
#     i+=1
# print(a)
# print(b)
while i<len(list):
    if list[i].isupper():
        a.append(list[i])
    else:
        b.append(list[i])
    i=i+1
print("upper",a)
print("lower",b)
