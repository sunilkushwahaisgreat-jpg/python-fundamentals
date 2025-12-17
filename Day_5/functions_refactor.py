#Q1 Checking a string is palindrome or not
def is_palindrome(text):
    text=text.lower()
    s=0
    e=len(text)-1
    while s<e:
        if text[s]!=text[e]:
            return False
        s+=1
        e-=1
    
    return True

#Q2 Count word in a string
def count_words(sentence):
    words=sentence.split()
    return len(words)

text=input("Enter a text to check for palindrome:")
print("given text is palindrome:",is_palindrome(text))

sentence=input("Enter a sentence: ")
print("No fof words in this senetence is:",count_words(sentence))




