from Abstract.Instruccion import Instruccion
from Abstract.NodoArbol import NodoArbol

class Primitivos(Instruccion):
    def __init__(self, tipo, valor, fila, columna):
        self.tipo = tipo
        self.valor = valor
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        return self.valor

    def getNodo(self):
        nodo = NodoArbol("PRIMITIVO")
        nodo.addHijo(str(self.valor))
        return nodo