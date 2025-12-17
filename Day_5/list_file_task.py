li=[]
for i in range(0,5):
    a=int(input(f"Enter {i+1} element:"))
    li.append(a)

with open("numbers.txt","w") as file:
    for val in li:
        file.write(f"{val}\n")
    
print("File successfully updated")