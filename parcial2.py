def is_mutant(adn):
    pos_mutant = ('AAAA', 'TTTT', 'CCCC', 'GGGG')
    for i in adn:
        for j in i:
            print(j, end=' ')
        print()
    #Filas
    for fila in adn:
        for i in range(len(fila) - 3):  
            for pos_mutant in pos_mutant:
                if fila[i:i + 4] == pos_mutant:
                    return True
    #Columnas
    for i in range(6):
        for j in range(3):
            if adn[j][i] == adn[j+1][i] == adn[j+2][i] == adn[j+3][i]:
                return True
    #Diagonales
    #Derecha
    for i in range(3):
        for j in range(3):
            if adn[i][j] == adn[i+1][j+1] == adn[i+2][j+2] == adn[i+3][j+3]:
                return True
    #Izquierda
    for i in range(3):
        for j in range(3):
            if adn[i][j+3] == adn[i+1][j+2] == adn[i+2][j+1] == adn[i+3][j]:
                return True

    # Si no se encuentra ninguna mutacion retornar False
    return False
adn = []
while len(adn) != 6:
    value = 0
    adn_str = input("Ingrese los valores del adn: ").upper()
    if len(adn_str) == 6:
        for adn_letter in adn_str:
            if (not(adn_letter=="A" or adn_letter == "T" or adn_letter == "G" or adn_letter == "C")):
                value = 1
        if value == 1:
            print("Los valores de la mutacion no son correctos!")
            continue
        else:
            print("Valor de mutacion correcto!")
            adn.append(adn_str)
    else:
        print("Ingrese 6 valores correctos!")

if is_mutant(adn):
    print("El humano es un mutante.")
else:
    print("El humano no es un mutante.")
