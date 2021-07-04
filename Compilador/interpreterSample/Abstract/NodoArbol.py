class NodoArbol():
    def __init__(self,value):
        self.hijos = []
        self.value = value

    def setHijo(self,hijos):
        self.hijos = hijos
    def addHijo(self,valueChildren):
        self.hijos.append(NodoArbol(valueChildren))
    def addHijos(self,hijos):
        for hijo in hijos:
            self.hijos.append(hijo)
    def addHijoNode(self,hijo):
        self.hijos.append(hijo)
    def addFirstHijo(self,valueHijo):
        self.hijos.insert(0,NodoArbol(valueHijo))
    def getValue(self):
        return str(self.value)
    def setValor(self,value):
        self.value = value
    def getHijos(self):
        return self.hijos