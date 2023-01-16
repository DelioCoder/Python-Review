class Persona():

    def __init__(self, nombre, edad, lugar_residencia):

        self.nombre             = nombre;
        self.edad               = edad;
        self.lugar_residencia   = lugar_residencia

    def descripcion(self):

        print(f"Nombre: {self.nombre} \nEdad: {self.edad} \nResidencia: {self.lugar_residencia}");

class Empleado(Persona):
    
    def __init__(self, nombre_empleado, edad_empleado, residencia_empleado, salario, antiguedad):
        super().__init__(nombre_empleado, edad_empleado, residencia_empleado)
        self.salario    = salario
        self.antiguedad = antiguedad

    def descripcion(self):

        super().descripcion();

        print(f"Salario: {self.salario}, Antiguedad: {self.antiguedad}")

Antonio = Persona("Antonio", 55, "España")

Antonio.descripcion();

print(isinstance(Antonio, Empleado))