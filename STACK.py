class Stack:
    def __init__(self,size=4):
        self._stack = []
        self._size = size
    
    def push(self,data):
        if len(self._stack)>= self._size:
            raise Exception('stack overflow')
        else:
            pushElements = self._stack.append(data)
            return pushElements
    
    def pop(self):
        if len(self._stack)<0:
            raise Exception('stack underflow')
        else:
            popElements = self._stack.pop()
            return popElements
    def print(self):
        return print(self._stack)
stack = Stack()
stack.push(3)
stack.push(4)
stack.push(9)
stack.push(9)
print(stack.pop())
stack.print()

