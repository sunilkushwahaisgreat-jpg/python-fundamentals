num=[2,4,6,8,10]

print(num)
print(num[0])
print(num[-1])

for value in num:
    print(value)

total=0
for value in num:
    total+=value

print("Sum of all elements in list is:",total)