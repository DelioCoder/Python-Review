print("Verificación de acceso");

nota_alumno = int(input("Introduce una nota: "))

if nota_alumno < 5:
    print("Insuficiente")

if nota_alumno < 6:
    print("Bien")

if nota_alumno < 7:
    print("Bien")

if nota_alumno < 9:
    print("Notable")

else:
    print("Sobresaliente")