from Instrucciones.Return import Return
from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion
from TS.Tipo import TIPO
from TS.TablaSimbolos import TablaSimbolos
from Instrucciones.Break import Break
from Instrucciones.Continue import Continue
from Abstract.NodoArbol import NodoArbol
class For(Instruccion):
    def __init__(self,variable,condicion,actualizacion,instrucciones,fila,columna):
        self.variable = variable
        self.condicion = condicion
        self.actualizacion= actualizacion
        self.intrucciones= instrucciones
        self.fila = fila
        self.columna = columna
    def interpretar(self, tree, table):
        new_tabla =  TablaSimbolos(table)
        declaracion = self.variable.interpretar(tree,new_tabla)
        if isinstance(declaracion, Excepcion):return declaracion
        while True:
            condicion = self.condicion.interpretar(tree,new_tabla)
            if isinstance(condicion,Excepcion):return condicion
            if self.condicion.tipo == TIPO.BOOLEANO:
                if bool(condicion) == True:
                 new2_tabla = TablaSimbolos(new_tabla)
                 for instrucciones in self.intrucciones:
                     result = instrucciones.interpretar(tree,new2_tabla)
                     if isinstance(result,Excepcion):
                         tree.getExcepciones().append(result)
                         tree.updateConsola(result.toString())
                     if isinstance(result,Break):return None
                     if isinstance(result, Return): return result
                     if isinstance(result, Continue): break
                 update = self.actualizacion.interpretar(tree,new2_tabla)
                 if isinstance(update,Excepcion):return update
            else:
                break
        else:
            return Excepcion("semantico","tipo de dato no aceptable para la instruccion for",self.fila,self.columna)

    def getNodo(self):
        nodo = NodoArbol("FOR")
        nodo.addHijoNode(self.variable.getNodo())
        nodo.addHijoNode(self.condicion.getNodo())
        instrucciones = NodoArbol("INSTRUCCIONES")
        for instruccion in self.instrucciones:
            instrucciones.addHijoNode(instruccion.getNodo())
        nodo.addHijoNode(instrucciones)

        nodo.addHijoNode(self.actualizacion.getNodo())
        return nodo