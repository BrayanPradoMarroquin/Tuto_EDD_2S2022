from asyncio.windows_events import NULL


class Node:
    def __init__(self, Nombre, carnet, edad, carrera):
        self.Nombre = Nombre
        self.carnet = carnet
        self.edad = edad
        self.carrera = carrera
        self.siguiente = None

##class NodoPaciente:
    ##def __init__(self, Nombre, edad):
        ##self.Nombre = Nombre
        ##self.edad = edad
        ##self.siguiente = None
        ##Self.SintomasAnteriores = ListaLista()
        ##Self.SintomasDespues = ListaLista()