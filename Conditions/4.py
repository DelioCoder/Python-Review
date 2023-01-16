# edad = 7

# if 0 < edad < 100:
#     print("Edad es correcta")
# else:
#     print("Edad incorrecta")

salario_presidente = int(input("Ingrese salario presidencial: "));

print(f"Salario presidente: {str(salario_presidente)}")

salario_director = int(input("Ingrese salario director: "));

print(f"Salario director: {str(salario_director)}")

salario_jefe_area = int(input("Ingrese salario jefe área: "));

print(f"Salario Jefe Área: {str(salario_jefe_area)}")

salario_administrativo = int(input("Ingrese salario administrativo: "));

print(f"Salario administrativo: {str(salario_administrativo)}")

if salario_administrativo < salario_jefe_area < salario_director < salario_presidente:
    print("Todo funciona correctamente");

else:
    print("Algo falla en esta empresa");