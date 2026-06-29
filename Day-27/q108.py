import csv

filename = "marksheet.csv"
marksheets = {}

def load_from_csv():
    try:
        with open(filename, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                marksheets[row["roll"]] = row
    except FileNotFoundError:
        pass

def save_to_csv():
    with open(filename, "w", newline="") as f:
        fieldnames = ["roll", "name", "admission_no", "Maths", "physics","chemistry","pps","ss", "total", "percentage"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for marks in marksheets.values():
            writer.writerow(marks)

def add_marksheets():
    roll = input("Enter Roll Number: ")
    if roll in marksheets:
        print("Marksheet already exists!")
        return
    name = input("Enter Name: ")
    admission_no = input("Enter Admission Number: ")
    maths = float(input("Enter Maths Marks: "))
    physics = float(input("Enter Physics Marks: "))
    chemistry = float(input("Enter Chemistry Marks: "))
    pps = float(input("Enter PPS Marks: "))
    ss = float(input("Enter SS Marks: "))
    total = maths + physics + chemistry + pps + ss
    percentage = (total / 500) * 100
    marksheets[roll] = {
        "roll": roll, "name": name, "admission_no": admission_no,
        "Maths": maths, "physics": physics, "chemistry": chemistry,
        "pps": pps, "ss": ss, "total": total, "percentage": percentage
    }
    save_to_csv()
    print("Marksheet record added successfully.")

def display_marksheets():
    if not marksheets:
        print("No records found.")
    else:
        for marks in marksheets.values():
            print(marks)

def search_marksheets():
    roll = input("Enter Roll Number to search: ")
    if roll in marksheets:
        print(marksheets[roll])
    else:
        print("Record not found.")

def update_marksheets():
    roll = input("Enter roll no to update: ")
    if roll in marksheets:
        name = input("Enter new Name: ")
        maths = float(input("Enter new Maths Marks: "))
        physics = float(input("Enter new Physics Marks: "))
        chemistry = float(input("Enter new Chemistry Marks: "))
        pps = float(input("Enter new PPS Marks: "))
        ss = float(input("Enter new SS Marks: "))
        total = maths + physics + chemistry + pps + ss
        percentage = (total / 500) * 100
        marksheets[roll] = {
            "roll": roll, "name": name, "admission_no": marksheets[roll]["admission_no"],
            "Maths": maths, "physics": physics, "chemistry": chemistry,
            "pps": pps, "ss": ss, "total": total, "percentage": percentage
        }
        save_to_csv()
        print(" Marksheet record updated.")
    else:
        print("Record not found.")

def delete_marksheets():
    roll = input("Enter ROll no to delete: ")
    if roll in marksheets:
        del marksheets[roll]
        save_to_csv()
        print("Marksheet record deleted.")
    else:
        print("Record not found.")

# def delete_salary():
#     empid = input("Enter Employee ID to delete: ")
#     if empid in salaries:
#         del salaries[empid]
#         save_to_csv()
#         print("✅ Salary record deleted.")
#     else:
#         print("❌ Record not found.")

def main():
    load_from_csv()
    while True:
        print("\n--- marksheets Management System ---")
        print("1. Add Marksheet Record")
        print("2. Display Marksheet Records")
        print("3. Search Marksheet Record")
        print("4. Update Marksheet Record")
        print("5. Delete Marksheet Record")
        print("6. Exit")

        choice = input("Enter choice: ")
        if choice == "1":
            add_marksheets()
        elif choice == "2":
            display_marksheets()
        elif choice == "3":
            search_marksheets()
        elif choice == "4":
            update_marksheets()
        elif choice == "5":
            delete_marksheets()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
