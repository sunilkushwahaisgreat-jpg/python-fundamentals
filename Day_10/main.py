import logic 
import file_io

def main_menu():
    while True:
        print("\n--- MASTER MENU ---")
        print("1. Add Marks")
        print("2. View Student Average")
        print("3. Save Report")
        print("4. Exit")

        choice=input("Select: ")

        if choice=='1':
            name =input("Enter Student name: ")
            marks=int(input(f"Enter marks for {name}: "))
            success, msg=logic.add_student(name,marks)
            if success:
                print(msg)
        elif choice=='2':
            name=input("Enter name of student to get average: ")
            print(logic.get_avg(name))
        elif choice=='3':
            msg=file_io.save_report()
            print(msg)
        elif choice=='4':
            print("Exiting")
            break
        else:
            print("Enter valid option")
