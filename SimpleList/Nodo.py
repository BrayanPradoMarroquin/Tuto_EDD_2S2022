from asyncio.windows_events import NULL


class Node:
    def __init__(self, Nombre, carnet, edad, carrera):
        self.Nombre = Nombre
        self.carnet = carnet
        self.edad = edad
        self.carrera = carrera
        self.siguiente = None