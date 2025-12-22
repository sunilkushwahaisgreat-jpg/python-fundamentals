from data import students

def add_student(name,marks):
    if name not in students:
        students[name]=[]
    students[name].append(marks)
    return True,"Student Added"

def get_avg(name):
    total=sum(students[name])
    return total/len(students[name])
