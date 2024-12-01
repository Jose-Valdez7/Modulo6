from laptop import Laptop

laptop_pepito=Laptop("lenovo","i7",32)
laptop_maria= Laptop("lenovo","i7",32,600)

for numero in range(1,1001):
    asus_laptop=Laptop.asus_laptop(numero)
    print(asus_laptop.__dict__)

# print(laptop_pepito.__dict__)
# print(laptop_pepito.valor_final())           
# print(f"el valor de descuento: {laptop_pepito.valor_descuento(10)}")  

#print(Laptop.comparar_costo(laptop_pepito,laptop_maria)) 


