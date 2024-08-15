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
    
    #Push a new data into stack
    def push(self, data):
        newNode = StackNode(data)
        newNode.next = self.root
        self.root = newNode
        
    #Pop a data from stack
    def pop(self):
        if self.isEmpty():
            return None
        tmp = self.root 
        self.root = self.root.next
    
    #Take first element of stack
    def peek(self):
        if self.isEmpty():
            return None
        return self.root.data
    
#solve    
def validParenthesis(arr):
        stack = Stack()
        stack.push(arr[0])
        for i in range(1, len(arr)):
            if (stack.peek() == "(" and arr[i] == ")") or (stack.peek() == "[" and arr[i] == "]") or (stack.peek() == "{" and arr[i] == "}"): 
                stack.pop()
            else:
                stack.push(arr[i])
        
        if stack.isEmpty():
            print("Balanced")
        else:
            print("Not Balanced")
            
test1 = "[()]{}{[()()]()}"
test2 = "[(])"
test3 = "((()))"

validParenthesis(test1) 
validParenthesis(test2)
validParenthesis(test3)
            
                
                
 
    

            

    
        