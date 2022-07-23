size=int(input("Enter the size of list:- "))
list1=[]
for i in range(size):
    tup=input("Enter the element as x,y: ")
    tmp_lst=tup.split(",")
    list1.append([int(tmp_lst[0]),int(tmp_lst[1])])
    tuple_list=list(map(tuple,list1))

print("Sample List: ",tuple_list)

ind=1
temp=0
for i in range(len(tuple_list)):
    for j in range(i+1,len(tuple_list)):
        if(tuple_list[i][ind]>tuple_list[j][ind]):
            temp=tuple_list[i]
            tuple_list[i]=tuple_list[j]
            tuple_list[j]=temp
        else:
            pass
    
print("Expected Result:- ",tuple_list)

