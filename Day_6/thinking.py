name=input("Enter name of student:")
marks={}
sub=int(input("Enter number of Subjects:"))
for i in range(sub):
    mark=int(input(f"Enter Marks of Subject{i+1}:"))
    marks[f"Subject{i+1}"]=mark

total=0
for val in marks.values():
    total+=val

print(f"Name: {name}\nAverage: {total/len(marks)}")