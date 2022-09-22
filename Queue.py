class Queue:
    def __init__(self):   #initializing empty stack
        self.items=[]

    def is_empty(self):     #checking if empty
        return self.items==[]

    def enqueue(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[len(self.items)-1]

a=Queue()
a.enqueue(45)
a.enqueue('True')
a.enqueue('dog')
print(a.peek())
print(a.size())
a.dequeue()
print(a.peek())
print(a.is_empty())

