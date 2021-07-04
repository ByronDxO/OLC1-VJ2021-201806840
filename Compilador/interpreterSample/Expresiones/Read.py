from Abstract import Instruccion
from TS.Tipo import TIPO
from Abstract.NodoArbol import NodoArbol
from tkinter import *
from tkinter import Tk, simpledialog
import tkinter as tk
import sys

class Read(Instruccion):
    def __init__(self,fila,columna):
        self.fila = fila
        self.columna = columna
        self.tipo = TIPO.CADENA
        self.lectura = None

    def interpretar(self,tree , table):
        print(tree.get_consola())
        tree.showConsolaSalida(tree.get_consola())
        self.lectura = simpledialog.askstring("Read()","Ingresa el valor ", parent = tree.getConsolaSalida())
        return self.lectura

    def getNodo(self):
        nodo = NodoArbol("READ")
        nodo.addHijo(str(self.lectura))
        return nodo
