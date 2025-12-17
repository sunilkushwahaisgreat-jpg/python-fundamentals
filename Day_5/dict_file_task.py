this_dict={"Name":"Sunil",
           "College":"NIT SILCHAR",
           "Branch":"EEE"}
with open("student.txt","w") as file:
    for key,value in this_dict.items():
        file.write(f"{key}: {value}\n")

print("File updated successfully")