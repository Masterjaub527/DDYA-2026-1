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
print(n.cola())


#1
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


#2
def solve1(n, answer):
    dp = []
    via = pila.Stack()
    j = 0

    for i in range(n):
        count = i + 1
        via.push(count)

        while (not via.is_empty()
               and j < len(answer)
               and answer[j] == via.head()):
            dp.append(via.pop())
            j += 1

    return dp == answer

print(solve1(5, [3,2,5,4,1]))


def solve2(n):
    cards = colas.Cola()    
    for i in range(1, n + 1):
        cards.enqueue(i)
    dp  = []
    while cards.length() > 1:
        dp.append(cards.cabeza())
        cards.dequeue()
        cards.enqueue(cards.cabeza())
        cards.dequeue()
    return f"Discarded  cards: {", ".join(map(str, dp))}, Remaining card: {cards.cabeza()}"
print(solve2(7))


#4
def solve3(array, mi_trabajo):
    trabajo_realizado = False
    t = 0
    m = colas.Cola()
    for i, item in enumerate(array):
        m.enqueue(item, token=(i == mi_trabajo))

    while not trabajo_realizado:
        if m.cabeza() == m.maximo():
            t += 1
            if m.head.token:
                trabajo_realizado = True
            m.dequeue()
        else:
            if m.head.token:
                m.enqueue(m.cabeza(), True)
                m.dequeue()
            else:
                m.enqueue(m.cabeza())
                m.dequeue()
            t += 1
    return t
print(solve3([1,1,9,1], 0))