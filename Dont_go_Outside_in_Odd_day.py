#Write a Python program to count the number of even and odd numbers from a series of numbers.

numbers=input("Please enter the number seperated by comma :") #Say-- 1,2,3,4,5,6,7,8,9
odd=0
even=0
lst=numbers.split(",")
for i in lst:
    if(int(i)%2==0):
        even=even+1
    else:
        odd=odd+1

print("Number of even numbers : ",even)
print("Number of odd numbers : ",odd)