from Cuenta import Cuenta

class CuentaJoven(Cuenta):
    def __init__(self, nombre, edad, dni, cantidad=0, bonificacion) -> None:
        super().__init__(nombre, edad, dni, cantidad)
        self.__bonificacion = bonificacion
    
    @property
    def bonificacion(self):
        return self.__bonificacion
    
    @bonificacion.setter
    def bonificacion(self, valor):
        self.__bonificacion = valor

    def es_titular_valido(self):
        return self.es_mayor_de_edad() and self.edad < 25
    
    def retirar(self, cantidad):
        if self.es_titular_valido():
            return super().retirar(cantidad)
        else:
            print("No es titular valido")
    def mostrar(self):
        print("Cuenta joven")
        print(f"Bonificacion: {self.bonificacion}")
        return super().mostrar()