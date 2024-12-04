from laptop import Laptop
from laptop_gaming import Laptop_Gaming
from laptop_business import Laptop_Business

#POLIMORFISMO
def imprimir_informe(Laptop):
    informe=Laptop.realizar_informe_uso()
    for clave,valor in informe.items():
        print(f"{clave} : {valor}")
    print("\n")

laptop_pepito=Laptop("lenovo","i7",32)
laptop_maria= Laptop("lenovo","i7",32,600)

laptop_juanito=Laptop_Gaming ("MSI","I7",4,"RTX 8GB")
print(laptop_juanito.realizar_diagnostico_sistema())

laptop_empresarial = Laptop_Business("Dell","I7",16,"1024GB SSD","8 horas")
print(laptop_empresarial.realizar_diagnostico_sistema())

print("PEPITO: ")
imprimir_informe(laptop_pepito)

print("JUANITO: ")
imprimir_informe(laptop_juanito)

# for numero in range(1,1001):
#     asus_laptop=Laptop.asus_laptop(numero)
#     print(asus_laptop.__dict__)

# print(laptop_pepito.__dict__)
# print(laptop_pepito.valor_final())           
# print(f"el valor de descuento: {laptop_pepito.valor_descuento(10)}")  

#print(Laptop.comparar_costo(laptop_pepito,laptop_maria)) 


