from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion
from TS.TablaSimbolos import TablaSimbolos
from Instrucciones.Break import Break
from Abstract.NodoArbol import NodoArbol
from Instrucciones.Return import Return
from Instrucciones.Continue import Continue

class Main(Instruccion):
    def __init__(self, instrucciones, fila, columna):
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna
    
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
            if isinstance(value, Return):
                err = Excepcion("Semantico", "Sentencia Return fuera de ciclo", instruccion.fila, instruccion.columna)
                tree.get_excepcion().append(err)
                tree.update_consola(err.toString())
            if isinstance(value, Continue):
                err = Excepcion("Semantico", "Sentencia Continue fuera de ciclo", instruccion.fila, instruccion.columna)
                tree.get_excepcion().append(err)
                tree.update_consola(err.toString())

    def getNodo(self):
        nodo = NodoArbol("MAIN")

        instrucciones = NodoArbol("INSTRUCCIONES")
        for instr in self.instrucciones:
            instrucciones.addHijoNode(instr.getNodo())
        nodo.addHijoNode(instrucciones)
        return nodo