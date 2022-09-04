#Q2. Write a program to reverse an array in place? In place means you cannot create a new array. You have to update the original array.

def reverse_array(arr):
    return arr[::-1]

arr=[]
length=int(input("Enter the length of list:- "))
for i in range(length):
    num=int(input("Enter the element of list:- "))
    arr.append(num)
print(reverse_array(arr))