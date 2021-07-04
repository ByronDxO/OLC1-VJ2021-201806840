from re import A
from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion
from TS.Tipo import TIPO, OperadorAritmetico
from Abstract.NodoArbol import NodoArbol
class Aritmetica(Instruccion):
    def __init__(self, operador, OperacionIzq, OperacionDer, fila, columna):
        self.operador = operador
        self.OperacionIzq = OperacionIzq
        self.OperacionDer = OperacionDer
        self.fila = fila
        self.columna = columna
        self.tipo = None

    
    def interpretar(self, tree, table):
        izq = self.OperacionIzq.interpretar(tree, table)
        if isinstance(izq, Excepcion): return izq
        if self.OperacionDer != None:
            der = self.OperacionDer.interpretar(tree, table)
            if isinstance(der, Excepcion): return der


        if self.operador == OperadorAritmetico.MAS: #SUMA
            #enteros
            #entero + entero
            if self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.ENTERO:
                self.tipo = TIPO.ENTERO
                return self.obtenerVal(self.OperacionIzq.tipo, izq) + self.obtenerVal(self.OperacionDer.tipo, der)
            #entero + decimal
            elif self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.DECIMAL:
                self.tipo = TIPO.DECIMAL
                return self.obtenerVal(self.OperacionIzq.tipo, izq) + self.obtenerVal(self.OperacionDer.tipo, der)
            #entero + cadena
            elif self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.CADENA:
                self.tipo = TIPO.CADENA
                return str(self.obtenerVal(self.OperacionIzq.tipo, izq)) + self.obtenerVal(self.OperacionDer.tipo, der)
            #entero + booleano
            elif self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.BOOLEANO:
                self.tipo = TIPO.ENTERO
                return self.obtenerVal(self.OperacionIzq.tipo, izq) + self.obtenerVal(self.OperacionDer.tipo, der)
            #cadena + entero
            elif self.OperacionIzq.tipo == TIPO.CADENA and self.OperacionDer.tipo == TIPO.ENTERO:
                self.tipo = TIPO.CADENA
                return self.obtenerVal(self.OperacionIzq.tipo, izq) + str(self.obtenerVal(self.OperacionDer.tipo, der))
                # cadena + double
            elif self.OperacionIzq.tipo == TIPO.CADENA and self.OperacionDer.tipo == TIPO.DECIMAL:
                self.tipo = TIPO.CADENA
                return self.obtenerVal(self.OperacionIzq.tipo, izq) + str(self.obtenerVal(self.OperacionDer.tipo, der))
            #double
            #double + int
            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.ENTERO:
                self.tipo = TIPO.DECIMAL
                return self.obtenerVal(self.OperacionIzq.tipo, izq) + self.obtenerVal(self.OperacionDer.tipo, der)
            #double + double
            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.DECIMAL:
                self.tipo = TIPO.DECIMAL
                return self.obtenerVal(self.OperacionIzq.tipo, izq) + self.obtenerVal(self.OperacionDer.tipo, der)
            #double + string
            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.CADENA:
                self.tipo = TIPO.CADENA
                return str(self.obtenerVal(self.OperacionIzq.tipo, izq)) + self.obtenerVal(self.OperacionDer.tipo, der)
            #double + boolean
            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.BOOLEANO:
                self.tipo = TIPO.DECIMAL
                return self.obtenerVal(self.OperacionIzq.tipo, izq) + self.obtenerVal(self.OperacionDer.tipo, der)
            #boolean
            #boolean + int
            elif self.OperacionIzq.tipo == TIPO.BOOLEANO and self.OperacionDer.tipo == TIPO.ENTERO:
                self.tipo = TIPO.ENTERO
                return self.obtenerVal(self.OperacionIzq.tipo, izq) + self.obtenerVal(self.OperacionDer.tipo, der)
            #boolean + double
            elif self.OperacionIzq.tipo == TIPO.BOOLEANO and self.OperacionDer.tipo == TIPO.DECIMAL:
                self.tipo = TIPO.DECIMAL
                return self.obtenerVal(self.OperacionIzq.tipo, izq) + self.obtenerVal(self.OperacionDer.tipo, der)
            #boolean + cadena
            elif self.OperacionIzq.tipo == TIPO.BOOLEANO and self.OperacionDer.tipo == TIPO.CADENA:
                self.tipo = TIPO.CADENA
                return str(self.obtenerVal(self.OperacionIzq.tipo, izq)) + self.obtenerVal(self.OperacionDer.tipo, der)
            # boolean + int
            elif self.OperacionIzq.tipo == TIPO.BOOLEANO and self.OperacionDer.tipo == TIPO.BOOLEANO:
                self.tipo = TIPO.ENTERO
                return bool(self.obtenerVal(self.OperacionIzq.tipo, izq)) + bool(
                    self.obtenerVal(self.OperacionDer.tipo, der))
            #char
            #cahr + char
            elif self.OperacionIzq.tipo == TIPO.CHARACTER and self.OperacionDer.tipo == TIPO.CHARACTER:
                self.tipo = TIPO.CHARACTER
                return str(self.obtenerVal(self.OperacionIzq.tipo, izq)) + self.obtenerVal(self.OperacionDer.tipo, der)
            #char + cadena
            elif self.OperacionIzq.tipo == TIPO.CHARACTER and self.OperacionDer.tipo == TIPO.CADENA:
                self.tipo = TIPO.CADENA
                return bool(self.obtenerVal(self.OperacionIzq.tipo, izq)) + bool(
                    self.obtenerVal(self.OperacionDer.tipo, der))
            #cadena
            #cadena + int
            elif self.OperacionIzq.tipo == TIPO.CADENA and self.OperacionDer.tipo == TIPO.ENTERO:
                self.tipo = TIPO.CADENA
                return self.obtenerVal(self.OperacionIzq.tipo, izq) + str(self.obtenerVal(self.OperacionDer.tipo, der))
            #cadena + double
            elif self.OperacionIzq.tipo == TIPO.CADENA and self.OperacionDer.tipo == TIPO.DECIMAL:
                self.tipo = TIPO.CADENA
                return self.obtenerVal(self.OperacionIzq.tipo, izq) + str(self.obtenerVal(self.OperacionDer.tipo, der))
            #cadena + cadena
            elif self.OperacionIzq.tipo == TIPO.CADENA and self.OperacionDer.tipo == TIPO.CADENA:
                self.tipo = TIPO.CADENA
                return str(self.obtenerVal(self.OperacionIzq.tipo, izq)) + self.obtenerVal(self.OperacionDer.tipo, der)
            #cadena + boolean
            elif self.OperacionIzq.tipo == TIPO.CADENA and self.OperacionDer.tipo == TIPO.BOOLEANO:
                self.tipo = TIPO.CADENA
                return self.obtenerVal(self.OperacionIzq.tipo, izq) + self.obtenerVal(self.OperacionDer.tipo, der)
            #cadena + char
            elif self.OperacionIzq.tipo == TIPO.CADENA and self.OperacionDer.tipo == TIPO.CHAR:
                self.tipo = TIPO.CADENA
                return self.obtenerVal(self.OperacionIzq.tipo, izq) + self.obtenerVal(self.OperacionDer.tipo, der)
            return Excepcion("Semantico", "Tipo Erroneo de operacion para +.", self.fila, self.columna)

            #resta
        elif self.operador == OperadorAritmetico.MENOS: #RESTA
            #entero
            # entero - entero
            if self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.ENTERO:
                self.tipo = TIPO.ENTERO
                return self.obtenerVal(self.OperacionIzq.tipo, izq) - self.obtenerVal(self.OperacionDer.tipo, der)
            # int - double
            elif self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.DECIMAL:
                self.tipo = TIPO.DECIMAL
                return round(
                    (self.obtenerVal(self.OperacionIzq.tipo, izq) - self.obtenerVal(self.OperacionDer.tipo, der)), 2)
            # int - boolean  = int
            elif self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.BOOLEANO:
                self.tipo = TIPO.ENTERO
                return self.obtenerVal(self.OperacionIzq.tipo, izq) - self.obtenerVal(self.OperacionDer.tipo, der)
            #double
            #double - entero
            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.ENTERO:
                self.tipo = TIPO.DECIMAL
                return round((self.obtenerVal(self.OperacionIzq.tipo, izq) - self.obtenerVal(self.OperacionDer.tipo, der)), 2)
            # double - double
            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.DECIMAL:
                self.tipo = TIPO.DECIMAL
                return round((self.obtenerVal(self.OperacionIzq.tipo, izq) - self.obtenerVal(self.OperacionDer.tipo, der)), 2)
            # double - boolean
            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.BOOLEANO:
                self.tipo = TIPO.DECIMAL
                return round((self.obtenerVal(self.OperacionIzq.tipo, izq) - self.obtenerVal(self.OperacionDer.tipo, der)), 2)
            #boolena
            # boolean - int
            elif self.OperacionIzq.tipo == TIPO.BOOLEANO and self.OperacionDer.tipo == TIPO.ENTERO:
                self.tipo = TIPO.ENTERO
                return self.obtenerVal(self.OperacionIzq.tipo, izq) - self.obtenerVal(self.OperacionDer.tipo, der)
            # boolean - double
            elif self.OperacionIzq.tipo == TIPO.BOOLEANO and self.OperacionDer.tipo == TIPO.DECIMAL:
                self.tipo = TIPO.DECIMAL
                return round((self.obtenerVal(self.OperacionIzq.tipo, izq) - self.obtenerVal(self.OperacionDer.tipo, der)), 2)
            return Excepcion("Semantico", "Tipo Erroneo de operacion para -.", self.fila, self.columna)

        #multiplicacion
        elif self.operador == OperadorAritmetico.POR: #MULTIPLICACION
                # int * int
            if self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.ENTERO:
                self.tipo = TIPO.ENTERO
                return self.obtenerVal(self.OperacionIzq.tipo, izq) * self.obtenerVal(self.OperacionDer.tipo, der)
            #int * double
            elif self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.DECIMAL:
                self.tipo = TIPO.DECIMAL
                return round(
                    (self.obtenerVal(self.OperacionIzq.tipo, izq) * self.obtenerVal(self.OperacionDer.tipo, der)), 2)
                # DOUBLE
            #double * int
            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.ENTERO:
                self.tipo = TIPO.DECIMAL
                return round(
                    (self.obtenerVal(self.OperacionIzq.tipo, izq) * self.obtenerVal(self.OperacionDer.tipo, der)), 2)
            #double * double
            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.DECIMAL:
                self.tipo = TIPO.DECIMAL
                return round((self.obtenerVal(self.OperacionIzq.tipo, izq) * self.obtenerVal(self.OperacionDer.tipo, der)), 2)
            return Excepcion("Semantico", "Tipo Erroneo de operacion para *.", self.fila, self.columna)

        elif self.operador == OperadorAritmetico.DIV:

            if self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.ENTERO:  # int / int     = double
                if self.obtenerVal(self.OperacionDer, der) == 0:
                    return Excepcion("semantico", ">operacion invalida no se puede operar entre 0<", self.fila,
                                     self.columna)
                else:
                    self.tipo = TIPO.DECIMAL
                    return round((self.obtenerVal(self.OperacionIzq.tipo, izq) / self.obtenerVal(self.OperacionDer.tipo, der)), 2)
            elif self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.DECIMAL:  # int / double  = double
                if self.obtenerVal(self.OperacionDer, der) == 0:
                    return Excepcion("semantico", ">operacion invalida no se puede operar entre 0<", self.fila,
                                     self.columna)
                else:
                    self.tipo = TIPO.DECIMAL
                    return round(
                        (self.obtenerVal(self.OperacionIzq.tipo, izq) / self.obtenerVal(self.OperacionDer.tipo, der)), 2)
            # DOUBLE
            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.ENTERO:  # doube / int   = double
                if self.obtenerVal(self.OperacionDer, der) == 0:
                    return Excepcion("semantico", ">operacion invalida no se puede operar entre 0<", self.fila,
                                     self.columna)
                else:
                    self.tipo = TIPO.DECIMAL
                    return round((self.obtenerVal(self.OperacionIzq.tipo, izq) / self.obtenerVal(self.OperacionDer.tipo, der)), 2)
            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.DECIMAL:  # double / double  = double
                if self.obtenerVal(self.OperacionDer, der) == 0:
                    return Excepcion("semantico", ">operacion invalida no se puede operar entre 0<", self.fila,
                                     self.columna)
                else:
                    self.tipo = TIPO.DECIMAL
                    return round(
                        (self.obtenerVal(self.OperacionIzq.tipo, izq) / self.obtenerVal(self.OperacionDer.tipo, der)), 2)

            return Exception("Semantico", "Tipo Erroneo de operacion para /.", self.fila, self.columna)


        elif self.operador == OperadorAritmetico.POT:

            if self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.ENTERO:  # int ** int     = int
                self.tipo = TIPO.ENTERO
                return self.obtenerVal(self.OperacionIzq.tipo, izq) ** self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.DECIMAL:  # int ** double  = double
                self.tipo = TIPO.DECIMAL
                return self.obtenerVal(self.OperacionIzq.tipo, izq) ** self.obtenerVal(self.OperacionDer.tipo, der)
            # DOUBLE
            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.ENTERO:  # doube ** int   = double
                self.tipo = TIPO.DECIMAL
                return self.obtenerVal(self.OperacionIzq.tipo, izq) ** self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.DECIMAL:  # double ** double  = double
                self.tipo = TIPO.DECIMAL
                return self.obtenerVal(self.OperacionIzq.tipo, izq) ** self.obtenerVal(self.OperacionDer.tipo, der)

            return Exception("Semantico", "Tipo Erroneo de operacion para **.", self.fila, self.columna)

        elif self.operador == OperadorAritmetico.MOD:

            if self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.ENTERO:  # int % int     = double
                if self.obtenerVal(self.OperacionDer, der)== 0:
                        return Excepcion("semantico", ">operacion invalida no se puede operar entre 0<",self.fila,self.columna)
                else:
                    self.tipo = TIPO.DECIMAL
                    return self.obtenerVal(self.OperacionIzq.tipo, izq) % self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.DECIMAL:  # int % double  = double
                if self.obtenerVal(self.OperacionDer, der) == 0:
                    return Excepcion("semantico", ">operacion invalida no se puede operar entre 0<", self.fila,
                                     self.columna)
                else:
                    self.tipo = TIPO.DECIMAL
                    return self.obtenerVal(self.OperacionIzq.tipo, izq) % self.obtenerVal(self.OperacionDer.tipo, der)
            # DOUBLE
            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.ENTERO:  # doube % int   = double
                if self.obtenerVal(self.OperacionDer, der) == 0:
                    return Excepcion("semantico", ">operacion invalida no se puede operar entre 0<", self.fila,
                                     self.columna)
                else:
                    self.tipo = TIPO.DECIMAL
                    return self.obtenerVal(self.OperacionIzq.tipo, izq) % self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.DECIMAL:  # double % double  = double
                if self.obtenerVal(self.OperacionDer, der) == 0:
                    return Excepcion("semantico", ">operacion invalida no se puede operar entre 0<", self.fila,
                                     self.columna)
                else:
                    self.tipo = TIPO.DECIMAL
                    return self.obtenerVal(self.OperacionIzq.tipo, izq) % self.obtenerVal(self.OperacionDer.tipo, der)

            return Exception("Semantico", "Tipo Erroneo de operacion para %.", self.fila, self.columna)

        elif self.operador == OperadorAritmetico.UMENOS: #NEGACION UNARIA
            if self.OperacionIzq.tipo == TIPO.ENTERO:
                self.tipo = TIPO.ENTERO
                return - self.obtenerVal(self.OperacionIzq.tipo, izq)
            elif self.OperacionIzq.tipo == TIPO.DECIMAL:
                self.tipo = TIPO.DECIMAL
                return - self.obtenerVal(self.OperacionIzq.tipo, izq)
            return Excepcion("Semantico", "Tipo Erroneo de operacion para - unario.", self.fila, self.columna)
        return Excepcion("Semantico", "Tipo de Operacion no Especificado.", self.fila, self.columna)

    def getNodo(self):
        nodo = NodoArbol("ARITMETICA")
        if self.OperacionDer != None:
            nodo.addHijoNode(self.OperacionIzq.getNodo())
            nodo.addHijo(str(self.operador))
            nodo.addHijoNode(self.OperacionDer.getNodo())
        else:
            nodo.addHijo(str(self.operador))
            nodo.addHijoNode(self.OperacionIzq.getNodo())
        return nodo

    def obtenerVal(self, tipo, val):
        if tipo == TIPO.ENTERO:
            return int(val)
        elif tipo == TIPO.DECIMAL:
            return float(val)
        elif tipo == TIPO.BOOLEANO:
            return bool(val)
        return str(val)
        