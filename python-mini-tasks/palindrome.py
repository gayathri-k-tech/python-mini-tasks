# Program: Palindrome Checker
# Author: Gayathri K

def is_palindrome(text):
    text = text.lower().replace(" ", "")
    return text == text[::-1]

word = input("Enter a word: ")

if is_palindrome(word):
    print("It is a palindrome !")
else:
    print("Not a palindrome !")