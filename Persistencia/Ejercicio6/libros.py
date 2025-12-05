import json

class Libro:
    def __init__(self, cod, tit, pre):
        self.__codLibro = cod
        self.__titulo = tit
        self.__precio = pre

    def to_dict(self):
        return {
            "codLibro": self.__codLibro,
            "titulo": self.__titulo,
            "precio": self.__precio
        }

    @staticmethod
    def leer():
        cod = int(input("codigo libro: "))
        tit = input("titulo: ")
        pre = float(input("precio: "))
        return Libro(cod, tit, pre)

    def mostrar(self):
        print("Cod:", self.__codLibro)
        print("Titulo:", self.__titulo)
        print("Precio:", self.__precio)

    def getCod(self):
        return self.__codLibro

    def getPrecio(self):
        return self.__precio


class Cliente:
    def __init__(self, cod, ci, nom, ape):
        self.__codCliente = cod
        self.__ci = ci
        self.__nombre = nom
        self.__apellido = ape

    def to_dict(self):
        return {
            "codCliente": self.__codCliente,
            "ci": self.__ci,
            "nombre": self.__nombre,
            "apellido": self.__apellido
        }

    @staticmethod
    def leer():
        cod = int(input("codigo cliente: "))
        ci = input("ci: ")
        nom = input("nombre: ")
        ape = input("apellido: ")
        return Cliente(cod, ci, nom, ape)

    def mostrar(self):
        print("Cod:", self.__codCliente)
        print("CI:", self.__ci)
        print("Nombre:", self.__nombre)
        print("Apellido:", self.__apellido)

    def getCod(self):
        return self.__codCliente


class Prestamo:
    def __init__(self, codC, codL, fecha, cant):
        self.__codCliente = codC
        self.__codLibro = codL
        self.__fechaPrestamo = fecha
        self.__cantidad = cant

    def to_dict(self):
        return {
            "codCliente": self.__codCliente,
            "codLibro": self.__codLibro,
            "fechaPrestamo": self.__fechaPrestamo,
            "cantidad": self.__cantidad
        }

    @staticmethod
    def leer():
        codC = int(input("cod cliente: "))
        codL = int(input("cod libro: "))
        fecha = input("fecha: ")
        cant = int(input("cantidad: "))
        return Prestamo(codC, codL, fecha, cant)

    def mostrar(self):
        print("codCliente:", self.__codCliente)
        print("codLibro:", self.__codLibro)
        print("fecha:", self.__fechaPrestamo)
        print("cant:", self.__cantidad)

    def getCodCliente(self):
        return self.__codCliente

    def getCodLibro(self):
        return self.__codLibro

    def getCantidad(self):
        return self.__cantidad


class ArchLibro:
    def __init__(self, nomArch):
        self.__nomArch = nomArch

    def crearArchivo(self):
        with open(self.__nomArch, "w") as f:
            json.dump([], f, indent=4)

    def adicionar(self, l):
        try:
            with open(self.__nomArch, "r") as f:
                lista = json.load(f)
        except:
            lista = []
        lista.append(l.to_dict())
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
        for x in lista:
            print(x)

    def librosEntre(self, x, y):
        lista = self.cargar()
        for l in lista:
            if x <= l["precio"] <= y:
                print(l)




class ArchCliente:
    def __init__(self, nomArch):
        self.__nomArch = nomArch

    def crearArchivo(self):
        with open(self.__nomArch, "w") as f:
            json.dump([], f, indent=4)
    def adicionar(self, c):
        try:
            with open(self.__nomArch, "r") as f:
                lista = json.load(f)
        except:
            lista = []
        lista.append(c.to_dict())
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
        for x in lista:
            print(x)


class ArchPrestamo:
    def __init__(self, nomArch):
        self.__nomArch = nomArch

    def crearArchivo(self):
        with open(self.__nomArch, "w") as f:
            json.dump([], f, indent=4)

    def adicionar(self, p):
        try:
            with open(self.__nomArch, "r") as f:
                lista = json.load(f)
        except:
            lista = []
        lista.append(p.to_dict())
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
        for x in lista:
            print(x)

    def ingresoLibro(self, codL, archLibros):
        pre_libros = {}
        for l in archLibros.cargar():
            pre_libros[l["codLibro"]] = l["precio"]
        s = 0
        for p in self.cargar():
            if p["codLibro"] == codL:
                s += p["cantidad"] * pre_libros.get(codL, 0)
        return s

    def nuncaVendidos(self, archLibros):
        todos = archLibros.cargar()
        usados = set()
        for p in self.cargar():
            usados.add(p["codLibro"])
        for l in todos:
            if l["codLibro"] not in usados:
                print(l)

    def clientesDeLibro(self, codL, archClientes):
        cli = {c["codCliente"]: c for c in archClientes.cargar()}
        vistos = set()
        for p in self.cargar():
            if p["codLibro"] == codL:
                codC = p["codCliente"]
                if codC in cli and codC not in vistos:
                    print(cli[codC])
                    vistos.add(codC)

    def libroMasPrestado(self, archLibros):
        conteo = {}
        for p in self.cargar():
            codL = p["codLibro"]
            conteo[codL] = conteo.get(codL, 0) + p["cantidad"]
        if not conteo:
            return None
        codMax = max(conteo, key=conteo.get)
        for l in archLibros.cargar():
            if l["codLibro"] == codMax:
                return l

    def clienteMasPrestamo(self, archClientes):
        conteo = {}
        for p in self.cargar():
            codC = p["codCliente"]
            conteo[codC] = conteo.get(codC, 0) + p["cantidad"]
        if not conteo:
            return None
        codMax = max(conteo, key=conteo.get)
        for c in archClientes.cargar():
            if c["codCliente"] == codMax:
                return c


archL = ArchLibro("libros.bin")
archC = ArchCliente("clientes.bin")
archP = ArchPrestamo("prestamos.bin")

archL.crearArchivo()
archC.crearArchivo()
archP.crearArchivo()

l1 = Libro(1, "Algebra", 50)
l2 = Libro(2, "Calculo", 80)
l3 = Libro(3, "Fisica", 40)
l4 = Libro(4, "Historia", 30)

archL.adicionar(l1)
archL.adicionar(l2)
archL.adicionar(l3)
archL.adicionar(l4)

c1 = Cliente(1, "111", "Ana", "Lopez")
c2 = Cliente(2, "222", "Luis", "Perez")
c3 = Cliente(3, "333", "Maria", "Gomez")

archC.adicionar(c1)
archC.adicionar(c2)
archC.adicionar(c3)

p1 = Prestamo(1,1,"2024-01-01", 2)
p2 = Prestamo(2,1,"2024-01-02", 1)
p3 = Prestamo(2,2,"2024-01-03", 3)
p4 = Prestamo(3,2,"2024-01-04", 1)
p5 = Prestamo(1,3,"2024-01-05", 1)

archP.adicionar(p1)
archP.adicionar(p2)
archP.adicionar(p3)
archP.adicionar(p4)
archP.adicionar(p5)


archL.librosEntre(35, 60)
print()


print(archP.ingresoLibro(1,archL))
print()


archP.nuncaVendidos(archL)
print()


archP.clientesDeLibro(2,archC)
print()


print(archP.libroMasPrestado(archL))
print()


print(archP.clienteMasPrestamo(archC))
