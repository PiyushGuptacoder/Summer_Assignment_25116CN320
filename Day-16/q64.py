def remove_duplicates_order(arr):
    set1 = set()
    result = []
    for num in arr:
        if num not in set1:
            set1.add(num)
            result.append(num)
    return result

# Example usage
n=int(input("enter the size "))
arr=[]
for i in range(n):
    num=int(input(f"enter the element {i+1}:"))
    arr.append(num)

result = remove_duplicates_order(arr)
print("Array after removing duplicates:", result)
