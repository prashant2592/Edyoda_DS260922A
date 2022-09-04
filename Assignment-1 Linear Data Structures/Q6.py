#Q6. Read about infix, prefix, and postfix expressions. Write a program to convert postfix to prefix expression.

def postToPre(post_exp):
    operators=["+","-","*","/"]
    s = []
    for i in range(len(post_exp)):
        if (post_exp[i] in operators):
            op1 = s[-1]
            s.pop()
            op2 = s[-1]
            s.pop()
            temp = post_exp[i] + op2 + op1
            s.append(temp)
        else:
            s.append(post_exp[i])
            
    ans = ""
    for i in s:
        ans += i
    return ans
 

post_exp = input("ENTER THE EXPRESSION:- ") #SAMPLE EXP ---> "AB+CD-*"
print("Prefix : ", postToPre(post_exp))