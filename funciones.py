import copy
import time 

def binarizar(decimal):
    """
    Funcionalidades: Convierte un numero a su forma binaria
    Entradas: int decimal
    Salidas: string con el número convertido a binario
    """
    binario = ''
    while decimal // 2 != 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    return str(decimal) + binario

def agregarCeros(num, cantDigitos):
    """
    Funcionalidades: Agrega los 0 a la izquierda faltantes en función a la cantidad de bits original del número
    Entradas: int num, int cantDigitos
    Salidas: string con el número final
    """
    numStr = str(num)
    while (len(numStr) < cantDigitos):
        numStr = "0" + numStr
    return numStr

def cantidadBits(n):
    """
    Funcionalidades: Determina la cantidad de fichas y por ende la cantidad de bits, dependiendo del tamaño del tablero
    Entradas: int n
    Salidas: int num
    """
    num = (n+1)*(n+2)/2  ###### (n(n+1)/2) + n
    return num

def posiblesSoluciones(n):
    """
    Funcionalidades: Genera todos los números binarios definidos por el tamaño del tablero
    Entradas: int n
    Salidas: list listaSoluciones
    """
    listaSoluciones = []
    i = 0
    m = 2**n
    while i != m:
        num = agregarCeros(binarizar(i), n)
        listaSoluciones.append(num)
        i+=1
    return listaSoluciones


def verificarResultado(matriz):
    """
    Funcionalidades: Verifica que la matriz temporal haya utilizado todas las posiciones, es decir, todos se hayan vuelto -1
    Entradas: list matriz
    Salidas: boolean True/False, true si se utilizaron todas las posiciones y false si no
    """
    for i in matriz:
        for j in i:
            if j != -1:
                return False
    return True