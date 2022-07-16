# Write a Python program to get the Fibonacci series between 0 to 50

start=int(input("Enter the start of range: "))
stop=int(input("Enter the stop of range: "))
num1 = 0
num2 = 1
fibonacci=[]
if stop == 1:
    fibonacci.append(num1)
else:
    fibonacci.append(num2)
    for i in range(stop):
        temp = num1 + num2
        num1 = num2
        num2 = temp
        fibonacci.append(temp)

print(f'Fibonacci series between {start} to {stop}: ')
for i in fibonacci:
    if(start<i<stop):
        print(i, end=" ")