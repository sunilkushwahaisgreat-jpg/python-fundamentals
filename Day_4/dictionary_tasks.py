#Q5 Average marks of student in a dictionary
def calculate_average(marks_dict):
    total=0
    for val in marks_dict.values():
        total+=val
    
    return total/len(marks_dict)

#Q6 Print Subject wise marks
def print_marks(marks_dict):
    for key,val in marks_dict.items():
        print(key,":",val)


marks_dict={
    "Math": 85,
    "Physics": 78,
    "Chemistry": 90
}

print("Average marks of student is:",calculate_average(marks_dict))
print_marks(marks_dict)


