class Stack:
        def __init__(self):
            self.items = []

        def is_empty(self):
            return self.items == []

        def push(self, item):
            self.items.insert(0,item)

        def pop(self):
            return self.items.pop(0)

        def view(self):
            return self.items[0]

        def length(self):
            return len(self.items)

class Digito:
    def __init__(self, bool):
        self.bool = bool

    def isdigit(self):
        return int(self) == self

def rpn(expression: str) -> int:
    args: list[str] = expression.split()
    n = len(args)
    m = Stack()
    for i in range(n):
        if not args[i].isdigit():
            if args[i] == "+":
                m.push(f"({m.pop()}+{m.pop()})")
            if args[i] == "*":
                m.push(f"({m.pop()}*{m.pop()})")
            if args[i] == "-":
                if m.length() == 1:
                    m.push(f"-{m.pop()}")
                else:
                    m.push(f"-{m.pop()}+{m.pop()}")
            if args[i] == "/":
                m.push(f"({m.pop()}/{m.pop()})")
        if args[i].isdigit():
            m.push(args[i])
    return eval(m.pop())

