class Persona:
    def __init__(self, nombre, edad, dni) -> None:
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni
        
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor
    
    @property
    def edad(self):
        return self.__edad
    
    @edad.setter
    def edad(self, valor):
        self.__edad = valor
    
    @property
    def dni(self):
        return self.__dni
    
    @dni.setter
    def dni(self, valor):
        self.__dni

    def mostrar(self):
        string = f"El nombre es: {self.__nombre}, tiene {self.__edad} y su dni es: {self.__dni}"
        print(string)
    
    def es_mayor_de_edad(self):
        return self.edad >= 18
    
p1 = Persona('pepe', 20, 270416)
p1.mostrar()