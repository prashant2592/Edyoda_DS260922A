#Q3. Write a program to check if two strings are a rotation of each other?

def areRotations(str1,str2):
    str1_1=str1[0:(len(str1)//2)]
    str1_2=str1[len(str2)//2:len(str2)]
    str2_1=str2[0:(len(str1)//2)]
    str2_2=str2[len(str2)//2:len(str2)] 
    
    if((str1_1==str2_2) and (str1_2==str2_1)):
        print(f"{str1} is a rotated form of {str2}")
    else:
        print(f"{str1} is not a rotated form of {str2}")
        
string1=input("ENTER THE STRING 1 :- ")
string2=input("ENTER THE STRING 2 :- ")

if(len(string1)==len(string2)):
    areRotations(string1,string2)
else:
    print(f"{string1} is not a rotated form of {string2}")