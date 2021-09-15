from CreateMatrix import create_puzzle

def binarizar(decimal):
    binario = ''
    while decimal // 2 != 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    return str(decimal) + binario

def agregarCeros(num, cantDigitos):
    numStr = str(num)
    while (len(numStr) < cantDigitos):
        numStr = "0" + numStr
    return numStr

def cantidadBits(n):
    num = (n+1)*(n+2)/2  ###### (n(n+1)/2) + n
    return num

def posiblesSoluciones(n):
    listaSoluciones = []
    i = 0
    m = 2**n
    while i != m:
        num = agregarCeros(binarizar(i), n)
        listaSoluciones.append(num)
        i+=1
    return listaSoluciones

def fuerzaBruta(n):
    #matriz = create_puzzle(n)                              #MATRIZ ALEATORIA
    matriz = [[0, 0, 0, 2], [2, 2, 1, 0],[2, 1, 1, 1]] 
    cBits = cantidadBits(n)
    #listaSoluciones = (posiblesSoluciones(cBits))          #TODAS LAS POSIBLES SOLUCIONES
    listaSoluciones = ["011000"]    
    listaSolucionesValid = []

    for solucionAct in listaSoluciones:
        x = 0
        y = 0
        matrizTemp = matriz
        try:
            solValida = True
            fichasUsadas = []
            for posFicha in solucionAct: 
                if int(posFicha) == 0:
                    if matrizTemp[x][y] == -1:
                        y+=1
                        if matriz[x][y] == -1:
                            y+=1
                        if y >= (n+2):
                            y = 0
                            x += 1
                    fichaAct = (matriz[x][y], matriz[x][y+1])
                    matrizTemp[x][y] = -1
                    matrizTemp[x][y+1] = -1
                    y+=2
                else:
                    if matrizTemp[x][y] == -1 or matrizTemp[x+1][y] == -1:
                        x+=1
                    fichaAct = (matriz[x][y], matriz[x+1][y])
                    matrizTemp[x][y] = -1
                    matrizTemp[x+1][y] = -1
                    y+=1
                if y >= (n+2):
                    y = 0
                    x += 1
                if fichaAct in fichasUsadas or (fichaAct[1],fichaAct[0]) in fichasUsadas:
                    solValida = False
                    print("Combinación inválida: " + solucionAct)
                    break
                fichasUsadas.append(fichaAct)
            if solValida:
                listaSolucionesValid.append(solucionAct)
        except:
            print("Combinación inválida: " + solucionAct)
    print("Soluciones válidas:\n\n\n")
    print(listaSolucionesValid)
        


fuerzaBruta(2)
#['000000', '000110', '001111', '011000', '011110', '011111', '101000', '101011', '101101', '101110', '101111']
#['000000', '000110', '001111', '011111']