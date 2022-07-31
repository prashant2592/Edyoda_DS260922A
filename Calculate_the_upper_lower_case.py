def lowerUppercnt(str_args):
    lower=0
    upper=0
    for i in str_args:
        if i.islower():
            lower+=1
        elif i.isupper():
            upper+=1
        else:
            pass
    print('No. of Upper case characters :',upper)
    print('No. of Lower case characters :',lower)

string=input("Enter the string:- ") 
lowerUppercnt(string)