def is_rotation(str1,str2):
    n1=len(str1)
    n2=len(str2)
    if n1!=n2:
        print("The strings are not rotations of each other")
        return 0
    str3=str1+str1
    if str2 in str3:
        print("The strings are rotations of each other")
        return 1
    else:
        print("The strings are not rotations of each other")
        return 0
str1=input("Enter the first string: ")
str2=input("Enter the second string: ")
is_rotation(str1,str2)