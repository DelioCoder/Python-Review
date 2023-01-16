# Ejercicio 1

# num_1 = int(input("Ingrese un número: "))
# num_2 = int(input("Ingrese otro número: "))

# def DevuelveMax():

#     if(num_1 > num_2):
#         print(f"Número A {num_1} es mayor que {num_2}");

#     else:
#         print(f"Número B {num_2} es mayor que {num_1}");

# DevuelveMax();

# Ejercicio 2

# lista = []

# nom     = input("Introduzca un nombre: ");
# direc   = input("Ingrese una dirección: ");
# tfno    = int(input("Ingrese un número telefonico: "));

# lista.append(nom);
# lista.append(direc);
# lista.append(tfno);

# print(f"Los datos personales son: {lista[0]} {lista[1]} {lista[2]}");

# Ejercicio 3

num1 = int(input("Introduce primera nota: "));
num2 = int(input("Introduce segunda nota: "));
num3 = int(input("Introduce tercera nota: "));

media = (num1 + num2 + num3 )/3;

print(f"Su promedio es: {round(media,1)}");