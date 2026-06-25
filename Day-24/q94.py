def compress_string(str):
    count=1
    comp=[]
    for i in  range (0,len(str)-1):
        if str[i]==str[i+1]:
            count+=1
        else:
            comp=comp+[str[i]]+[count]
            count=1
    print("the compressed string is: ",comp)
str=input("Enter the string: ")
compress_string(str)