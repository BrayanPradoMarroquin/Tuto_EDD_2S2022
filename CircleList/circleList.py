from Nodo import Nodo
import os

class ListaCircular:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def vacio(self):
        return self.primero == None

    def agregar(self, dato):
        Nuevo = Nodo(dato)

        if self.vacio():
            self.primero = self.ultimo = Nuevo
            self.ultimo.siguiente = self.primero
        else:
            Nuevo.siguiente = self.primero
            self.primero = Nuevo
            self.ultimo.siguiente = self.primero

    def recorrer(self):
        aux = self.primero
        while(aux.siguiente!=self.primero):
            print(aux.dato)
            aux = aux.siguiente
        print(aux.dato)

    def graficar(self):
        aux = self.primero
        cont = 0
        cadena = ""
        file = open('ListaCircular.dot', 'w')
        cadena = cadena + "digraph G {\n"
        while(aux.siguiente!=self.primero):
            cadena = cadena + "Node"+str(cont)+"[label=\""+str(aux.dato)+"\"];\n"
            if(aux!=self.primero):
                cadena = cadena + "Node"+str(cont-1)+" -> Node"+str(cont)+";\n"
            cont+=1
            aux = aux.siguiente
        cadena = cadena + "Node"+str(cont)+"[label=\""+str(aux.dato)+"\"];\n"
        cadena = cadena + "Node"+str(cont-1)+" -> Node"+str(cont)+";\n"
        cadena = cadena + "Node"+str(cont)+" -> Node"+str(0)+";\n"
        cadena = cadena + "}"
        file.write(cadena)
        file.close()
        os.system('dot -Tpng ListaCircular.dot -o ListaCircular.png')