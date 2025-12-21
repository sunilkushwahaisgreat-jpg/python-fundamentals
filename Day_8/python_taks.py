#Q1
with open("sample.txt","r") as file:
    content=file.read()
    num_lines=len(content.splitlines())
    num_words=len(content.split())
    num_characters=len(content)

print(f"No of lines:{num_lines}\nNo of words:{num_words}\nNo of characters:{num_characters}")

#Q2
students = {
    "Amit": 85,
    "Rohit": 92,
    "Sunil": 88
}
max_marks=0
summ=0
for key,value in students.items():
    if max_marks< value:
        topper=key
        max_marks=value
    summ+=value

print("Topper of class is:",topper)
print("Average marks:",summ/len(students))

#Q3
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    
    def apply_bonus(self,percent):
        bonus=(percent/100)*self.salary
        self.salary+=bonus
        print(f"Bonus given: {percent}\nNew salary: {self.salary}")
    
    def save_to_file(self):
        with open("employee.txt","w") as file:
            file.write(f"Name:{self.name}\nSalary:{self.salary}")


#Q4
while True:
    print("Calculator Menu\n")
    print("1.Add Numbers\n")
    print("2.Subtract numbers\n")
    print("3.Multiply numbers\n")
    print("Exit\n")
    op=int(input("Enter option for 1-4: "))
    if op==4:
        print("Exit")
        break

    if op in (1,2,3):
        try:
            num1=int(input("Enter first number:"))
            num2=int(input("Enter second number:"))
            if op==1:
                print(f"Result: {num1}+{num2}={num1+num2}")
            elif op==2:
                print(f"Result: {num1}-{num2}={num1-num2}")
            else:
                print(f"Result: {num1}*{num2}={num1*num2}")
        except ValueError:
            print("Error: Please enter valid numbers")
    else:
        print("Invalid choice! please select 1 2 3 or 4.")

