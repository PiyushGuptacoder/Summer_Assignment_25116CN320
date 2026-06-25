def sort_char(str):
    str1=[]
    for word in str.split():
        j =len(word)
        str1.append((j,word))
    for k in sorted(str1).index:
        str2+=k
    return str2
str=input("Enter string:")
print(sort_char(str))