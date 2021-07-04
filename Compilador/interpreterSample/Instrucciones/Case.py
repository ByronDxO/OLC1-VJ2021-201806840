from Instrucciones.Decremento_incremento import Decremento_incremento
from Instrucciones.Declaracion import Declaracion
from Instrucciones.Asignacion import Asignacion
from Abstract.Instruccion import  Instruccion
from TS.Excepcion import  Excepcion
from TS.Tipo import TIPO
from TS.TablaSimbolos import  TablaSimbolos
from Instrucciones.Break import Break
from Abstract.NodoArbol import NodoArbol

class Case(Instruccion):
    def __init__(self,condicion,intrucciones,fila,columna ):
        self.condicion = condicion
        self.intrucciones = intrucciones
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        result = self.condicion.interpretar(tree,table)
        if isinstance(result, Excepcion):return result
        return result
    def getNodo(self):
        nodo = NodoArbol("CASE")
        if self.intrucciones != None:
            nodo.addHijoNode(self.condicion.getNodo())
            instruccionesD = NodoArbol("INSTRUCCIONES CASE")
            for instr in self.intrucciones:
                instruccionesD.addHijoNode(instr.getNodo())
            nodo.addHijoNode(instruccionesD)
        return nodo
    def get_intrucciones_case(self):
        return self.intrucciones
    def set_instrucciones_case(self, instrucciones):
        self.intrucciones = instrucciones