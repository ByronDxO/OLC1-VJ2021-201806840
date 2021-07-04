from TS.Excepcion import  Excepcion
from TS.Tipo import  TIPO
from Instrucciones.Funcion import  Funcion
import math

class Round(Funcion):
    def __init__(self,nombre,parametros,instrucciones,fila,columna):
        self.nombre = nombre
        self.parametros = parametros
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        simbolo = table.getTabla("round##Param1")
        if simbolo == None: return Excepcion("Semantico","No se econtro el parametro truncate", self.fila,self.columna)
        if simbolo.getTipo() != TIPO.DECIMAL and simbolo.getTipo() != TIPO.ENTERO:
            return Excepcion("semantico","Tipo de parametro de Round no es un valor",self.fila,self.columna)
        self.tipo = TIPO.ENTERO
        if simbolo.getTipo() == TIPO.DECIMAL:
            if str(simbolo.getValor()).split('.')[1][0] >= '5':
                return int(math.ceil(simbolo.getValor()))
        return round(simbolo.getValor())