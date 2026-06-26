def votting_system(age):
    if age >=18:
        print("You are eligible to vote.")
    else:
        print("You are under age and not eligible to vote.")
    
age=int(input("Enter your age: "))
votting_system(age)