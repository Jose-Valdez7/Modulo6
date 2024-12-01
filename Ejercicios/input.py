nota_tarea=float(input("Ingresar la nota de la tarea: "))
nota_leccion=float(input("Ingresar la nota de la leccion: "))
nota_examen=float(input("Ingresar la nota del examen: "))

total_promedio = (nota_leccion + nota_tarea + nota_examen)/3

print(f"Promedio: {total_promedio}")