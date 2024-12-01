class Laptop:
    def __init__(self,marca,procesador, memoria, costo=500, impuesto=10):
        self.marca = marca
        self.procesador= procesador
        self.memoria= memoria
        self.costo=costo
        self.impuesto=impuesto
    
    def valor_final(self):
        return self.costo + self.impuesto
    
    def valor_descuento(self, descuento):
        return (self.costo*descuento)/100

    @staticmethod
    def comparar_costo(Laptop1,Laptop2):
        if Laptop1.costo == Laptop2.costo:
            return "Los costos son iguales"
        else:
            return "Los costos son diferentes"
    
    @classmethod
    def asus_laptop(cls,costo):
        marca="asus"
        procesador="i5"
        memoria=16
        return cls(marca,procesador,memoria,costo)