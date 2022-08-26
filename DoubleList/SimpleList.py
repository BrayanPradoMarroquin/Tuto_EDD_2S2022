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
            self.cabecera.anterior = nuevo
            self.ultimo = self.cabecera
            self.cabecera = nuevo
    
    def recorrer(self):
        aux = self.cabecera
        while(aux!=None):
            print(aux.Nombre," -> ",aux.carnet)
            aux = aux.siguiente

    def eliminar(self, carnet):
        aux1 = self.cabecera
        while(aux1!=None):
            if(aux1.carnet == carnet):
                if(aux1 == self.cabecera):
                    aux1 = aux1.siguiente
                    aux1.anterior = None
                    ##self.cabecera = self.cabecera.siguiente
                    break;
                elif(aux1.siguiente == None):
                    aux1.anterior.siguiente = None
                    aux1.anterior = None
                else:
                    aux1.anterior.siguiente = aux1.siguiente
                    aux1.siguiente.anterior = aux1.anterior
                    aux1.anterior = None
                    aux1.siguiente = None
                    break;
            else:
                aux1 = aux1.siguiente

    def buscar(self, carnet):
        aux = self.cabecera
        while(aux!=None):
            if(aux.carnet!=carnet):
                aux = aux.siguiente
            else:
                print(aux.Nombre," ",aux.carnet)
                break;
    
    def graficar(self):
        aux = self.cabecera
        contador = 0
        cadena = ""
        file = open("grafica2.dot", "w")
        cadena = cadena + "digraph G{ \n"
        while(aux!=None):
            cadena = cadena + "Node"+str(contador)+"[label=\""+aux.Nombre+"\"];\n"
            if(aux!=self.cabecera):
                cadena = cadena + "Node"+str(contador-1)+" -> Node"+str(contador)+";\n"
                cadena = cadena + "Node"+str(contador)+" -> Node"+str(contador-1)+";\n"
            aux = aux.siguiente
            contador = contador + 1
        cadena = cadena + "}"
        file.write(cadena)
        file.close()
        os.system('dot -Tpng grafica2.dot -o grafica2.png')
