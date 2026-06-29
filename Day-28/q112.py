contact={}
def save_to_csv(){
    with open("contact.csv", "w", newline="") as f:
        fieldnames = ["number", "name"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for cont in contact.values():
            writer.writerow(cont)
}
def add_contact():
    print("Enter contact details: ")
    number=int(input("Enter contact number: "))
    name=input("Enter contact name: ")
    contact[number]={"number": number, "name": name}
    save_to_csv()
    print("Contact added successfully")
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
     