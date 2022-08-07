lst=[]
length=int(input("Enter the length of list:- "))
for i in range(length):
    num=int(input("Enter the element of list:- "))
    lst.append(num)

func=lambda x:x*3
tripled_list=list(map(func,lst))
print("Triple of list numbers: ",tripled_list)