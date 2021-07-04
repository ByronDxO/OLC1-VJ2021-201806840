from TS.Excepcion import Excepcion
from TS.Tipo import TIPO
from Instrucciones.Funcion import  Funcion

class Lenght(Funcion):
    def __init__(self,nombre,parametros,instrucciones,fila,columna):
        self.nombre = nombre
        self.parametros = parametros
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        simbolo = table.getTabla("length##Param1")
        if simbolo == None: return Excepcion("Semantico","No se encontro el parametro para lenght ",self.fila,self.columna)
        if simbolo.getTipo() != TIPO.CADENA:
            return Excepcion("Semantico", "Tipo de aparametro de lenght no es cadena ",self.fila,self.columna)
        self.tipo = simbolo.getTipo()
        return len(simbolo.getValor())