
roll_num =[]
names=[]
courses=[]

def add_student():
    roll=int(input("Enter roll number; "))
    if roll in roll_num:
        print("Student already exists")
    else:
        name=str(input("Enter student name: "))
        course=str(input("Enter student course: "))
        roll_num.append(roll)
        names.append("name")
        courses.append("course")
        print("Student added successfully")
def del_student():
    roll=int(input("Enter roll number: "))
    if roll not in roll_num:
        print("Student not found")
    else:
        i=roll_num.index(roll)
        del roll_num[i]
        del names[i]
        del courses[i]
        print("Student deleted successfully ")
def show_student():
    if not roll_num:
        print("No students found")
    else:
        for i in range(len(roll_num)):
            print(f"Roll Number: {roll_num[i]}, Name: {names[i]}, Course: {courses[i]}")
while True:
    print("1. Add Student")
    print("2. Delete Student")
    print("3. Show Students")
    print("4. Exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        add_student()
    elif choice==2:
        del_student()
    elif choice==3:
        show_student()
    elif choice==4:
        exit()

    else:
        print("Invalid choice")