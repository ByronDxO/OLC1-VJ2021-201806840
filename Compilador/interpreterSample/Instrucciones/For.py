from Instrucciones.Return import Return
from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion
from TS.Tipo import TIPO
from TS.TablaSimbolos import TablaSimbolos
from Instrucciones.Break import Break

class For(Instruccion):
    def __init__(self,variable,condicion,actualizacion,instrucciones,fila,columna):
        self.variable = variable
        self.condicion = condicion
        self.actualizacion= actualizacion
        self.intrucciones= instrucciones
        self.fila = fila
        self.columna = columna
    def interpretar(self, tree, table):
        new_tabla =  TablaSimbolos(table)
        declaracion = self.variable.interpretar(tree,new_tabla)
        if isinstance(declaracion, Exception):return declaracion
        while True:
