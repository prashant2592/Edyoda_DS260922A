def sumList(lst_arg):
    sum=0
    for i in lst_arg:
        sum+=i
    return sum

lst=[]
length=int(input("Enter the length of list:- "))
for i in range(length):
    num=int(input("Enter the element of list:- "))
    lst.append(num)

print("Sum : ",sumList(lst))