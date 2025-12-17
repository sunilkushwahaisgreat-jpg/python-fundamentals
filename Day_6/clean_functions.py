def safe_divide(a,b):
    if b==0 :
        return "cannot divide by zero"
    else:
        return a/b

def calculate_percentage(marks):
    if len(marks)==0:
        return 0
    total=0
    for val in marks:
        total+=val
    
    return (total/(len(marks)*100))*100
    
a, b=map(int, input("Enter dividend and divisor:").split())
print("Result",safe_divide(a,b))

marks=[80,90,70]
print("Percentage of Marks is:",calculate_percentage(marks))


