# Bucle indeterminado porque no sabemos cuantas veces se repetira la condición
# Indeterminate loop cause' we don't know how many times it would repeat the condition inside

# i = 1

# while i<=10:

#     print(f"Hola {str(i)}");

#     i=i+1

# print("Termino la ejecución")

#2

# edad = int(input("Introduce la edad: "))

# while edad < 5 or edad>100:
#     print("Haz introducido una edad negativa. Vuelve a intentarlo")

#     edad = int(input("Introduce la edad otra vez: "))

# print("Fin del programa")

#3

import math

print("Programa de cálculo de raíz cuadrada")

numero = int(input("Introduce un número: "))

intentos = 0

while numero < 0:
    
    if numero < 0:
        intentos = intentos+1

    print("No se puede hallar la raíz de un número negativo")

    if intentos == 2:
        print("Haz consumido demasiados intentos. El programa ha finalizado")
        break;

    numero = int(input("Introduce un número otra vez: ")) 
    
if intentos < 2:
    solucion = math.sqrt(numero)
    print(f"La raíz cuadrada de {str(numero)} es {str(solucion)}")