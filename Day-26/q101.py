import random as r
def random_no(r):
    number1=int(input("enter a number between 1 to 100: "))
    number2=r.randint(1,100)
    # number=print(random_no(r))
    if number1==number2:
        print("you win")
    else:
        print("you lose")
        print("the number was",number2)
        print("try again")
    random_no(r)

random_no(r)