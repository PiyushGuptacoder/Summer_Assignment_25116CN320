def string_operation():
    while True:
        str1=input("Enter first string: ")
        str2=input("Enter second string: ")
        print("1. Concatenate")
        print("2. Display strings")
        print("3. length of strings")
        print("4. compare with another string")
        print("5. convert to upper case")
        print("6. convert to lower case")
        print("7. Exit")
        choice=int(input("Enter your choice: "))
        if choice==1:
            result=str1+" " +str2
            print("Concatenated string:", result)
        elif choice==2:
            print("First string:", str1)
            print("Second string:", str2)
        elif choice==3:
            print("lenght of string 1: ", len(str1))
            print("lenght of string 2: ", len(str2))
        elif choice==4:
            str3=input("Enter string to compare: ")
            if str3==str1:
                print("String 1 is equal to string 3")
            elif str3==str2: 
                print("String 2 is equal to string 3")
            else:
                print("String 3 is not equal to string 1 or string 2")
        
        elif choice==5:
            print("Upper case of string 1: ", str1.upper())
            print("Upper case of string 2: ", str2.upper())
        elif choice==6:
            print("Lower case of string 1: ", str1.lower())
            print("Lower case of string 2: ", str2.lower())
        elif choice==7:
            print("Thank you for using the String Operations!")
            exit()
        else:
            print("Invalid choice")
string_operation()