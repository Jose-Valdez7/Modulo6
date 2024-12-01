#Listas

planetas = ["Mercurio", "Venus", "Tierra", "Marte", "Jupiter", "Saturno", "Urano","Neptuno"]
# print (planetas[-1])
# print (planetas[2: ])
# print(len(planetas))
# print(planetas[7])

#Trabajar con una lista de numeros
gravdedad_en_planetas = [0.378 , 0.907, 1, 0.377, 2.36, 0.916, 0.889, 1.12]
peso_bus= 124054 #Newtons, en la Tierra
print(f"En la Tierra, un autobus de dos pisos pesa {peso_bus} N")
print(f"En Mercurio, un atobus de dos pisos pesa {peso_bus * gravdedad_en_planetas[0]} N")

print(f"Lo mas liviano que seria un autobus en el sistema solar es {peso_bus * min(gravdedad_en_planetas)} N")
print(f"Lo mas pesado que seria un autobus en el sistema solar es {peso_bus*max(gravdedad_en_planetas)} N")