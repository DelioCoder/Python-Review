def suma(num1, num2):
    
    total = num1 + num2;

    return total;

def restar(num1, num2):

    total = num1 - num2;

    return total;

def multiplicar(num1, num2):

    total = num1 * num2;

    return total;

def dividir(num1, num2):

    try:    

        total = num1 / num2;

        return total;

    except ZeroDivisionError:
        print("No se puede dividir entre 0");
        return "Operación errónea";

while True:

    try:

        op1 = int(input("Introduce el primer número"))

        op2 = int(input("Introduce el segundo número"))

        break;

    except ValueError:
        print("Los valores introducidos no son correctos. Intentalo de nuevo")

operacion = input("Introduce la operación: ")

if operacion == "suma":
    print(suma(op1, op2))

elif operacion == "resta":
    print(restar(op1, op2))

elif operacion == "multiplicar":
    print(multiplicar(op1, op2))

elif operacion == "dividir":
    print(dividir(op1, op2))

else:
    print("Operación desconocida")