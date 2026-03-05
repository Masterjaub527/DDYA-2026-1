class Nodo:
    def __init__(self, item):
        self.dato = item
        self.siguiente = None

class Cola:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head == None
    
    def enqueue(self, item):
        nuevo_nodo = Nodo(item)

        if self.is_empty():
            self.head = nuevo_nodo
            self.tail = nuevo_nodo
        else:
            self.tail.siguiente = nuevo_nodo
            self.tail = nuevo_nodo
        
    def dequeue(self):
        if not self.is_empty():
            dato = self.head.dato
            self.head = self.head.siguiente
            return dato
        
    def cabeza(self):
        if not self.is_empty():
            return self.head.dato
        
    def cola(self):
        if not self.is_empty():
            return self.tail.dato
        
    def length(self):
        contador = 0
        nodo_actual = self.head
        while nodo_actual is not None:
            contador += 1
            nodo_actual = nodo_actual.siguiente
        return contador