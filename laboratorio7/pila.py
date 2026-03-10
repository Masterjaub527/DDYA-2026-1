class Stack:
        def __init__(self):
            self.items = []

        def is_empty(self):
            return self.items == []

        def push(self, item):
            self.items.insert(0,item)

        def pop(self):
            return self.items.pop(0)

        def head(self):
            return self.items[0]

        def length(self):
            return len(self.items)
        
        def tail(self):
            return self.items[self.length()-1]
