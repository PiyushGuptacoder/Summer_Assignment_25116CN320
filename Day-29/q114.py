def menu_driven_list():
    arr=[]
    while True:
        print("1. Insert element")
        print("2. Show elements")
        print("3. search element")
        print("4. sort element")
        print("5. delete element")
        print("6. exit")
        choice=int(input("Enter your choice: "))
        if choice==1:
            # element=int(input("Enter element to insert: "))
            # arr.append(element)
            arr=input("Enter elements separated by space: ").split()
        elif choice==2:
            print("Elements in the list:")
            for i in arr:
                print(i, end=" ")
            print()
        elif choice==3:
            element=int(input("Enter element to search: "))
            if element in arr:
                print("Element found at index:", arr.index(element))
            else:
                print("Element not found")
        elif choice==4:
            arr.sort()
            print("Elements sorted")
            print(arr)
        elif choice==5:
            element=int(input("Enter element to delete: "))
            if element in arr:
                arr.remove(element)
                print("Element deleted")
            else:
                print("Element not found")
        elif choice==6:
            print("Thank you for using the List!")
            exit()
        else:
            print("Invalid choice")

menu_driven_list()