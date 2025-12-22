from data import students

def save_report():
    if not students:
        return False,"No data to Save"
    
    with open("report.txt","w") as file:
        for name,marks in students.items():
            file.write(f"Name:{name}\nMarks:{marks}")
            total=sum(students[name])
            file.write(f"Average marks:{total/len(students[name])}")
    
    return True,"saved top report.txt"
            