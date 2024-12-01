nombre_paciente=[]
edad =[]

def agregar_nombre(paciente):
    nombre_paciente.append(paciente)
    print(f"Paciente agregado: {paciente}")

def agregar_edad(año_nacimiento):
    edad_actual = 2024 - int(año_nacimiento)
    edad.append(edad_actual)

def paciente_mayor_menor():
    edad_mayor = max(edad)
    edad_menor = min(edad)
    index_mayor = edad.index(edad_mayor)
    index_menor = edad.index(edad_menor)
    
    print(f"\nEl paciente mayor es: {nombre_paciente[index_mayor]} con {edad_mayor} años.")
    print(f"El paciente menor es: {nombre_paciente[index_menor]} con {edad_menor} años.")

def informacion():
    return nombre_paciente, edad