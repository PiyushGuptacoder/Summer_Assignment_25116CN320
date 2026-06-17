arr1=list(map(int, input("enter The  elements of array1: ").split()))
arr2=list(map(int, input("enter The  elements of array2: ").split()))
arr1.extend(arr2)
print("The merged array is ", arr1)