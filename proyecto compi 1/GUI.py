import tkinter
from tkinter import *
class GUI:
    pass
    def  interfaz(self):
        ventana = tkinter.Tk()
        ventana.geometry("1300x800")
        Titulo = tkinter.Label(ventana, text ="JRC EDITOR", bg = "green", width = 50 , height = 5 )
        Contador = tkinter.Label(ventana, text ="0",width = 50 , height = 5)
        Contador_columnas_linea = tkinter.Label(ventana, text ="[1,0]",width = 50 , height = 5)
        CajaTexto_entrada =  tkinter.Text(ventana)
        CajaTexto_salida = tkinter.Text(ventana)
        Tabla_simbolos = tkinter.Label(ventana, text ="Tabla de Simbolos ",width = 50 , height = 5)
        Reporte_Errores = tkinter.Label(ventana, text ="Reporte Errores ",width = 50 , height = 5)
        Titulo.grid(row =0 , column = 0  )
        Contador.grid(row = 0 , column = 2)
        Contador_columnas_linea.grid(row = 1 , column = 0)
        CajaTexto_entrada.place(x=50 , y = 50)
        CajaTexto_entrada.grid(row = 2 , column = 0)
        CajaTexto_salida.place(x=50 , y = 50)
        CajaTexto_salida.grid(row = 2 , column = 1)
        Tabla_simbolos.grid(row =5 , column = 0)
        Reporte_Errores.grid(row = 5,column=1)

        ventana.mainloop()





a = GUI()
a.interfaz()

