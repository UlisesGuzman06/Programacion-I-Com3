

'''x = 0

while x<= 30:
    x+=1
    
    if x == 15:
        print(f"The execution of the loop was broken when x was {x}")
        break 
    elif x== 4 or x == 6 or x == 10:
        print(f"the value {x} of x was skipped")
        continue
    print(f"The value of the loop is: {x}")'''
    
    
#ejercicio 1
'''word = ""
while word != " ":
    word = input("ingrese una palabra: ")
    print(word.upper())'''
    
#ejercicio 2
'''D = 0
R = 0
total = 0
ingresar = ""
while ingresar != " ":
    
    ingresar = input("ingrese la operacion que desea realizar (D) deposito (R) retirar: ")
    
    if ingresar == "D":
        D = float(input("Ingrese el valor que desea depositar: "))
        total += D
    elif ingresar == "R":
        if R > total:
            print("su cuenta no dispone de ese total! ")
        elif R <= total:
            R = float(input("Ingrese el valor que desea retirar: "))
    else:
        print("Ingrese una operacion valida!")
total-= R
print(f"La bitacora de su cuenta es: {total}")'''

#ejercicio 3

'''binnacle = 0
aux = input() . upper()
while aux !=" " or aux !="":
    if aux == " ":
        break
    elif "D"  in aux[0]:
        aux = aux . split(" ")
        aux[1] = float(aux[1])
        binnacle += aux[1]
    elif "R" in aux[0]:
        aux = aux . split(" ")
        aux[1] = float(aux[1])
        binnacle -=aux[1]

    aux = input() . upper()


print("LA BITÁCORA ES: ", binnacle)'''
#ejercicio 4

'''one_year = int(input("Ingrese el primer año: "))
two_year = int(input("Ingrese el segundo año: "))

for i in range(one_year, two_year, 1):
    if (i% 4 ==0 or(i%100==0 and i%400==0)) and i%10==0 :
        print(i)'''

#ejercicio 5

'''for i in range(1,20+1):
    if i%2!=0:
        continue
    print(i)'''
    
#ejercicio 6

'''list_number = [1,2,3,4,5,6,7,8,9,0]
number = int(input("ingrese un numero: "))
for i in list_number:
    if i == number:
        print(f"el numero encontrado es {i}")'''

#ejercicio 7

'''option = " "
while option != "":
    if option == 1:
        print("Elegiste la opcion 1")
    elif option == 2:
        print("elegiste la opcion 2")
    elif option == 3:
        print("elegiste la opcion 3")
    elif option == 0:
        break
    else:
        print("elija una opcion correcta")
    option = int(input("Ingresa una opcion: "))'''



