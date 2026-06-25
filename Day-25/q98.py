def common_char(str1,str2):
    str3=""
    for i in str1:
        if i in str2 and i not in str3:
            str3+=i
    return str3

str1=input("Enter first string: ")
str2=input("Enter second string: ")
print(common_char(str1,str2))