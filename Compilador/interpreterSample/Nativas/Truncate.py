from TS.Excepcion import Excepcion
from TS.Tipo import TIPO
from Instrucciones.Funcion import Funcion
class Truncate(Funcion):
    def __init__(self,nombre, parametros, instrucciones , fila , columna ):
        self.nombre = nombre.lower()
        self.parametros = parametros
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna
        self.tipo = TIPO.NULO

    def interpretar(self, tree, table):
        simbolo = table.getTabla("truncate##Param1")
        if simbolo == None: return Excepcion("Semantica", "No se encontro el parametro de Truncate",self.fila,self.columna)
        if simbolo.getTipo() != TIPO.ENTERO:
            return Excepcion("Semantico", "Tipo de parametro de Truncate noes un valor", self.fila,self.columna)
        self.tipo = simbolo.getTipo()
        return int(simbolo.getValor())