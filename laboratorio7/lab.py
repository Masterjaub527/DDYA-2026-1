import pila
import colas

m = pila.Stack()
m.push(1)
m.push(2)
m.push(3)
print(m.tail())
print(m.head())

n = colas.Cola()
n.enqueue(1)
n.enqueue(2)
n.enqueue(3)
print(n.cabeza())
print(n.cola)
      
def solve(string):
    m = pila.Stack()
    for elemento in string:
        if elemento in "[(":
            m.push(elemento)

        elif elemento == "]" and m.pop() == "[":
            continue

        elif elemento == ")" and m.pop() == "(":
            continue
        else:
            return False
        
    return True

print(solve("([()])"))
