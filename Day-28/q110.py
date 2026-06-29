import csv

filename = "bank.csv"
details = {}

def load_from_csv():
    try:
        with open(filename, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                details[row["custid"]] = row
    except FileNotFoundError:
        pass
def save_to_csv():
    with open(filename, "w", newline="") as f:
        fieldnames = ["custid", "name", "address","balance","acctype","openingdate"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for det in details.values():
            writer.writerow(det)

def open_acc():
    custid = input("Enter customer ID: ")
    if custid in details:
        print("Customer ID already exists.")
        return

    name = input("Enter Name: ")
    address = input("Enter Address: ")
    balance = float(input("Enter initial balance: "))
    acctype = input("Enter account type: ")
    openingdate = input("Enter opening date: ")

    details[custid] = {
        "custid": custid,
        "name": name,
        "address": address,
        "balance": balance,
        "acctype": acctype,
        "openingdate": openingdate
    }
    save_to_csv()
    print("Customer record added successfully.")
        
    

def display_details():
    if not details:
        print("No records found.")
    else:
        for det in details.values():
            print(det)

def search_customer():
    custid = input("Enter customer ID to search: ")
    if custid in details:
        print(details[custid])
    else:
        print("Record not found.")
        
    
def update_details():
    custid = input("Enter customer ID to update: ")
    if custid in details:
        name = input("Enter new Name: ")
        address = input("Enter new Address: ")
        balance = float(input("Enter new balance: "))
        acctype = input("Enter new account type: ")
        details[custid] = {
            "custid": custid,
            "name": name,
            "address": address,
            "balance": balance,
            "acctype": acctype,
            "openingdate": details[custid]["openingdate"]
        }
        save_to_csv()
        print("Customer record updated.")
    else:
        print("Record not found.")

def delete_customer_record():
    custid = input("Enter Customer ID to delete: ")
    if custid in details:
        del details[custid]
        save_to_csv()
        print("Customer record deleted.")
    else:
        print("Record not found.")

def main():
    load_from_csv()
    while True:
        print("\n--- Bank Management System ---")
        print("1. Add Customer Record")
        print("2. Display Customer Records")
        print("3. Update Customer Record")
        print("4. Delete Customer Record")
        print("5. Search Customer")
        print("6. Exit")

        choice = input("Enter choice: ")
        if choice == "1":
            open_acc()
        elif choice == "2":
            display_details()
        elif choice == "3":
            update_details()
        elif choice == "4":
            delete_customer_record()
        elif choice == "5":
            search_customer()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
