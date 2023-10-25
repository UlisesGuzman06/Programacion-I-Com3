class Motocicleta:
    state = "Nuevo"
    motor_estado = False
    def __init__(self,color,matricula,combustible_litros,numero_ruedas,fecha_fabricacion,velocidad_punta,peso):
        self.color = color
        self.matricula = matricula
        self.combustible_litros = combustible_litros
        self.numero_ruedas = numero_ruedas
        self.__marca = " "
        self.__modelo = " "
        self.fecha_fabricacion = fecha_fabricacion
        self.velocidad_punta = velocidad_punta
        self.peso = peso
    @property
    def marca(self):
        return self.__marca
    @property
    def modelo(self):
        return self.__modelo
    @marca.setter
    def marca(self,new_marca):
        self.__marca = new_marca
    @modelo.setter
    def modelo(self,new_modelo):
        self.__modelo = new_modelo
    def encender_motor(self):
        if(self.motor_estado==True):
            print("El motor esta encendido")
        else:
            print("El motor estaba apagado, ahora esta encendido")
            self.motor_estado = True

    def apagar_motor(self):
        if(self.motor_estado==False):
            print("El motor esta apagado")
        else:
            print("El motor estaba encendido, ahora esta apagado")
            self.motor_estado = False
    def consultar_precio(self):
        print(f"El precio de la motocicleta {self.marca} modelo {self.modelo} es de {self.precio}")
    