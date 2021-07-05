from Interprete.Abstract.Instruccion import Instruccion
from Interprete.TS.Tipo import Tipo
from Interprete.Abstract.NodoAST import NodoAST


from tkinter import *
from tkinter import Tk, simpledialog
import tkinter as tk
import sys

class Read(Instruccion):
    def __init__(self, fila, columna):
        self.fila = fila
        self.columna = columna
        self.tipo = Tipo.CADENA
        self.lectura = None

    def interpretar(self, tree, table):
        print("iteracion")
        print(tree.get_consola())
        
        tree.showConsolaSalida(tree.get_consola())
        self.lectura = simpledialog.askstring("Read()", "Ingrese el Valor:", parent=tree.getConsolaSalida())
        print(self.lectura)
        return self.lectura

    def getNodo(self):
        nodo = NodoAST("READ")
        nodo.agregarHijo(str(self.lectura))
        return nodo