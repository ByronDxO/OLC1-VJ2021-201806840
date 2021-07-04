from Abstract.Instruccion import  Instruccion
from TS.Excepcion import Excepcion
from TS.Tipo import TIPO
from Abstract.NodoArbol import NodoArbol
class Casteo(Instruccion):
    def __init__(self,tipo,expresion,fila,columna):
        self.expresion = expresion
        self.fila = fila
        self.columna = columna
        self.tipo = tipo

    def interpretar(self, tree, table):
        val = self.expresion.interpretar(tree, table)

        if self.tipo == TIPO.DECIMAL:  # Tipo a DOUBLE.

            if self.expresion.tipo == TIPO.ENTERO:  # Este es el tipo de la expresion(int).                      -> Int a Double
                try:
                    return float(self.obtenerVal(self.expresion.tipo, val))
                except:
                    return Exception("Semantico", "No se puede castear para Int a Double.", self.fila, self.columna)
            elif self.expresion.tipo == TIPO.CADENA:  # Este es el tipo de la expresion(String).                 -> String a Double
                try:
                    return float(self.obtenerVal(self.expresion.tipo, val))
                except:
                    return Exception("Semantico", "No se puede castear para String a Double.", self.fila, self.columna)
            elif self.expresion.tipo == TIPO.CHAR:  # Este es el tipo de la expresion(Char).                     -> Char a Double
                try:
                    return float(ord(self.obtenerVal(self.expresion.tipo, val)))
                except:
                    return Exception("Semantico", "No se puede castear para Char a Double.", self.fila, self.columna)
            return Exception("Semantico", "Tipo Erroneo de casteo para Double.", self.fila, self.columna)


        elif self.tipo == TIPO.ENTERO:  # Tipo a INT
            #
            if self.expresion.tipo == TIPO.DECIMAL:  # Este es el tipo de la expresion(Double).                    -> Double a Int
                try:
                    return int(self.obtenerVal(self.expresion.tipo, val))
                except:
                    return Exception("Semantico", "No se puede castear para Double a Int.", self.fila, self.columna)

            elif self.expresion.tipo == TIPO.CADENA:  # Este es el tipo de la expresion(String).                   -> String a Int
                try:
                    return int(self.obtenerVal(self.expresion.tipo, val))
                except:
                    return Exception("Semantico", "No se puede castear para String a Int.", self.fila, self.columna)

            elif self.expresion.tipo == TIPO.CHAR:  # Este es el tipo de la expresion(Char).                        -> Char a Int
                try:
                    return ord(self.obtenerVal(self.expresion.tipo, val))
                except:
                    return Exception("Semantico", "No se puede castear para Char a Int.", self.fila, self.columna)
            return Exception("Semantico", "Tipo Erroneo de casteo para Int.", self.fila, self.columna)

        elif self.tipo == TIPO.CHAR:
            if self.expresion.tipo == TIPO.ENTERO:  # Este es el tipo de la expresion(Int).                          -> Int a Char
                try:
                    return chr(self.obtenerVal(self.expresion.tipo, val))
                except:
                    return Exception("Semantico", "No se puede castear para Int a Char.", self.fila, self.columna)
            return Exception("Semantico", "Tipo Erroneo de casteo para Char.", self.fila, self.columna)

        elif self.tipo == TIPO.CADENA:
            if self.expresion.tipo == TIPO.DECIMAL:  # Este es el tipo de la expresion(Double).                    -> Double a String
                try:
                    return str(self.obtenerVal(self.expresion.tipo, val))
                except:
                    return Exception("Semantico", "No se puede castear para Double a String.", self.fila, self.columna)
            elif self.expresion.tipo == TIPO.ENTERO:  # Este es el tipo de la expresion(Int).                        -> Int a String
                try:
                    return str(self.obtenerVal(self.expresion.tipo, val))
                except:
                    return Exception("Semantico", "No se puede castear para Int a String.", self.fila, self.columna)
            return Exception("Semantico", "Tipo Erroneo de casteo para Char.", self.fila, self.columna)

        elif self.tipo == TIPO.BOOLEANO:
            if self.expresion.tipo == TIPO.CADENA:  # Este es el tipo de la expresion(String).                   -> String a Boolean
                try:

                    if str(self.obtenerVal(self.expresion.tipo, val)).lower() == "true":
                        return True
                    elif str(self.obtenerVal(self.expresion.tipo, val)).lower() == "false":
                        return False
                    else:
                        return Exception("Semantico", "No se puede castear para String a Boolean.", self.fila,
                                         self.columna)
                except:
                    return Exception("Semantico", "No se puede castear para String a Boolean.", self.fila, self.columna)
            return Exception("Semantico", "Tipo Erroneo de casteo para Boolean.", self.fila, self.columna)
        return Exception("Semantico", "Tipo erroneo para casteo.", self.fila, self.columna)

    def getNodo(self):
        nodo = NodoArbol("CASTEO")
        nodo.addHijo(str(self.tipo))
        nodo.addHijoNode(self.expresion.getNodo())
        return nodo

    def obtenerVal(self, tipo, val):
        if tipo == TIPO.ENTERO:
            return int(val)
        elif tipo == TIPO.DECIMAL:
            return float(val)
        elif tipo == TIPO.BOOLEANO:
            return bool(val)
        return str(val)

    def toASCII(cadena):
        result = 0
        for char in cadena:
            result += ord(char)
        return result

