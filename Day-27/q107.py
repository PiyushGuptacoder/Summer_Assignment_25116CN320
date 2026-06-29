import csv

filename = "salary.csv"
salaries = {}

def load_from_csv():
    try:
        with open(filename, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                salaries[row["empid"]] = row
    except FileNotFoundError:
        pass

def save_to_csv():
    with open(filename, "w", newline="") as f:
        fieldnames = ["empid", "name", "basic", "allowances", "deductions", "net"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for sal in salaries.values():
            writer.writerow(sal)

def add_salary():
    empid = input("Enter Employee ID: ")
    if empid in salaries:
        print("Salary record already exists!")
        return
    name = input("Enter Name: ")
    basic = float(input("Enter Basic Salary: "))
    allowances = float(input("Enter Allowances: "))
    deductions = float(input("Enter Deductions: "))
    net = basic + allowances - deductions
    salaries[empid] = {
        "empid": empid, "name": name,
        "basic": basic, "allowances": allowances,
        "deductions": deductions, "net": net
    }
    save_to_csv()
    print("Salary record added successfully.")

def display_salaries():
    if not salaries:
        print("No records found.")
    else:
        for sal in salaries.values():
            print(sal)

def search_salary():
    empid = input("Enter Employee ID to search: ")
    if empid in salaries:
        print(salaries[empid])
    else:
        print("Record not found.")

def update_salary():
    empid = input("Enter Employee ID to update: ")
    if empid in salaries:
        name = input("Enter new Name: ")
        basic = float(input("Enter new Basic Salary: "))
        allowances = float(input("Enter new Allowances: "))
        deductions = float(input("Enter new Deductions: "))
        net = basic + allowances - deductions
        salaries[empid] = {
            "empid": empid, "name": name,
            "basic": basic, "allowances": allowances,
            "deductions": deductions, "net": net
        }
        save_to_csv()
        print("Salary record updated.")
    else:
        print("Record not found.")

def delete_salary():
    empid = input("Enter Employee ID to delete: ")
    if empid in salaries:
        del salaries[empid]
        save_to_csv()
        print("Salary record deleted.")
    else:
        print("Record not found.")

def main():
    load_from_csv()
    while True:
        print("\n--- Salary Management System ---")
        print("1. Add Salary Record")
        print("2. Display Salary Records")
        print("3. Search Salary Record")
        print("4. Update Salary Record")
        print("5. Delete Salary Record")
        print("6. Exit")

        choice = input("Enter choice: ")
        if choice == "1":
            add_salary()
        elif choice == "2":
            display_salaries()
        elif choice == "3":
            search_salary()
        elif choice == "4":
            update_salary()
        elif choice == "5":
            delete_salary()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
