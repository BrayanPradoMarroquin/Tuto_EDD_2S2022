from SimpleList import SimpleList

newList = SimpleList()

newList.agregar("Byron", "201805390", "20", "Sistemas")
newList.agregar("Ana", "201805391", "22", "Sistemas")
newList.agregar("Luis", "201905390", "20", "Sistemas")
newList.agregar("Brayan", "201805390", "23", "Sistemas")
newList.agregar("Eduardo", "201805390", "23", "Sistemas")
newList.recorrer()
print("-------------------------------")
newList.eliminar("201905390")
newList.recorrer()
print("-------------------------------")
newList.buscar("201805390")
newList.buscar("201905390")
newList.graficar()