#Q1. Write a program to find all pairs of an integer array whose sum is equal to a given number?

def integerPair(arr,given_no):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if(arr[i]+arr[j]==given_no and i!=j):
                print([i,j])

arr=[]
length=int(input("Enter the length of list:- "))
for i in range(length):
    num=int(input("Enter the element of list:- "))
    arr.append(num)
given_no=int(input("Enter the sum number:- "))
integerPair(arr,given_no)