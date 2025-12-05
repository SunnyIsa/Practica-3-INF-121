import json

class Jugador:
    def __init__(self, nom, niv, punt):
        self.__nombre = nom
        self.__nivel = niv
        self.__puntaje = punt

    def to_dict(self):
        return {
            "nombre": self.__nombre,
            "nivel": self.__nivel,
            "puntaje": self.__puntaje
        }

    @staticmethod
    def leer():
        nom = input("nombre jugador: ")
        niv = int(input("nivel: "))
        punt = int(input("puntaje: "))
        return Jugador(nom, niv, punt)

    def mostrar(self):
        print("Nombre:", self.__nombre)
        print("Nivel:", self.__nivel)
        print("Puntaje:", self.__puntaje)

    def getNombre(self):
        return self.__nombre


class ArchJugador:
    def __init__(self, nomArch):
        self.__nomArch = nomArch

    def crearArchivo(self):
        with open(self.__nomArch, "w") as f:
            json.dump([], f, indent=4)

    def adicionar(self, j):
        try:
            with open(self.__nomArch, "r") as f:
                lista = json.load(f)
        except:
            lista = []
        lista.append(j.to_dict())
        with open(self.__nomArch, "w") as f:
            json.dump(lista, f, indent=4)

    def cargar(self):
        try:
            with open(self.__nomArch, "r") as f:
                return json.load(f)
        except:
            return []

    def listar(self):
        lista = self.cargar()
        for j in lista:
            print(j)

    def buscarNombre(self, nom):
        lista = self.cargar()
        for j in lista:
            if j["nombre"] == nom:
                print(j)


arch = ArchJugador("jugadores.txt")
arch.crearArchivo()

j1 = Jugador("Ragnar", 12, 1500)
j2 = Jugador("Atenea", 20, 2400)
j3 = Jugador("ShadowKing", 30, 5000)

arch.adicionar(j1)
arch.adicionar(j2)
arch.adicionar(j3)

print("Lista de jugadores:")
arch.listar()
print()

print("Buscar jugador = 'Atenea'")
arch.buscarNombre("Atenea")
