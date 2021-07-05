from tkinter import ttk, Tk, Label, Menu, Button, Entry, StringVar, Scrollbar, Frame, Text, scrolledtext
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import webbrowser as wb

class Ventana():

    def __init__(self):
        self.text_global = ""
        self.filename = ""

        self.root_window = Tk()

        self.scrollbar = Scrollbar(self.root_window)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        self.root_window.geometry("1350x670+0+0")
        self.root_window.title("PROYECTO COMPI 1 ")
        self.root_window.configure(bg='black')

        # ------------------------------------ BARRA MENU ------------------------------------
        self.barra_menu = Menu(self.root_window)

        # ------------------------------------ CARGAR ARCHIVO ------------------------------------
        self.open_file = Menu(self.barra_menu)
        self.open_file.add_command(label="Abrir Archivo", command=lambda: self.abrir_archivo())
        self.open_file.add_command(label="Crear Archivo", command=lambda: self.crear_archivo())

        self.open_file.add_command(label="Guardar", command=lambda: self.guardar())
        self.open_file.add_command(label="Guardar Como", command=lambda: self.guardar_como())

        self.barra_menu.add_cascade(label="Archivo", menu=self.open_file)

        self.herramienta = Menu(self.barra_menu)
        self.herramienta.add_command(label="Interpretar", command=self.interpretar)
        self.herramienta.add_command(label="Debugger")

        self.barra_menu.add_cascade(label="Herramientas", menu=self.herramienta)

        self.reporte = Menu(self.barra_menu)
        self.reporte.add_command(label="Reporte de Errores",command = lambda:self.reporte_error())
        self.reporte.add_command(label="Generar Árbol AST (Árbol de Análisis Sintáctico)",command = lambda:self.reporte_ast())
        self.reporte.add_command(label="Reporte de Tabla de Símbolos")

        self.barra_menu.add_cascade(label="Reporte", menu=self.reporte)

        # ------------------------------------ AYUDA ------------------------------------
        self.ayuda = Menu(self.barra_menu)
        self.ayuda.add_command(label="opcion 1")

        self.barra_menu.add_cascade(label="Ayuda", menu=self.ayuda)

        # ----------------------------------- CONSOLA Y PARTE DE CODIGO ---------------------------------------

        self.editor = Label(self.root_window, text="Editor",bg = "white")
        self.editor.pack()
        self.editor.place(x=20, y=1)

        self.label_position = Label(self.root_window)
        self.label_position.pack()
        self.label_position.place(x=50, y=1)

        self.scroll = ScrollText(self.root_window)

        self.scroll.pack()
        self.scroll.place(x=50, y=25)


        self.scroll_consola = scrolledtext.ScrolledText(self.root_window, height=20, width=70,bg ="gray")  # consola
        self.scroll_consola.insert(tk.INSERT, "creditos a Jose Puac Auxiliar del curso por su guia en la realización de este proyecto")
        self.scroll_consola.configure(state='disabled')
        self.scroll_consola.pack()
        self.scroll_consola.place(x=700, y=25)

        # -----------------------  PARTE DE REPORTES Y TABLA DE SIMBOLOS ---------------------------

        self.root_tab_control = ttk.Notebook(self.root_window, height=210, width=1250)  # Creando la raiz de las petañas
        """
        """


        self.root_tab2 = ttk.Frame(self.root_tab_control)  # Creeando otra pestaña
        self.root_tab_control.add(self.root_tab2, text="Reporte de Errores")
        self.root_tab1 = ttk.Frame(self.root_tab_control)  # Creando la pestaña
        self.root_tab_control.add(self.root_tab1, text="Tabla de Simbolos")

        self.lb1 = Label(self.root_tab1, text="Tabla de Simbolos")
        self.lb1.pack()
        self.lb2 = Label(self.root_tab2, text="Tabla de Reportes")
        self.lb2.pack()

        self.root_tab_control.pack(expand=1, fill="both")
        self.root_tab_control.place(x=50, y=400)

        # TABLA SIMBOLOS
        """
        
       
        self.table = ttk.Treeview(self.root_tab1)
        self.table['columns'] = ('NO', 'ID', 'TIPO', 'UBICACION', 'VALOR', 'AMBITO', 'REFERENCIAS')
        self.table.column('#0', width=0, stretch=NO)
        self.table.column('NO', anchor=CENTER, width=3)
        self.table.column('ID', anchor=CENTER)
        self.table.column('TIPO', anchor=CENTER)
        self.table.column('UBICACION', anchor=CENTER)
        self.table.column('VALOR', anchor=CENTER)
        self.table.column('AMBITO', anchor=CENTER)
        self.table.column('REFERENCIAS', anchor=CENTER)

        self.table.heading('#0', text='', anchor=CENTER)
        self.table.heading('NO', text='#', anchor=CENTER)
        self.table.heading('ID', text='Id', anchor=CENTER)
        self.table.heading('TIPO', text='Tipo', anchor=CENTER)
        self.table.heading('UBICACION', text='Dimension', anchor=CENTER)
        self.table.heading('VALOR', text='Valor', anchor=CENTER)
        self.table.heading('AMBITO', text='Ambito', anchor=CENTER)
        self.table.heading('REFERENCIAS', text='Referencias', anchor=CENTER)
        
        i = 0
        while i < 10:
            self.table.insert(parent='', index=i, iid=i, text='', values=(f'{i+1}', f'id{i}',f'tipo{i}',f'dime{i}',f'val{i}',f'amb{i}',f'refe{i}'))
            i += 1
        """



        # TABLA DE ERRORES
        self.table_error = ttk.Treeview(self.root_tab2)
        self.table_error['columns'] = ('NO', 'TIPO', 'DESCRIPCION', 'LINEA', 'COLUMNA')
        self.table_error.column('#0', width=0, stretch=NO)
        self.table_error.column('NO', anchor=CENTER, width=3)
        self.table_error.column('TIPO', anchor=CENTER)
        self.table_error.column('DESCRIPCION', anchor=CENTER)
        self.table_error.column('LINEA', anchor=CENTER)
        self.table_error.column('COLUMNA', anchor=CENTER)

        self.table_error.heading('#0', text='', anchor=CENTER)
        self.table_error.heading('NO', text='#', anchor=CENTER)
        self.table_error.heading('TIPO', text='Tipo', anchor=CENTER)
        self.table_error.heading('DESCRIPCION', text='Descripcion', anchor=CENTER)
        self.table_error.heading('LINEA', text='LINEA', anchor=CENTER)
        self.table_error.heading('COLUMNA', text='COLUMNA', anchor=CENTER)
        """
        i = 0
        while i < 10:
            self.table_error.insert(parent='', index=i, iid=i, text='', values=(f'{i+1}',f'tipo{i}',f'des{i}',f'linea{i}',f'colu{i}'))
            i += 1
        """
        self.table_error.pack()
        # ----------------------------------- POSICION DEL MOUSE ----------------------------------

        self.scroll.text.bind("<Button-1>", self.get_posicion_mouse)
        self.scroll.text.bind("<Button-2>", self.get_posicion_mouse)
        self.scroll.text.bind("<Button-3>", self.get_posicion_mouse)

        # ------------------------------------ FIN DE TK -------------------------------------------

        self.root_window.config(menu=self.barra_menu)
        self.root_window.mainloop()



    ########################## POSICION ##########################

    def get_posicion_mouse(self, *args, **kwargs):
        position = self.scroll.text.index(INSERT)
        self.label_position.destroy()
        self.label_position = Label(self.root_window, text=f"{position}")
        self.label_position.pack()
        self.label_position.place(x=50, y=1)

    # -------------------------------------------------------- ARCHIVO ------------------------------------------------------

    def crear_archivo(self):
        print('\n---------------')
        result = self.scroll.text.get(1.0, tk.END + "-1c")
        print(result)
        print('---------------')

        self.filename = filedialog.asksaveasfilename(initialdir="/", title="Guardar como",
                                                     filetypes=(("txt files", "*.jpr"), ("todos los archivos", "*.*")))

        if self.filname != '':
            archi1 = open(self.filename, "w")
            archi1.write(result)
            archi1.close()

    def abrir_archivo(self):
        try:
            ruta = ""
            self.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                       filetypes=(("JPR files", "*.jpr"), ("all files", "*.*")))
            ruta = self.filename
            if ruta != "":
                try:
                    archivo = open(ruta, "r")
                    texto = archivo.read()
                    self.scroll.text.insert(tk.INSERT, texto)
                    archivo.close()
                except (FileNotFoundError):
                    print("Error")
            else:
                return None

        except IndexError as e:
            print(e)

    def guardar(self):

        if self.filename != "":
            result = self.scroll.text.get(1.0, tk.END + "-1c")
            archivo = open(self.filename, "w")
            archivo.write(result)
            archivo.close()
        else:
            messagebox.showinfo(message="No hay Documento abierto", title="Gaurdar")

    def guardar_como(self):

        self.filename = filedialog.asksaveasfilename(initialdir="/", title="Seleccione el Archivo",
                                                     defaultextension=".jpr",
                                                     filetypes=(("jpr files", "*.jpr"), ("all files", "*.*")))
        result = self.scroll.text.get(1.0, tk.END + "-1c")

        if self.filename != '':
            archi1 = open(self.filename, "w")
            archi1.write(result)
            archi1.close()

    # -------------------------------------------------------- HERRAMIENTAS ------------------------------------------------------
    def interpretar(self):

        import grammar as prueba

        result = self.scroll.text.get(1.0, tk.END + "-1c")


        AST = prueba.interprete_perron(result, self.scroll_consola)
        asd =AST.get_consola()
        self.scroll_consola.delete("1.0", "end")
        self.scroll_consola = scrolledtext.ScrolledText(self.root_window, height=20, width=70, bg="gray")  # consola
        self.scroll_consola.insert(tk.INSERT, asd)
        self.scroll_consola.configure(state='disabled')
        self.scroll_consola.pack()
        self.scroll_consola.place(x=700, y=25)


        for d in self.table_error.get_children():  # Esto sirve para resetear la tabla de errores.
            self.table_error.delete(d)

        i = 0
        for pedo in AST.get_excepcion():
            self.table_error.insert(parent='', index=i, iid=i, text='', values=(
                f'{i + 1}', f'{pedo.tipo}', f'{pedo.descripcion}', f'{pedo.fila}', f'{pedo.columna}'))
            print(pedo)
            i += 1


    def debugger(self):
        pass



    # -------------------------------------------------------- REPORTE ------------------------------------------------------

    def reporte_error(self):
        print("entro reporte error")
        from grammar import interprete_perron
        ast = interprete_perron(self.scroll.text.get(1.0, tk.END + "-1c"))
        contador = 0


        for error in ast.getExcepciones():
            contador = contador +1
            tipo = error.tipo
            descripcion = error.descripcion
            fila = error.fila
            columna = error.columna
            self.table_error.insert(parent='',index='end',iid=contador,text = "Parent",
                                    values=(f"{contador}",f"{tipo}",f"{descripcion}",f"{fila}",f"{columna}"))



    def reporte_ast(self):
        print("entro reporte ast")
        try:
            # root = Tk()
            ruta = ""
            filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                  filetypes=(("TXT files", "*.pdf"), ("all files", "*.*")))
            ruta = filename
            if ruta != "":
                wb.open_new(ruta)
                return ruta
            else:

                return None

        except IndexError as e:
            print(e)

    def reporte_tabla_simbolo(self):
        pass


class ScrollText(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        # bg -> color de fondo --- foreground -> color al texto --- selectbrackgroud -> color a lo que seleccione --- inserbackgroud -> color al puntero
        self.text = tk.Text(self, bg='#FFFFFF', foreground="#000000", selectbackground="#C8C8C8",
                            insertbackground='#000000', height=20, width=70)

        self.scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL, command=self.text.yview)
        self.text.configure(yscrollcommand=self.scrollbar.set)

        self.numero_lineas = TextoLinea(self, width=35, bg='#D5D5D5')
        self.numero_lineas.attach(self.text)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.numero_lineas.pack(side=tk.LEFT, fill=tk.Y, padx=(5, 0))
        self.text.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.text.bind("<Key>", self.onPressDelay)
        self.text.bind("<Button-1>", self.numero_lineas.redraw)
        self.scrollbar.bind("<Button-1>", self.onScrollPress)
        self.text.bind("<MouseWheel>", self.onPressDelay)

    def onScrollPress(self, *args):
        self.scrollbar.bind("<B1-Motion>", self.numero_lineas.redraw)

    def onScrollRelease(self, *args):
        self.scrollbar.unbind("<B1-Motion>", self.numero_lineas.redraw)

    def onPressDelay(self, *args):
        self.after(2, self.numero_lineas.redraw)

    def get(self, *args, **kwargs):
        return self.text.get(*args, **kwargs)

    def insert(self, *args, **kwargs):
        return self.text.insert(*args, **kwargs)

    def delete(self, *args, **kwargs):
        return self.text.delete(*args, **kwargs)

    def index(self, *args, **kwargs):
        return self.text.index(*args, **kwargs)

    def redraw(self):
        self.numero_lineas.redraw()


class TextoLinea(tk.Canvas):
    def __init__(self, *args, **kwargs):
        tk.Canvas.__init__(self, *args, **kwargs, highlightthickness=0)
        self.textwidget = None

    def attach(self, text_widget):
        self.textwidget = text_widget

    def redraw(self, *args):
        self.delete("all")
        i = self.textwidget.index("@1,0")
        while True:
            dline = self.textwidget.dlineinfo(i)
            if dline is None: break
            y = dline[1]
            linenum = str(i).split(".")[0]
            self.create_text(2, y, anchor="nw", text=linenum, fill="#606366")
            i = self.textwidget.index("%s+1line" % i)

