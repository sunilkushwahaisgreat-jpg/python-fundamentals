class Student:
    def __init__(self,name,college):
        self.name=name
        self.college=college
    
    def display_info(self):
        print(f"Name: {self.name}\nCollege: {self.college}")

student1=Student("Sunil","NIT Silchar")

student1.display_info()