class Excepcion:
    def __init__(self, tipo, descripcion, fila, columna):
        self.tipo = tipo
        self.descripcion = descripcion
        self.fila = fila
        self.columna = columna

    def toString(self):
        return self.tipo + " - " + self.descripcion + " [" + str(self.fila) + "," + str(self.columna) + "]"

    def getTipo(self):
        return self.tipo
    def getDescripcion(self):
        return self.descripcion
    def getFila(self):
        return self.fila
    def getColumna(self):
        return self.columna