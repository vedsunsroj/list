def eligible_for_vote():
    age=int(input("enter a number"))
    if age<18:
        print("not eligible") 
    elif age>=18:
        print("eligible")
eligible_for_vote()


def eligible_for_vote():
    age=int(input("enter a number"))
    def vote():
        if age<18:
            print("not eligible") 
        elif age>=18:
            print("eligible")
    vote()
eligible_for_vote()




# def func(x=1,y=2):
#     x=x+y
#     y+=1
#     print(x,y)
# func(y=2,x=1)
