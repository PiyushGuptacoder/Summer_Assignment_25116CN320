def sort_alpha(str):
    str1=""
    for i in (sorted(str)):
        str1+=i
    return str1
str=input("Enter string:")
print(sort_alpha(str))