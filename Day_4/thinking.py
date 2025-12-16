li=[]
for i in range (0,5):
    a=int(input("Enter element of list:"))
    li.append(a)
    
print("Given list is:",li)

maxi=li[0]
mini=li[0]

for val in li:
    if maxi<val:
        maxi=val
    if mini>val:
        mini=val

print("Minimum value in list is:",mini)
print("Maximum value in list is:",maxi)
