class Stack:
    def __init__(self):
        self.Elements = []
        self.top = None
    def push(self, value):
        self.Elements.append(value)
    def pop(self):
        return self.Elements.pop()
    def empty(self):
        return self.Elements == []
    def show(self):
        for value in reversed(self.Elements):
            print(value)
    def getMin(self):
        print(min(self.Elements))

#--------------------------------------------------------------
#Q9. Write a program to reverse a stack.
#--------------------------------------------------------------
def BottomInsert(s, value):
    if s.empty(): 
        s.push(value)
    else:
        popped = s.pop()
        BottomInsert(s, value)
        s.push(popped)

def Reverse(s):
    if s.empty():
        pass
    else:
        popped = s.pop()
        Reverse(s)
        BottomInsert(s, popped)
  
  
stk = Stack()
 
stk.push(23)
stk.push(21)
stk.push(32)
stk.push(41)
stk.push(55)
  
print("Original Stack")
stk.show()
  
print("\nStack after Reversing")
Reverse(stk)
stk.show()

#--------------------------------------------------------------
#Q10. Write a program to find the smallest number using a stack.
#--------------------------------------------------------------

print("Minimum value in Stack")
stk.getMin()


