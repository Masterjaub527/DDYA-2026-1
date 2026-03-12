class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None
        self.contador = 1

class Arbol:
    def __init__(self):
        self.raiz = None

    def insert(self, valor):
        nuevo = Nodo(valor)

        if self.raiz is None:
            self.raiz = nuevo
        else:
            self._insert(self.raiz, nuevo)

    def _insert(self, actual, nuevo):
        if nuevo.valor < actual.valor:
            if actual.izq is None:
                actual.izq = nuevo
            else:
                self._insert(actual.izq, nuevo)
        else:
            if actual.der is None:
                actual.der = nuevo
            else:
                self._insert(actual.der, nuevo)


arbol = Arbol()
arbol.insert(6)
arbol.insert(8)
arbol.insert(2)
arbol.insert(9)
arbol.insert(3)
arbol.insert(1)
def preorden(nodo):
    if nodo:
        print(nodo.valor, end=" ")
        preorden(nodo.izq)
        preorden(nodo.der)

def inorden(nodo):
    if nodo:
        inorden(nodo.izq)
        print(nodo.valor, end=" ")
        inorden(nodo.der)

def postorden(nodo):
    if nodo:
        preorden(nodo.izq)
        preorden(nodo.der)
        print(nodo.valor, end=" ")

def preorden_list(nodo, dp=[]):
    if not nodo: return
    dp.append(nodo.valor)
    preorden_list(nodo.izq)
    preorden_list(nodo.der)
    return dp

print(preorden_list(raiz))

def inorden_list(nodo, dp=[]):
    if not nodo: return
    inorden_list(nodo.izq)
    dp.append(nodo.valor)
    inorden_list(nodo.der)
    return dp

print(inorden_list(raiz))

def postorden_list(nodo, dp=[]):
    if not nodo: return
    postorden_list(nodo.izq)
    postorden_list(nodo.der)
    dp.append(nodo.valor)
    return dp

print(postorden_list(raiz))

def es_hoja(nodo):
  if nodo is None:
    return False
  return nodo.izq is None and nodo.der is None


def suma_de_caminos(nodo, suma_acumulada=0):
    if not nodo: return 
    suma_actual = suma_acumulada + nodo.valor

    if es_hoja(nodo):
        print(f"Camino acabado {nodo.valor}. Suma total {suma_actual}")

    suma_de_caminos(nodo.izq, suma_actual)
    suma_de_caminos(nodo.der, suma_actual)

suma_de_caminos(raiz)