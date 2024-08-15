class Stack:
    def __init__(self):
        self.items = []
      
    def isEmpty(self):
        return self.items == []
      
    def push(self, item):
        self.items.append(item)
      
    def pop(self):
        return self.items.pop()
      
    def peek(self):
        return self.items[len(self.items)-1]
    

    
#solve 
def next_greater_ele(arr):
    stack = Stack()
    stack.push(arr[0])
    for i in range(1, len(arr)):
        if(stack.isEmpty()):
            stack.push(arr[i])
            
        while(stack.isEmpty() == False and stack.peek() < arr[i]):
            print(str(stack.peek()) + "-->" + str(arr[i]))
            stack.pop()
            
        stack.push(arr[i])
        
    while(stack.isEmpty() == False):
        print(str(stack.peek()) + "-->" + "-1")
        stack.pop() 
        
arr = [11, 13, 21, 3]
next_greater_ele(arr)