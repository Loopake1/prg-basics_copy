class myStack():
    def __init__(self):
        self.Stack = []
    def get(self):
        return self.Stack.pop(-1)
    def put(self,value):
        return self.Stack.append(value)
    def empty(self):
        return len(self.Stack)==0