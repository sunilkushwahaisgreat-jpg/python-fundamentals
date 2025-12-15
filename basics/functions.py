# name function
def greet_user(name):
    print("Hello", name)

#square 
def square(num):
    return num*num

#is_even
def is_even(num):
    if num%2==0:
        return True
    else:
        return False

name=input("Enter name")
greet_user(name)

num=int(input("enter a number:"))
print("Square of",num,"is:",square(num))
print(num,"is even:",is_even(num))