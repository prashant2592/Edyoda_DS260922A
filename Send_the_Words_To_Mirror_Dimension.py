# Write a Python program that accepts a word from the user and reverse it.

word=input("Enter the word: ")
print("After reversing : ")
for i in range(-1,-len(word)-1,-1):
    print(word[i],end="")