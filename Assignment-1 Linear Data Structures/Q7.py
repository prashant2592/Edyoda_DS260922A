#Q7. Write a program to convert prefix expression to infix expression.

def prefixToInfix(prefix):
    operators=["+","-","*","/"]
    s = []
    i = len(prefix) - 1
    while i >= 0:
        if prefix[i] not in operators:
            s.append(prefix[i])
            i -= 1
        else:
            string = "(" + s.pop() + prefix[i] + s.pop() + ")"
            s.append(string)
            i -= 1
     
    return s.pop()

str = input("ENTER THE EXPRESSION:- ") #SAMPLE EXP ---> "*+AB-CD"
print(prefixToInfix(str))