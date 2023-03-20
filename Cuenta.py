from Persona import Persona

class Cuenta(Persona):
    def __init__(self, nombre, edad, dni, cantidad=0) -> None:
        super().__init__(nombre, edad, dni)
        self.__cantidad = cantidad
    
    @property
    def cantidad(self):
        return self.__cantidad
    
    def mostrar(self):
        super().mostrar()
        print(f"El saldo es: {self.__cantidad}")
    
    def ingresar(self, cantidad):
        self.__cantidad += cantidad
    
    def retirar(self, cantidad):
        self.__cantidad -= cantidad
