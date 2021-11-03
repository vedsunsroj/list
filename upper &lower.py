str =input("Enter a string: ")
upper=0
lower=0
for i in str:
    if (i.islower()):
        lower=lower+1
    elif (i.isupper()):
        upper=upper+1

print("The lower case letters:",lower)
print("The upper case letters:",upper)

