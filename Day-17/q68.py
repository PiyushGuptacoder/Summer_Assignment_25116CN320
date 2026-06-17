arr1=list(map(int, input("enter The  elements of array1: ").split()))
arr2=list(map(int, input("enter The  elements of array2: ").split()))
result=list(set(arr1) & set(arr2))
print("The common elements of both arrays are ", result)