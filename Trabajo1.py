#Ejercicios complementarios

#1. Crea una variable llamada "numero1" y asígnale un número entero de tu elección

numero1 = int(5)

#2. No borres la variable número uno y crea una variable llamada "numero2" asignándole
#un número decimal de tu elección

numero2 = int(3)

#3. Crear una variable llamada "suma" y almacena la suma de "numero1" y "numero2"

suma = numero1 + numero2

#4. Ahora crear tres variables más sin borrar lo que tienes. Una para resta, otra para
#multiplicación y otra para división. Imprime estas variables.

resta = numero1 - numero2
division = numero1 / numero2
multiplicacion = numero1 * numero2

print(suma)
print(resta)
print(division)
print(multiplicacion)


#5. Crea una variable llamada "nombre" y asígnale tu nombre como valor.

nombre = "ulises"

#6. Crea una variable llamada "precio" y asígnale un valor decimal que represente el
#precio de un artículo ficticio.

precio = 20.99

#7. Ahora, sin borrar la variable anterior, crea una variable llamada "descuento" y asígnale
#un valor decimal que represente el descuento aplicado al artículo. Por ejemplo, si le
#quieres aplicar un 25% de descuento, dale un valor de 0,25. El valor 1 equivaldría al
#100% y el valor 0 al 0%

descuento = 0.25 * precio

#8. Ahora, intenta calcular el precio final aplicando el descuento al precio original y
#almacena el resultado en una variable llamada "precio_final". Para ello vas a tener que
#aplicar la lógica de matemáticas.

precio_final = precio - descuento
print(precio_final)

#9. Crea una variable llamada "cadena" y asignale un texto, una frase, lo que quieras de tu
#elección. Qué sea un string.

cadena = "esto es una cadena"
print(type(cadena))

#10. Sin borrar la variable "cadena", crea una nueva variable llamada "longitud". En ella, vas
#a almacenar la longitud en caracteres de la cadena utilizando una de las funciones de
#Python

longitud = len("longitud")
print(longitud)

#11. rea otra vez la variable llamada "precio" y dale un valor decimal, el que sea y
#conviértelo en número entero. Lo puedes hacer en la misma variable o en otra, da lo
#mismo.

precio1 = 10.65
print(int(precio1))

#12. Crea dos variables. Una se va a llamar "nombre" y la segunda "apellido" concaténalas
#en una tercera variable llamada "nombre_completo", el nombre y el apellido con un
#espacio entre medio. Puedes usar libremente la forma de concatenación que quieras.

nombre1 = "Ulises "
apellido1 = "Guzman"

nombre_completo = (nombre1 + apellido1)
print(nombre_completo)

#13. Escribe tu edad en una variable. Increméntala en 5 y luego disminúyela en 10.

edad = 18
edad += 5
print(edad)
edad -= 10
print(edad)

#14. Crea una variable llamada "altura" que contenga con decimales, tu altura en metros y
#centímetros. Por ejemplo: 1.83. Multiplícala por 4 y luego divídela en 3.

altura = 1.82
altura *= 4
print(altura)
altura /= 3
print(altura)

#15. Crea una variable que contenga tu nombre completamente en mayúsculas. Después
#transfórmalo todo en minúsculas con algún método o función de Python.

nombre_mayusculas = "ULISES"
print(nombre_mayusculas.lower())

#16. Por último, con la variable con el nombre en mayúsculas, aplica un método parecido
#para que se transforme todo en minúsculas excepto la primera letra.

print(nombre_mayusculas.title())