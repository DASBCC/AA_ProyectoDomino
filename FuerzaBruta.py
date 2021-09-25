from CreateMatrix import create_puzzle
import copy
import time 

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

def crearMatrizTemp(matriz):
    matrizTemp = []
    for i in matriz:
        temp = i
        matrizTemp.append(temp)
    return matrizTemp

def verificarResultado(matriz):
    for i in matriz:
        for j in i:
            if j != -1:
                return False
    return True

def fuerzaBruta(n):
    matriz = create_puzzle(n)                              #MATRIZ ALEATORIA
    #matriz = [[0, 0, 0, 2], [2, 2, 1, 0],[2, 1, 1, 1]]  #DOBLE 2
    #matriz = [[2,0,0,0,2], [0,3,1,0,1], [2,3,1,1,3], [3,1,2,2,3]]  #DOBLE 3
    #matriz = [[0,1,1,4,0,3], [1,4,0,4,4,3], [3,3,2,3,1,3], [0,4,2,2,1,2], [0,0,4,1,2,2]]  #DOBLE 4
    cBits = cantidadBits(n)
    print("Creacion de soluciones")
    listaSoluciones = (posiblesSoluciones(cBits))          #TODAS LAS POSIBLES SOLUCIONES
    #listaSoluciones = ["000110", "011110"]    CORRECTAS
    #listaSoluciones = ["011110"] #CORRECTA     DOBLE 2
    #listaSoluciones = ["011100"]  #ERRONEA      DOBLE 2
    #listaSoluciones = ["0010000100"]       #CORRECTA    DOBLE 3
    #listaSoluciones = ["101111111001100"]   #   CORRECTA    DOBLE4
    listaSolucionesValid = []
    print("Inicio de corrida")
    for solucionAct in listaSoluciones:
        x = 0
        y = 0
        matrizTemp = copy.deepcopy(matriz)
        #matrizTemp = matriz
        try:
            solValida = True
            fichasUsadas = []
            for posFicha in solucionAct: 
                while matrizTemp[x][y] == -1:
                        y+=1
                        #if matrizTemp[x][y] == -1:
                        #    y+=1
                        if y >= (n+2):
                            y = 0
                            x += 1
                if int(posFicha) == 0:
                    """
                    if matrizTemp[x][y] == -1:
                        y+=1
                        if matrizTemp[x][y] == -1:
                            y+=1
                        if y >= (n+2):
                            y = 0
                            x += 1
                    """
                    #while matrizTemp[x][y] == -1:
                    #    y+=1
                        #if matrizTemp[x][y] == -1:
                        #    y+=1
                    #    if y >= (n+2):
                    #        y = 0
                    #        x += 1
                    fichaAct = (matriz[x][y], matriz[x][y+1])
                    matrizTemp[x][y] = -1
                    matrizTemp[x][y+1] = -1
                    y+=2
                else:
                    #if matrizTemp[x][y] == -1 or matrizTemp[x+1][y] == -1:
                    #    x+=1
                    fichaAct = (matriz[x][y], matriz[x+1][y])
                    matrizTemp[x][y] = -1
                    matrizTemp[x+1][y] = -1
                    y+=1
                if y >= (n+2):
                    y = 0
                    x += 1
                if fichaAct in fichasUsadas or (fichaAct[1],fichaAct[0]) in fichasUsadas:
                    solValida = False     
                fichasUsadas.append(fichaAct)
            if solValida:
                if verificarResultado(matrizTemp):
                    listaSolucionesValid.append(solucionAct)
        except:
            ""
    print("Soluciones válidas:\n\n\n")
    print(listaSolucionesValid)
    return [listaSolucionesValid, matriz]
        

start = time.time() 
#fuerzaBruta(6)
end = time.time()
print("Time elapsed during the calculation:", end - start)
#create_puzzle(10)
#['000000', '000110', '001111', '011000', '011110', '011111', '101000', '101011', '101101', '101110', '101111']
#['000000', '000110', '001111', '011111']
