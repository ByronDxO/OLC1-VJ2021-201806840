from TS.Tipo import TIPO
from Instrucciones.Return import Return
from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion
from TS.TablaSimbolos import TablaSimbolos
from Instrucciones.Break import Break
from Instrucciones.Continue import Continue
from Abstract.NodoArbol import  NodoArbol
class Funcion(Instruccion):
    def __init__(self, nombre, parametros, instrucciones, fila, columna):
        self.nombre = nombre.lower()
        self.parametros = parametros
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna
        self.tipo = TIPO.NULO
    
    def interpretar(self, tree, table):
        nuevaTabla = TablaSimbolos(table) 
        for instruccion in self.instrucciones:      # REALIZAR LAS ACCIONES
            value = instruccion.interpretar(tree,nuevaTabla)
            if isinstance(value, Excepcion) :
                tree.getExcepciones().append(value)
                tree.updateConsola(value.toString())
            if isinstance(value, Break): 
                err = Excepcion("Semantico", "Sentencia BREAK fuera de ciclo", instruccion.fila, instruccion.columna)
                tree.getExcepciones().append(err)
                tree.updateConsola(err.toString())
            if isinstance(value, Continue):
                err = Exception("Semantico", "Sentencia Continue fuera de ciclo", instruccion.fila, instruccion.columna)
                tree.get_excepcion().append(err)
                tree.update_consola(err.toString())
            if isinstance(value, Return):
                self.tipo = value.tipo
                return value.result
            
        return None

    def getNodo(self):
        nodo = NodoArbol("FUNCION")

        nodo.addHijo(str(self.nombre))

        parametros = NodoArbol("PARAMETROS")
        for param in self.parametros:
            parametro = NodoArbol("PARAMETRO")
            parametro.addHijo(param["tipoDato"])
            parametro.addHijo(param["identificador"])
            parametros.addHijoNode(parametro)
        nodo.addHijoNode(parametros)

        instrucciones = NodoArbol("INSTRUCCIONES")
        for instruccion in self.instrucciones:
            instrucciones.addHijo(instruccion.getNodo())
        nodo.addHijoNode(instrucciones)

        return nodo