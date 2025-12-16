#Q3 Maximum element in a list
def find_max(numbers):
    max_val = numbers[0]
    for val in numbers:
        if(val>max_val):
            max_val = val
    
    return max_val

#Q4 Sum of elements in a list
def find_sum(numbers):
    total=0
    for val in numbers:
        total+=val

    return total

numbers=[3,7,2,9,4]

print("Max element in list is:",find_max(numbers))
print("Sum of all element in list is:",find_sum(numbers))
