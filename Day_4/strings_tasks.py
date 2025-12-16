#Q1: Count number of vowels in a string
def count_vowels(text):
    vowels="aeiouAeiou"
    count=0
    for char in text:
        if char in vowels:
            count+=1
    
    return count

#Q2 Reverse string
def reverse_string(text):
    revstring=""
    for char in text:
        revstring=char+revstring

    return revstring

text=input("Enter a string: ")

print("Number of vowels in string is:",count_vowels(text))
print("The reverse string is:",reverse_string(text))


