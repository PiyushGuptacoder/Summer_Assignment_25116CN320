def calculator(op):
    num1=int(input("Enter first number: "))
    num2=int(input("Enter second number: "))
    if op==1:
        result=num1+num2
    elif op==2:
        result=num1-num2
    elif op==3:
        result=num1*num2
    elif op==4:
        if num2==0:
            print("division by zero not possible")
        else:
            result=num1/num2
    elif op==5:
        result=num1%num2
    else:
        # print("Invalid operation")
        result="Invalid operation"
    print("Result: ",result)
while True:
    print("Welcome to the Calculator!")
    print("1. Addition")
    print("2. Subtraction") 
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exit")
    op=int(input("Enter your choice: "))
    if op==6:
        print("Thank you for using the Calculator!")
        exit()
    calculator(op)
