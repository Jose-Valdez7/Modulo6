import random

Zona_urbana_max=random.randint(1,90)
Zona_urbana_min=random.randint(1,20)
Zona_rural_max=random.randint(1,90)
Zona_rural_min=random.randint(1,90)
Zona_perimetral_max=random.randint(1,150)
Zona_perimetral_min=random.randint(1,90)

if Zona_urbana_max <=50:
    print("Excedida velocidad max zona urbana ecuatoriana")
elif Zona_urbana_min >=10:
    print("Velocidad de circulacion zona urbana ecuatoriana muy baja Acelere!!")

if Zona_rural_max <=80:
    print("Excedida velocidad max zona rural colombiana")
elif Zona_rural_min >=31:
    print("Velocidad de circulacion zona rural colombiana muy baja Acelere!!")

if Zona_perimetral_max <=120:
    print("Excedida velocidad max zona perimetral peruana")
elif Zona_perimetral_min >=61:
    print("Velocidad de circulacion zona perimetral peruana muy baja Acelere!!")


