class Stack:
    def __init__(self):   #initializing empty stack
        self.items=[]

    def is_empty(self):     #checking if empty
        return self.items==[]

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

def evenorodd(num):
    if num%2==0:
        print("EVEN")
    else:
        print("ODD")

evenorodd(6)
a=Stack()
a.push(45)
a.push('True')
a.push('dog')
print(a.size())
print(a.peek())
a.pop()
print(a.peek())
print(a.is_empty())

