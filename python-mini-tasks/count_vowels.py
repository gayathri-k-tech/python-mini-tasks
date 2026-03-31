# Program: Count Vowels
# Author: Gayathri K

def count_vowels(text):
    vowels = "aeiou"
    count = 0
    for char in text.lower():
        if char in vowels:
            count += 1
    return count

sentence = input("Enter a sentence: ")
print("Number of vowels:", count_vowels(sentence))