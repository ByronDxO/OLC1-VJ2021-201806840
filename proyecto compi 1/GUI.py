import tkinter
import os
from tkinter import ttk
from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter import filedialog
class GUI:
    ventana = tkinter.Tk()
    def  interfaz(self):

        self.ventana.title("Proyecto Compi 1 Vacas ")
        self.ventana.geometry("1425x1200")
        Titulo = tkinter.Label(self.ventana, text ="JRC EDITOR", bg = "green", width = 50 , height = 2 )
        Contador = tkinter.Label(self.ventana, text ="0",width = 50 , height = 2)
        Contador_columnas_linea = tkinter.Label(self.ventana, text ="[1,0]",width = 50 , height = 2)
        CajaTexto_entrada =  tkinter.scrolledtext.ScrolledText(self.ventana,background = "cyan")
        CajaTexto_salida = tkinter.scrolledtext.ScrolledText(self.ventana,background = "grey")
        label_simbolos = tkinter.Label(self.ventana, text ="Tabla de Simbolos ",width = 50 , height = 2)
        Reporte_Errores = tkinter.Label(self.ventana, text ="Reporte Errores ",width = 50 , height = 2)
        """
        var = tkinter.OptionMenu(ventana)
        var.set("Archivo")
        first_menu = ['Crear Archivo','Abrir Archivo','Guardar','Guardar Como']
        opcion = tkinter.OptionMenu(ventana,var,*first_menu)
        opcion.config(width = 20 )
        opcion.grid(row=0, column=0)
        """
        #Scrollbar
        scrollbar = tkinter.Scrollbar(self.ventana)



        ### Menus ##
        barramenu = Menu(self.ventana)
        mnuArchivo = Menu(barramenu)
        mnuArchivo.add_command(label = "Crear Archivo")
        mnuArchivo.add_command(label="Abrira Archivo")
        mnuArchivo.add_command(label="Guardar")
        mnuArchivo.add_command(label="Guardar Como")
        mnuArchivo.add_command(label = "Salir",command = self.salir)
        barramenu.add_cascade(label = "Archivo", menu=mnuArchivo)
        self.ventana.config(menu = barramenu)
        ##menu herramientas ##
        mnu_herramientas = Menu(barramenu)
        mnu_herramientas.add_command(label = "Ejecutar")
        mnu_herramientas.add_command(label = "Debugger")
        barramenu.add_cascade(label="Herramientas ", menu = mnu_herramientas)
        ###menu Reportes ##
        mnu_Reportes = Menu(barramenu)
        mnu_Reportes.add_command(label = "Reporte de Arbol")
        barramenu.add_cascade(label = "Reportes",menu = mnu_Reportes)
        #Tablas
        #tabla Error
        columnas = ("#","Tipo de Error","Descripcion","Linea","Columna")
        tabla_errores = ttk.Treeview(self.ventana,columns=[f"#{n}" for n in range (1, 5)])
        tabla_errores.heading("#0",text= "#")
        tabla_errores.heading("#1", text="Tipo_de_Error")
        tabla_errores.heading("#2", text="Descripcion")
        tabla_errores.heading("#3", text="Linea")
        tabla_errores.heading("#4", text="Columna")
        tabla_errores.grid(row = 7 , column = 0,columnspan = 5)
        #Tabla de Simbolos
        Tabla_simbolos = ttk.Treeview(self.ventana,columns=[f"#{n}" for n in range (1, 7)])
        Tabla_simbolos.heading("#0",text = "Identificador")
        Tabla_simbolos.heading("#1", text="Tipo/Función/Método")
        Tabla_simbolos.heading("#2", text="Tipo")
        Tabla_simbolos.heading("#3", text="Entorno")
        Tabla_simbolos.heading("#4", text="Valor")
        Tabla_simbolos.heading("#5", text="Linea")
        Tabla_simbolos.heading("#6", text="Columna")
        Tabla_simbolos.grid(row = 9 , column = 0 , columnspan = 7)
        ###grid##
        Titulo.grid(row =1 , column = 0  )
        Contador.grid(row = 1 , column = 1)
        Contador_columnas_linea.grid(row = 2 , column = 0)
        CajaTexto_entrada.place(x=50 , y = 50)
        CajaTexto_entrada.grid(row = 3 , column = 0)
        CajaTexto_salida.place(x=50 , y = 50)
        CajaTexto_salida.grid(row = 3 , column = 1)
        label_simbolos.grid(row =8 , column = 0)
        Reporte_Errores.grid(row = 6,column=0)

        self.ventana.mainloop()

    def salir(self):  # SALIR DEL PROGRAMA
        value = messagebox.askokcancel("Salir", "Está seguro que desea salir?")
        if value:
            self.ventana.destroy()

    def cerrarDoc(self):  # CERRAR UN DOCUMENTO
        value = messagebox.askretrycancel("Reintentar", "No es posible cerrar el documento.")
        if value == False:
            self.ventana.destroy()

    archivo = ""  # PATH DEL ARCHIVO EN MEMORIA
"""
    def nuevo(self):  # NUEVO ARCHIVO
        global archivo
        editor.delete(1.0, END)
        archivo = ""

    def abrir(self):  # ABRIR ARCHIVO
        global archivo
        archivo = filedialog.askopenfilename(title="Abrir Archivo", initialdir="C:/")

        entrada = open(archivo)
        content = entrada.read()

        editor.delete(1.0, END)
        for s in recorrerInput(content):
            editor.insert(INSERT, s[1], s[0])
        entrada.close()
        lineas()

    def guardarArchivo(self):  # GUARDAR
        global archivo
        if archivo == "":
            guardarComo()
        else:
            guardarc = open(archivo, "w")
            guardarc.write(editor.get(1.0, END))
            guardarc.close()

    def guardarComo(self):  # GUARDAR COMO
        global archivo
        guardar = filedialog.asksaveasfilename(title="Guardar Archivo", initialdir="C:/")
        fguardar = open(guardar, "w+")
        fguardar.write(editor.get(1.0, END))
        fguardar.close()
        archivo = guardar

    def openPDF(self):  # ABRIRI UN PDF
        dirname = os.path.dirname(__file__)
        direcc = os.path.join(dirname, 'ast.pdf')
        os.startfile(direcc)

    def lineas(self,*args):  # ACTUALIZAR LINEAS
        lines.delete("all")

        cont = editor.index("@1,0")
        while True:
            dline = editor.dlineinfo(cont)
            if dline is None:
                break
            y = dline[1]
            strline = str(cont).split(".")[0]
            lines.create_text(2, y, anchor="nw", text=strline, font=("Arial", 15))
            cont = editor.index("%s+1line" % cont)

    def posicion(event):  # ACTUALIZAR POSICION
        pos.config(text="[" + str(editor.index(INSERT)).replace(".", ",") + "]")
"""



