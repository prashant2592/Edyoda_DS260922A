#Q4. Write a program to print the first non-repeated character from a string?

def first_non_repeated_character(string):
    for i in string:
        if(string.count(i)==1):
            return i

string=input("ENTER THE STRING:- ")
print(first_non_repeated_character(string))