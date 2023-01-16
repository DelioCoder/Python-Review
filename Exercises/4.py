# Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos. 

# def max(num1, num2):

#     if(num1 > num2):
#         print(f"{num1} es mayor que {num2}")

#     else:
#         print(f"{num2} es mayor que {num1}")

# max(1,2)

# Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.

# def max_three(num1, num2, num3):

#     if(num1 > num2 and num1 > num3):
#         print(f"{num1} es mayor que {num2} y {num3}")

#     elif (num1 < num2 and num2 > num3):
#         print(f"{num2} es mayor que {num1} y {num3}")

#     else:
#         print(f"{num3} es mayor que {num1} y {num2}")

# max_three(4,1,8)

# Definir una función que calcule la longitud de una lista o una cadena dada. 

# def getLong(list):
    
#     cont = 0

#     for i in list:
        
#         cont += 1

# milista = ["hola", "adsa", "dasd", "dasdas", "dasdas"]

# getLong(milista)

#  Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.



def vocal(x):

    vocales = ["a", "e", "i", "o", "u"];

    letra = x.lower();

    for i in vocales:
        
        if letra != i:
            return False

        else:
            return True

print(vocal("A"))