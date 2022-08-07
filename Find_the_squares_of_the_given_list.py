lst=[]
length=int(input("Enter the length of list:- "))
for i in range(length):
    num=int(input("Enter the element of list:- "))
    lst.append(num)

func=lambda x:x**2
squared_list=list(map(func,lst))
print("Square the elements of the list: ",squared_list)