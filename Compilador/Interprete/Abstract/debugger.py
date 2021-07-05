import time


class debugger:
    debuggeando = False
    interpretando = False
    linea_actual = 1
    editor = None

    @staticmethod
    def configurar_editor(text_widget):
        debugger.editor = text_widget

    @staticmethod
    def arrancar():
        debugger.debuggeando = True
        debugger.interpretando = False
        debugger.linea_actual = 1

    @staticmethod
    def detener():
        debugger.debuggeando = False
        debugger.interpretando = False
        debugger.linea_actual = 1
        debugger.editor.tag_remove('highlight', '1.0', 'end')

    @staticmethod
    def pausar(linea):
        if debugger.debuggeando:
            debugger.interpretando = False
            debugger.linea_actual = linea
            debugger.editor.yview_pickplace(str(linea) + '.0')
            debugger.editor.tag_remove('highlight', '1.0', 'end')
            debugger.editor.tag_add('highlight', str(linea) + '.0', str(linea) + '.end')
            debugger.editor.tag_config('highlight', background='white', foreground='black')
            while not debugger.interpretando:
                time.sleep(0.01)
            debugger.interpretando = False

    @staticmethod
    def continuar():
        debugger.interpretando = True