students={}
def add_student():
    name=input("Enter student name: ")
    subjects=int(input("Enter number of subjects:"))
    students[name]=[]
    for i in range(subjects):
        marks=int(input(f"Enter subject{i+1} marks: "))
        students[name].append(marks)

def student_avg():
    name=input("Enter name of student: ")
    if not students:
        print("empty data")
        return
    if name not in students:
        print("No student found!")
        return

    total=sum(students[name])
    print(f"Average of student: {total/len(students[name])}")

def save_file():
    with open("report.txt","w") as file:
        for key, value in students.items():
            file.write(f"Name:{key}\nMarks:{value}\n")
            avg=sum(students[key])/len(students[key])
            file.write(f"Average: {avg}\n\n")
    
while True:
    print("\nSTUDENT SYSTEM")
    print("1. Add Student")
    print("2. View Average")
    print("3. Save Report")
    print("4. Exit")
        
    choice = input("Select (1-4): ")

    if choice == '1':
        add_student()
    elif choice == '2':
        student_avg()
    elif choice == '3':
        save_file()
    elif choice == '4':
        print("👋 Exiting...")
        break
    else:
        print("Invalid choice.")
