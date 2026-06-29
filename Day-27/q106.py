import csv
employee={}
def load_from_csv():
    try:
        with open ("employee.csv","r")  as f:
            read=csv.DictReader(f)
            for  row in read:
                employee[row["empid"]]=row
    except FileNotFoundError:
        print("File not found")
def save_to_csv():
    with open ("employee.csv","w",newline="") as f:
        write=csv.DictWriter(f, fieldnames=["name", "empid", "dep", "salary", "doj"])
        write.writeheader()
        for emp in employee.values():
            write.writerow(emp)

def add_emp(name,empid,dep,salary,doj):
    if empid in employee:
        print("Employee already exists")
    else:
        employee[empid]={"name": name, "empid": empid, "dep": dep, "salary": salary, "doj": doj}
        save_to_csv()
        print("Employee added successfully")
def del_emp(empid):
    load_from_csv()
    if empid not in employee:
        print("Employee not found")
    else:
        del employee[empid]
        save_to_csv()
        print("Employee removed successfully")
def display_emp():
    if not employee:
        print("Employee not found")
    else:
        for emp in employee.values():
            print(emp)
def update_emp(empid,name,dep,salary,doj):
    if empid not in employee:
        print("Employee not found")
    else:
        employee[empid]["name"]=name
        employee[empid]["dep"]=dep
        employee[empid]["salary"]=salary
        employee[empid]["doj"]=doj
        save_to_csv()
        print("Employee details updated successfully")
def main():
    load_from_csv()
    while True:
        load_from_csv()
        print("1. Add Employee")
        print("2. Remove Employee")
        print("3. Display Employee")
        print("4. Update Employee")
        print("5. Exit")
        choice=int(input("Enter your choice: "))
        if choice==1:
            name=input("Enter name: ")
            empid=int(input("Enter empid: "))
            dep=input("Enter department: ")
            salary=int(input("Enter salary: "))
            doj=input("Enter date of joining: ")
            add_emp(name,empid,dep,salary,doj)
        elif choice==2:
            empid=int(input("Enter empid: "))
            del_emp(empid)
        elif choice==3:
            display_emp()
        elif choice==4:
            empid=int(input("Enter empid: "))
            name=input("Enter name: ")
            dep=input("Enter department: ")
            salary=int(input("Enter salary: "))
            doj=input("Enter date of joining: ")
            update_emp(empid,name,dep,salary,doj)
        elif choice==5:
            exit()
        else:
            print("Invalid choice")
if __name__ == "__main__":
    main()