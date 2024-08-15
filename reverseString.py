class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Stack:
    def __init__(self):
        self.root = None

    #Check stack is empty or not 
    def isEmpty(self):
        return True if self.root is None else False
    
    #Method push a new data into stack
    def push(self, data):
        newNode = StackNode(data)
        newNode.next = self.root
        self.root = newNode
    
    #Method pop a data from stack
    def pop(self):
        if self.isEmpty():
            return None
        tmp = self.root
        self.root = self.root.next
        
    #Take the first element of stack
    def peek(self):
        if self.isEmpty():
            return None
        return self.root.data
    
#solve
def reverseString(arr):
    stack = Stack()
    if stack.isEmpty():
        print("Stack is empty")
    
    for i in range(len(arr)):
        stack.push(arr[i])
    
    tmp = ""
    for i in range(len(arr)):
        tmp += stack.peek()
        stack.pop()
    return tmp

str1 = "GeeksQuiz"
str2 = "abc"
str3 = "NguyeMinhTri"
print(reverseString(str1))
print(reverseString(str2))
print(reverseString(str3))