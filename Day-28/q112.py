import csv
contact={}
def load_from_csv():
    try:
        with open("contact.csv","r") as f:
            read=csv.DictReader(f)
            for  row in read:
                contact[row["number"]]=row
    except FileNotFoundError:
        pass

def save_to_csv():
    with open("contact.csv", "w", newline="") as f:
        fieldnames = ["number", "name"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for cont in contact.values():
            writer.writerow(cont)

def add_contact():
    print("Enter contact details: ")
    number=int(input("Enter contact number: "))
    name=input("Enter contact name: ")
    contact[number]={"number": number, "name": name}
    save_to_csv()
    print("Contact added successfully")
def display_contact():
    if not contact:
        print("No contacts found")
    else:
        for cont in contact.values():
            print(cont)
def update_contact(number,name):
    if number not in contact:
        print("Contact not found")
    else:
        contact[number]["name"]=name
        save_to_csv()
        print("Contact updated successfully")

def delete_contact(number):
    if number not in contact:
        print("Contact not found")
    else:
        del contact[number]
        save_to_csv()
        print("contact deleted sucessfully")
while True:
    load_from_csv()
    print("1. Add contact")
    print("2. Update contact")
    print("3. Display contact")
    print("4. Delete contact")
    print("5. Exit")
    ch=int(input("Enter your choice: "))
    if ch==1:
        add_contact()
    elif ch==2:
        number=int(input("Enter contact number to update: "))
        name=input("Enter new contact name: ")
        update_contact(number,name)
    elif ch==3:
        display_contact()
    elif ch==4:
        number=int(input("Enter contact number to delete: "))
        delete_contact(number)
    elif ch==5 :
        exit()
    else:
        print("Invalid choice")
