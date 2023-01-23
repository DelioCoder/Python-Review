# Objects Serialization

import pickle

class Vehiculo():

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

coche1 = Vehiculo("Mazda", "MX5")

coche2 = Vehiculo("Seat", "Leon")

coche3 = Vehiculo("Renault", "Megane")

coches = [coche1, coche2, coche3]

fichero = open("vehicles", "wb")

pickle.dump(coches, fichero)

fichero.close()

del (fichero)

fichero_apertura = open("vehicles", "rb")

misCoches = pickle.load(fichero_apertura)

fichero_apertura.close()

for v in misCoches:

    print(v.estado())