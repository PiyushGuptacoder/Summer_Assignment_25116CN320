def sort_char(str):
    str1=[]
    str2=[]
    for word in str.split():
        j =len(word)
        str1.append((j,word))
    str1.sort()
    for k,word in str1:
        str2.append(word)
    return str2
str=input("Enter string:")
print(sort_char(str))