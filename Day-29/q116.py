import csv
product={}
def load_from_csv():
    try:
        with open ("product.csv","r") as f:
            read=csv.DictReader(f)
            for row in read:
                product[row["pro_id"]]=row
    except FileNotFoundError:
        print("File not found")
def save_to_csv():
    with open ("product.csv","w",newline="") as f:
        write=csv.DictWriter(f, fieldnames=["pro_id","name","price","qty","dateofpurchase"])
        write.writeheader()
        for pro in product.values():
            write.writerow(pro)
def add_item():
    pro_id=input("Enter product id: ")
    if pro_id in product:
        print ("Product already exists")
    else:
        name=input("Enter product name: ")
        price=float(input("Enter product price"))
        qty=int (input("Enter products quantity"))
        dateofpurchase=input("Enter date of purchase: ")
        product[pro_id]={"pro_id": pro_id,"name": name, "price": price, "qty": qty, "dateofpurchase":dateofpurchase}
        save_to_csv()
        print("product added sucessfully")
def del_item(pro_id):
    if product not in product:
        print("Product not found")
    else:
        del product[pro_id]
        save_to_csv()
        print("Product removed successfully")
def diplay_item():
    if not product:
        print("Product not found")
    else:
        for  pro in product.values():
            print(pro)
def update_item():
    pro_id=input("Enter product id to update: ")
    if pro_id not in product:
        print("Product not found")
    else:
        name=input("Enter new product name: ")
        price=float(input("Enter new product price"))
        qty=int (input("Enter new products quantity"))
        dateofpurchase=input("Enter new date of purchase: ")
        product[pro_id]={"pro_id": pro_id,"name": name, "price": price, "qty": qty, "dateofpurchase":dateofpurchase}
        save_to_csv()
        print("Product updated successfully")
def search_item(pro_id):
    if pro_id in product:
        print(product[pro_id])
    else:
        print("Product not found")
while True:
    load_from_csv()
    print("1. Add product")
    print("2. Update product")
    print("3. Display product")
    print("4. Delete product")
    print("5. Search product")
    print("6. Exit")
    ch=int(input("Enter your choice: "))
    if ch==1:
        add_item()
    elif ch==2:
        update_item()
    elif ch==3:
        diplay_item()
    elif ch==4:
        pro_id=input("Enter product id to delete: ")
        del_item(pro_id)
    elif ch==5:
        pro_id=input("Enter product id to search: ")
        search_item(pro_id)
    elif ch==6 :
        break
            