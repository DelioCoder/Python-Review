# print("Programa de becas año 2022")

# distancia_escuela = int(input("Introduce la distancia a la escuela en km: "))

# print(distancia_escuela);

# num_hermanos = int(input("Introduce el n° de hermanos en el centro: "))

# print(num_hermanos);

# salario_familiar = int(input("Introduce salario anual bruto: "))

# print(salario_familiar)

# if distancia_escuela > 40 and num_hermanos > 2 or salario_familiar <= 20000:
#     print("Tienes derecho a beca")

# else:
#     print("No tienes derecho a beca")

# Operador in: Permite evaluar varias condiciones a la vez

print("Asignaturas optativas año 2022");

print("Asignaturas optativas: Informática gráfica - Pruebas de software - Usabilidad y Accesibilidad");

opcion = input("Escribe la asignatura escogida: ");

asignatura = opcion.lower();

if asignatura in ("Informática gráfica", "Pruebas de software", "Usabilidad y Accesibilidad"):

    print(f"Asignatura elegida: {asignatura}");

else:

    print("")