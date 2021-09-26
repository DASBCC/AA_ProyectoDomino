from CreateMatrix import create_puzzle
from funciones import *

def fuerzaBruta(n):
    """
    Funcionalidades: Algoritmo que prueba todas las posibles soluciones de fichas en una matriz de tamaño doble n
    Entradas: int n
    Salidas: list que contiene en la primera posición la lista de soluciones y en la segunda la matriz generada
    """
    matriz = create_puzzle(n)                              #MATRIZ ALEATORIA
    cBits = cantidadBits(n)
    print("Creacion de soluciones")
    listaSoluciones = (posiblesSoluciones(cBits))          #TODAS LAS POSIBLES SOLUCIONES
    listaSolucionesValid = []
    print("Inicio de corrida")
    for solucionAct in listaSoluciones:
        x = 0
        y = 0
        matrizTemp = copy.deepcopy(matriz)                 #MATRIZ TEMPORAL QUE AYUDARÁ A REGISTRAR LAS POSICIONES USADAS
        try:
            solValida = True
            fichasUsadas = []
            for posFicha in solucionAct: 
                while matrizTemp[x][y] == -1:           #SE COMPRUEBA SI LA POS ACTUAL FUE USADA
                        y+=1                            #DE SER ASÍ LA AUMENTA  
                        if y >= (n+2):                  #SI LLEGÓ AL LIMITE DE LA MATRIZ (ANCHURA) 
                            y = 0
                            x += 1                      #PASA A LA SIGUIENTE FILA
                if int(posFicha) == 0:                          #CASO FICHA HORIZONTAL
                    fichaAct = (matriz[x][y], matriz[x][y+1])
                    matrizTemp[x][y] = -1
                    matrizTemp[x][y+1] = -1
                    y+=2
                else:                                           #CASO FICHA VERTICAL
                    fichaAct = (matriz[x][y], matriz[x+1][y])
                    matrizTemp[x][y] = -1
                    matrizTemp[x+1][y] = -1
                    y+=1
                if y >= (n+2):                                  #COMPRUEBA SI SE LLEGÓ AL LÍMITE DE LA MATRIZ
                    y = 0
                    x += 1                                      #DE SER ASÍ AUMENTA FILA
                if fichaAct in fichasUsadas or (fichaAct[1],fichaAct[0]) in fichasUsadas:   #COMPRUEBA QUE LA FICHA NO HAYA SIDO USADA
                    solValida = False                                                       #SI YA SE USÓ, DESCARTA LA SOLUCIÓN ACTUAL
                fichasUsadas.append(fichaAct)
            if solValida:                                       #AL FINALIZAR LA REVISIÓN DE LA SOLUCIÓN, SI ES VÁLIDA LA AGREGA
                if verificarResultado(matrizTemp):              #A LA LISTA DE SOLUCIONES
                    listaSolucionesValid.append(solucionAct)
        except:
            ""
    print("Soluciones válidas:\n\n\n")
    print(listaSolucionesValid)
    return [listaSolucionesValid, matriz]