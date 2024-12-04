import random
from laptop import Laptop

class Laptop_Business(Laptop):
    def __init__(self, marca, procesador, memoria, almacenamiento, duracion_bateria, costo=500, impuesto=10):
        super().__init__(marca, procesador, memoria, costo, impuesto)
        self.almacenamiento=almacenamiento
        self.duracion_bateria=duracion_bateria
    
    def __str__(self):
        return f"Marca: {self.marca}\n Procesador: {self.procesador} \n Memoria: {self.memoria} \n Costo:{self.costo}\n Impuesto: {self.impuesto}\n Almacenamiento: {self.almacenamiento}\n Duración de Batería: {self.duracion_bateria}\n"

    def realizar_diagnostico_sistema(self):
        resultado_diagnostico= super().realizar_diagnostico_sistema()
        resultado_conectividad=self.verificar_conectividad()
        resultado_diagnostico["Resultado conectividad"]=resultado_conectividad
        return resultado_diagnostico
    
    def verificar_conectividad(self):
        conectividad={
            "WiFi_disponible": random.choice([True,False]),
            "Acceso_servidor_empresarial": random.choice([True,False]),
            "Latencia_aceptable": random.choice([True, False])
        }
        return conectividad
    
pass
    
