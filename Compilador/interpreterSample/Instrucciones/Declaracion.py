from TS.Excepcion import Excepcion
from Abstract.Instruccion import Instruccion
from TS.Simbolo import Simbolo
from Abstract.NodoArbol import  NodoArbol

class Declaracion(Instruccion):
    def __init__(self, tipo, identificador, fila, columna, expresion=None):
        self.identificador = identificador
        self.tipo = tipo
        self.expresion = expresion
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        if self.expresion != None:
            value = self.expresion.interpretar(tree, table) # Valor a asignar a la variable
            if isinstance(value, Excepcion): return value
            self.tipo = self.expresion.tipo
        else:
            value = None
       # if self.tipo != self.expresion.tipo:
        #    return Excepcion("Semantico", "Tipo de dato diferente en Declaracion", self.fila, self.columna)

        simbolo = Simbolo(str(self.identificador), self.tipo, self.fila, self.columna, value)
        result = table.setTabla(simbolo)
        if isinstance(result, Excepcion): return result
        return None

    def getNodo(self):
        nodo = NodoArbol("DECLARACION")
        nodo.addHijo(str(self.tipo))
        nodo.addHijo(str(self.identificador))
        if self.expresion != None:
            nodo.addHijoNode(self.expresion.getNodo())
        return nodo