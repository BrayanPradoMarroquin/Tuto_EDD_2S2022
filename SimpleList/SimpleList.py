import os
from Nodo import Node

class SimpleList:
    def __init__(self):
        self.cabecera = None
        self.ultimo = None

    def vacio(self):
        if ((self.cabecera == None) and (self.ultimo == None)):
            return True
        else:
            return False
    
    def agregar(self, Nombre, carnet, edad, carrera):
        nuevo = Node(Nombre, carnet, edad, carrera)

        if self.vacio():
            self.cabecera = nuevo
            self.ultimo = nuevo
        else:
            nuevo.siguiente = self.cabecera
            self.cabecera = nuevo
    
    def recorrer(self):
        aux = self.cabecera
        while(aux!=None):
            print(aux.Nombre," -> ",aux.carnet)
            aux = aux.siguiente

    def eliminar(self, carnet):
        aux1 = self.cabecera
        aux2 = None
        while(aux1!=None):
            if(aux1.carnet == carnet):
                if(aux1 == self.cabecera):
                    aux1 = aux1.siguiente
                    ##self.cabecera = self.cabecera.siguiente
                    break;
                elif(aux1.siguiente == None):
                    aux2.siguiente = None
                else:
                    aux2.siguiente = aux1.siguiente
                    aux1.siguiente = None
                    break;
            else:
                aux2 = aux1
                aux1 = aux1.siguiente

    ##Agregar los Nodos (informacion) a la lista secundaria
    def buscar(self, carnet):
    ##def buscar(self, carnet, x, y, informacion):
        aux = self.cabecera
        while(aux!=None):
            if(aux.carnet!=carnet):
                aux = aux.siguiente
            else:
                print(aux.Nombre," ",aux.carnet)
                ##aux.data.agregar(x, y, informacion)
                break;
    

    def graficar(self):
        aux = self.cabecera
        contador = 0
        cadena = ""
        file = open("grafica.dot", "w")
        cadena = cadena + "digraph G{ \n"
        while(aux!=None):
            cadena = cadena + "Node"+str(contador)+"[label=\""+aux.Nombre+"\"];\n"
            if(aux!=self.cabecera):
                cadena = cadena + "Node"+str(contador-1)+" -> Node"+str(contador)+";\n"
            aux = aux.siguiente
            contador = contador + 1
        cadena = cadena + "}"
        file.write(cadena)
        file.close()
        os.system('dot -Tpng grafica.dot -o grafica.png')
