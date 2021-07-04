from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion
from TS.Tipo import TIPO
from TS.TablaSimbolos import TablaSimbolos
from Abstract.NodoArbol import NodoArbol
class Return(Instruccion):
    def __init__(self, expresion, fila, columna):
        self.expresion = expresion
        self.fila = fila
        self.columna = columna
        self.tipo = None
        self.result = None

    def interpretar(self, tree, table):
        result = self.expresion.interpretar(tree, table)
        if isinstance(result, Excepcion): return result

        self.tipo = self.expresion.tipo #TIPO DEL RESULT
        self.result = result            #VALOR DEL RESULT

        return self

    def getNodo(self):
        nodo = NodoArbol("RETURN")
        nodo.addHijoNode(self.expresion.getNodo())
        return nodo