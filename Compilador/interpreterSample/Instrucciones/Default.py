from Instrucciones.Decremento_incremento import  Decremento_incremento
from Instrucciones.Declaracion import  Declaracion
from Instrucciones.Asignacion import Asignacion
from Abstract.Instruccion import Instruccion
from TS.Excepcion import  Excepcion
from TS.TablaSimbolos import  TablaSimbolos
from Instrucciones.Break import  Break
from Abstract.NodoArbol import  NodoArbol

class Default(Instruccion):
    def __init__(self,instrucciones , fila , columna ):
        self.condicion = None
        self.intrucciones = instrucciones
        self.fila = fila
        self.columna = columna
    def interpretar(self, tree, table):
        return None
    def getNodo(self):
        nodo = NodoArbol("DEFAULT")
        if self.intrucciones != None:
            instruccionesDefault = NodoArbol("INTRUCCIONES DEFAULT")
            for instr in self.intrucciones:
                instruccionesDefault.addHijoNode(instr.getNodo())
            nodo.addHijoNode(instruccionesDefault)
        return nodo

    def get_instrucciones_default(self):
        return self.instrucciones

    def set_instrucciones_default(self, instrucciones):
        self.instrucciones = instrucciones