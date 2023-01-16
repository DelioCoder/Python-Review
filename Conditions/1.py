print("Programa de evaluación de notas de alumnos");

nota_alumno = int(input());

def evaluation(nota):
    
    valoracion = "aprobado";

    if nota<5:
        valoracion = "suspenso";

    return valoracion;

print(evaluation(nota_alumno));