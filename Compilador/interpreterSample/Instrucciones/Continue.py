from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion
from TS.Tipo import TIPO
from TS.TablaSimbolos import TablaSimbolos
from Abstract.NodoArbol import NodoArbol

class Continue(Instruccion):
    def __init__(self,fila , columna ):
        self.fila = fila
        self.columna = columna
    def interpretar(self, tree, table):
        return self
    def getNodo(self):
        nodo = NodoArbol("CONTINUE")
        return nodo
