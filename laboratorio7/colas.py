class Nodo:
    def __init__(self, item, token=False):
        self.dato = item
        self.siguiente = None
        self.token = token

class Cola:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head == None
    
    def enqueue(self, item, token=False):
        nuevo_nodo = Nodo(item, token)

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
    
    def marca(self):
        return self.head.token
    
    def maximo(self):
        if not self.is_empty():
            maximo = self.head.dato
            actual = self.head.siguiente

            while actual is not None:
                if actual.dato > maximo:
                    maximo = actual.dato
                actual = actual.siguiente

            return maximo
        
        