import csv
employee = {}
class student_details:
    def __init__(self,name,rollno,section,year,branch,admission_date):
        self.name=name
        self.rollno=rollno
        self.section=section
        self.year=year
        self.branch=branch
        self.admission_date=admission_date
    def __str__(self):
        return f"Roll: {self.rollno}, Name: {self.name}, Section: {self.section}, Year: {self.year}, Branch: {self.branch}, Admission Date: {self.admission_date}"

    def display(self):
        print("Name:",self.name)
        print("Roll No:",self.rollno)
        print("Section:",self.section)
        print("Year:",self.year)
        print("Branch:",self.branch)
        print("Admission Date:",self.admission_date)

class studentmanagement:
    def __init__(self,filename="studentmanagement.csv"):
        self.students={}
        self.filename=filename
        self.load_from_csv()


    def add_student(self,roll,name,section,year,branch,dateofadm):
        if roll in self.students:
            print("student already exixts")
        else:
            self.students[roll] =student_details(name,roll,section,year,branch,dateofadm)
            self.save_to_csv()
            print("Student added successfully")

    def remove_student(self,roll):
        if roll not in self.students:
            print("student not found")
        else:
            del self.students[roll]
            self.save_to_csv()
            print("Student removes seccessfully")
    def display_stu(self):
        if not self.students:
            print("Student not found")
        else:
            for student in self.students.values():
                print(student)

    def update_stu(self,roll,name,section,year,branch,dateofadm):
        if roll not in self.students:
            print("Student not found")
        else:
            self.students[roll].name=name
            self.students[roll].section=section
            self.students[roll].year=year
            self.students[roll].branch=branch
            self.students[roll].admission_date=dateofadm
            self.save_to_csv()
            print("Student details updated successfully")
            
    def search_stu(self,roll):
        if roll not in self.students:
            print("Student not found")
        else:

            print(self.students[roll])
            # print(self.load_from_csv())

    def save_to_csv(self):
        with open(self.filename,"w") as f:
            write=csv.writer(f)
            write.writerow(["Name", "Roll No", "Section", "Year", "Branch", "Admission Date"])
            for student in self.students.values():
                write.writerow([student.name, student.rollno, student.section, student.year, student.branch, student.admission_date])
    def load_from_csv(self):
        try:
            with open(self.filename,"r") as f:
                read=csv.DictReader(f)
                for row in read:
                    name=row["Name"]
                    roll=int(row["Roll No"])
                    section=row["Section"]
                    year=int(row["Year"])
                    branch=row["Branch"]
                    dateofadm=row["Admission Date"]
                    self.students[row[roll]]=student_details(name,roll,section,year,branch,dateofadm)
        except FileNotFoundError:
            pass
def main():
    sm=studentmanagement()
    while True:
        print("1. Add Student")
        print("2. Remove Student")
        print("3. Display Students Details")
        print("4. Upddate students details")
        print("5. Search Student")
        print("6. Exit")
        choice=int (input("Enter enter menu choice: "))
        if choice==1:
            roll=int (input ("Enter roll nuumber : "))
            name=input("Enter name: ")
            section=input("Enter section: ")        
            year=int(input("Enter year: "))
            branch=input("Enter branch: ")
            dateofadm=input("Enter date of admission: ")
            sm.add_student(roll,name,section,year,branch,dateofadm)
        
        elif choice==2:
            roll=int(input("Enter roll number: "))
            sm.remove_student(roll)
        elif choice==3:
            # roll=int(input("Enter roll number: "))
            sm.display_stu()
        elif choice==4:
            roll=int(input("Enter roll number: "))
            name=input("Enter name: ")
            section=input("Enter section: ")        
            year=int(input("Enter year: "))
            branch=input("Enter branch: ")
            dateofadm=input("Enter date of admission: ")
            sm.update_stu(roll,name,section,year,branch,dateofadm)
        elif choice==5:
            roll=int(input("Enter roll number: "))
            sm.search_stu(roll)
        elif choice==6:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
    
if __name__=="__main__":
    main()
# st1=student_details("John",101,"A",2,"CSE","2022-08-15",1001)
# st2=student_details("Alice",102,"B",3,"ECE","2022-08-16",1002)
# st3=student_details("Bob",103,"A",1,"MECH","2022-08-17",1003)

# st1.display()
# st2.display()
# st3.display()

