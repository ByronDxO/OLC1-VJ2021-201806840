from TS.Excepcion import Excepcion
from Abstract.Instruccion import Instruccion
from TS.Simbolo import Simbolo
from Abstract.NodoArbol import  NodoArbol

class Asignacion(Instruccion):
    def __init__(self, identificador, expresion, fila, columna):
        self.identificador = identificador
        self.expresion = expresion
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        value = self.expresion.interpretar(tree, table) # Valor a asignar a la variable
        if isinstance(value, Excepcion): return value

        simbolo = Simbolo(self.identificador, self.expresion.tipo, self.fila, self.columna, value)

        result = table.actualizarTabla(simbolo)

        if isinstance(result, Excepcion): return result
        return None
    def getNodo(self):
        nodo = NodoArbol("ASIGNACION")
        nodo.addHijo(str(self.expresion.tipo))
        nodo.addHijo(str(self.identificador))
        nodo.addHijoNode(self.expresion.getNodo())
        return nodo

