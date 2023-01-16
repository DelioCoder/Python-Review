# Elio

number = int(input("Introduce un número: "))
number_2 = int(input("Introduce otro número: "));

isMinor = True;

while number_2 > number:

    number = number_2

    if number_2 < number:
        break;

    number_2 = int(input(f"Introduce otro número mayor que {number_2} :"));


print("Fin del programa")

# Pildoras

# num1 = int(input("Introduce un número: "))
# num2 = int(input(f"Introduce un número mayor que {num1} :"))

# while num2 > num1:
#     num1 = num2
#     num2 = int(input(f"Escriba un número mayor que {num1} :"))

# print(f"{num2} no es mayor que {num1}")