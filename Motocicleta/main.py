import sys 
sys.path.append("C:/Users/guzma/OneDrive/Escritorio/Motocicleta/clases")
from Motocicleta import Motocicleta

moto_one = Motocicleta("Azul","AC 196 UT",18,2, 2019, 300, 500)
moto_one.marca = "Sandero"
moto_one.modelo = "785XS"
moto_one.precio = "$19.000"

moto_two = Motocicleta("Rojo", "AA 987 UT", 10, 2, 2022, 400, 650)
moto_two.marca = "Sandero"
moto_two.modelo = "775XS"
moto_two.precio = "$15.000"

print(moto_one.marca)
moto_one.apagar_motor()
moto_one.encender_motor()


moto_one.consultar_precio()
moto_two.consultar_precio()