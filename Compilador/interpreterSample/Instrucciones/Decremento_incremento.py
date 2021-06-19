from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion
from TS.Tipo import OperadorAritmetico,TIPO
from TS.TablaSimbolos import TablaSimbolos
from TS.Simbolo import Simbolo
from Expresiones.Identificador import Identificador

class Decremento_incremento(Instruccion):
    def __init__(self,identificador,tipo,fila,columna):
        self.identificador = identificador
        self.tipo=tipo
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        if self.tipo == OperadorAritmetico.INCREMENTO:
            simbolo = table.getTabla(self.identificador.lower())
            if simbolo.tipo == TIPO.ENTERO or simbolo.tipo == TIPO.DECIMAL:
                value = simbolo.valor +1
                self.tipo = simbolo.tipo
        elif self.tipo == OperadorAritmetico.DECREMENTO:
            simbolo = table.getTabla(self.identificador.lower())
            if simbolo.tipo == TIPO.ENTERO or simbolo.tipo == TIPO.DECIMAL:
                value = simbolo.valor -1
                self.tipo = simbolo.tipo
        else:
            return Excepcion("Semantico", "Dato no compatible, solo se aceptan INT y DOUBLE", self.fila, self.columna)
        new_symbol = Simbolo(self.identificador,self.tipo,self.fila,self.columna,value)
        result = table.actualizarTabla(new_symbol)
        if isinstance(result, Exception): return result
        return None