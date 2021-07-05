from Interprete.Abstract.Instruccion import Instruccion

from Interprete.Abstract.NodoAST import NodoAST

class Break(Instruccion):
    def __init__(self, fila, columna):
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        return self
        
    def getNodo(self):
        nodo = NodoAST("BREAK")
        return nodo