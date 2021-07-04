from TS.Excepcion import Excepcion
from TS.Tipo import TIPO
from Instrucciones.Funcion import Funcion

class TypeOf(Funcion):
    def __init__(self,nombre , parametros, instrucciones , fila , columna):
        self.nombre = nombre
        self.parametros = parametros
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna
        self.tipo = TIPO.NULO

    def interpretar(self, tree, table):
        simbolo = table.getTabla("typeOf##Param1")
        if simbolo == None: return Excepcion("Semantico","No se encontro el parametro de TypeOf",self.fila,self.columna)
        if simbolo.getTipo() == TIPO.NULO:
            return Excepcion("Semantico", "Tipo de Parametro de TypeOf es Nulo",self.fila , self.columna)
        self.tipo = simbolo.getTipo()

        if self.tipo == TIPO.ENTERO:
            return "INT"
        elif self.tipo == TIPO.DECIMAL:
            return "DOUBLE"
        elif self.tipo == TIPO.BOOLEANO:
            return "BOOLEANO"
        elif self.tipo == TIPO.CHARACTER:
            return "CHAR"
        elif self.tipo == TIPO.CADENA:
            return "STRING"
