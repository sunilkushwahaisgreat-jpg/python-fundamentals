name=input("Enter the name:")
age=int(input("Enter the age:"))

with open("data.txt","w") as file:
    file.write(f"Name: {name}\n")
    file.write(f"Age: {age}\n")

print("File written successfully")

