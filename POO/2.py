# Herencia

class Vehiculos():

    def __init__(self, marca: str, modelo: str):
        
        self.marca      = marca
        self.modelo     = modelo
        self.enMarcha   = False
        self.acelera    = False
        self.frena      = False

    def arrancar(self):

        self.enMarcha = True

    def acelerar(self):
        
        self.acelera = True

    def frenar(self):

        self.frena = True

    def estado(self):

        print(f"Marca: {self.marca} \nModelo: {self.modelo} \nEn marcha: {self.enMarcha} \nAcelerando: {self.acelera} \nFrenando: {self.frena}")

class Furgoneta(Vehiculos):
    
    def carga(self, cargar):

        self.cargado = cargar

        if self.cargado:

            return "La furgoneta está cargada"

        else:

            return "La furgoneta no esta cargada"

print("Furgoneta")

print("")

miFurgoneta = Furgoneta("Renault", "Kangoo")

miFurgoneta.arrancar();

miFurgoneta.estado();

print(miFurgoneta.carga(True))

class Moto(Vehiculos):

    hCaballito = ""

    def caballito(self):
        self.hCaballito = "Voy haciendo el caballito"

    def estado(self):

        print(f"Marca: {self.marca} \nModelo: {self.modelo} \nEn marcha: {self.enMarcha} \nAcelerando: {self.acelera} \nFrenando: {self.frena} \n{self.hCaballito}")

print("")

print("Moto")

print("")

miMoto = Moto("Honda", "CBR");

miMoto.caballito()

miMoto.estado()

class VElectricos(Vehiculos):

    def __init__(self, marca, modelo):

        super().__init__(marca, modelo)

        self.autonomia = 100
        
    def cargarEnergia(self):

        self.cargando = True

class BicicletaElectrica(VElectricos, Vehiculos):

    pass

print("")

print("Bicicleta Electrica")

miBicicleta = BicicletaElectrica("Orbea", "HC1030");