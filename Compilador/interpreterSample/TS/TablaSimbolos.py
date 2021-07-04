

from TS.Excepcion import Excepcion
from TS.Tipo import *

class TablaSimbolos:
    def __init__(self, anterior = None):
        self.tabla = {} # Diccionario Vacio
        self.anterior = anterior

    def setTabla(self, simbolo):      # Agregar una variable
        if simbolo.id.lower() in self.tabla :
            return Excepcion("Semantico", "Variable " + simbolo.id + " ya existe", simbolo.fila, simbolo.columna)
        else:
            self.tabla[simbolo.id.lower()] = simbolo
            return None

    def getTabla(self, id):            # obtener una variable
        tablaActual = self
        while tablaActual != None:
            if id in tablaActual.tabla :
                return tablaActual.tabla[id]           # RETORNA SIMBOLO
            else:
                tablaActual = tablaActual.anterior
        return None

    def actualizarTabla(self, simbolo):
        tablaActual = self
        while tablaActual != None:
            if simbolo.id.lower() in tablaActual.tabla:
                if tablaActual.tabla[simbolo.id.lower()].getTipo() == simbolo.getTipo() or tablaActual.tabla[simbolo.id].getTipo() is TIPO.NULO or simbolo.getTipo() is TIPO.NULO:
                    tablaActual.tabla[simbolo.id.lower()].setValor(simbolo.getValor())
                    tablaActual.tabla[simbolo.id.lower()].setTipo(simbolo.getTipo())
                    return None             #VARIABLE ACTUALIZADA
                return Excepcion("Semantico", "Tipo de dato Diferente en Asignacion", simbolo.getFila(), simbolo.getColumna())
            else:
                tablaActual = tablaActual.anterior
                if tablaActual is None:
                    return None
        return Excepcion("Semantico", "Variable No encontrada en Asignacion", simbolo.getFila(), simbolo.getColumna())
        
    
