try:
    a, b=map(int, input("Enter divivdend and divisor: ").split())
    x=a/b
    print("Result: ",x)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input.Please enter numbers only")
finally:
    print("Program ended successfully")