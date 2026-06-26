def remove_duplicate(str):
    str2=""
    for i in str:
        i
        if i not in str2:
            str2=str2+i
    return str2
        

str=input("Enter a string: ")
print(remove_duplicate(str))
