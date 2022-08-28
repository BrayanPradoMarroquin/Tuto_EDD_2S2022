import xml.etree.ElementTree as ET
#from tkinter import *
#from tkinter.filedialog import askopenfilename
from SimpleList import SimpleList

newList = SimpleList()
#root = Tk()
#root.withdraw()
#root.update()

dato = '''
        <matrices>
            <matriz nombre="Ejemplo" n="3" m="3">
                <dato x="1" y="1">1</dato>
                <dato x="1" y="2">2</dato>
                <dato x="1" y="3">3</dato>
                <dato x="2" y="1">0</dato>
                <dato x="2" y="2">5</dato>
                <dato x="2" y="3">6</dato>
                <dato x="3" y="1">0</dato>
                <dato x="3" y="2">0</dato>
                <dato x="3" y="3">9</dato>
            </matriz>
            <matriz nombre="matriz_ejemplo" n="2" m="2">
                <dato x="1" y="1">0</dato>
                <dato x="1" y="2">3</dato>
                <dato x="2" y="1">0</dato>
                <dato x="2" y="2">1</dato>
            </matriz>
        </matrices>
        '''

def generar():
    pathString = input()
    tree = ET.parse(pathString)
    raiz = tree.getroot()
    return raiz

def guardar(raiz):
    for elem in raiz:
        newList.agregar(elem.get('nombre'), elem.get('n'), elem.get('m'), "")
        for data in elem:
            #newList.buscar(elem.get('nombre'), data.get('x'), " ",data.get('y'), " ", data.text)
            print(data.get('x'), " ",data.get('y'), " ", data.text)

guardar(generar())
newList.recorrer()
##newList.agregar("Byron", "201805390", "20", "Sistemas")
##newList.agregar("Ana", "201805391", "22", "Sistemas")
##newList.agregar("Luis", "201905390", "20", "Sistemas")
##newList.agregar("Brayan", "201805390", "23", "Sistemas")
##newList.agregar("Eduardo", "201805390", "23", "Sistemas")
##newList.recorrer()
##print("-------------------------------")
##newList.eliminar("201905390")
##newList.recorrer()
##print("-------------------------------")
##newList.buscar("201805390")
##newList.buscar("201905390")
##newList.graficar()