from backtracking import backtracking
from FuerzaBruta import fuerzaBruta, posiblesSoluciones
from tkinter import *
from tkinter import messagebox
import copy
import time

#VENTANA PRINCIPAL
ventana = Tk()
ventana.geometry("700x900")
ventana.title("Proyecto: Domino")
ventana.resizable(False,False)
ventana.config(background="#212227")
titulo = Label(text = "Proyecto Domino", font = "Arial 20", bg = "#212227", fg = "white")
titulo.pack(pady = 10)

canvas = Canvas(width=400, height=300, bg='white')
canvas.pack(expand=YES, fill=BOTH)

#variable que almacena la matriz una vez generada
matrizBackup = ""
#canvas.create_rectangle(50, 50, 50 + 50, 50 + 50, fill="red")
#canvas.create_rectangle(100, 50, 150, 100, fill="blue") #aumentar label en x
#canvas.create_rectangle(50, 100, 100, 150, fill="green") #aumentar label en y 


def limpiarMatriz():
    """
    Funcionalidad: Elimina la matriz generada y resetea las funcionalidades del programa para poder ingresar nuevamente otra matriz
    Entradas: N/A
    Salidas: N/A
    """
    canvas.delete("all")
    entradaCont.config(state = "normal")
    boton1.config(state = "normal")
    entradaCont.delete(0, "end")
    boton2.config(state = "disable")
    seleccionCB.set('')
    drop['menu'].delete(0, 'end')
    boton3.config(state = "disable")
    entradaTiempo.config(state = "normal")
    entradaTiempo.delete(0, END)
    entradaTiempo.config(state = "disable")

def actualizarCB(opciones):
    """
    Funcionalidad: Actualiza las opciones de soluciones de la matriz generada, mostradas en la ComboBox
    Entradas: list opciones
    Salidas: N/A
    """
    for opcion in opciones:
        drop['menu'].add_command(label=opcion, command= lambda opAct = opcion: seleccionCB.set(opAct))
    seleccionCB.set(opciones[0])


def pintarMatriz(solucion, n, matriz):
    """
    Funcionalidad: Genera los cuadrados de la matriz que corresponden a las fichas generadas, con sus colores respectivos
    Entradas: string solucion, int n y list matriz
    Salidas: N/A
    """
    x = 0
    y = 0

    xPintar = 50
    yPintar = 50
    ancho = n + 2 #LA FORMA DE LA MATRIZ DE DOMINO EN LA INTERFAZ
    alto = n + 1
    aumento = 600 / ancho

    colores = ["red", "green", "blue", "cyan", "yellow", "magenta", "darkblue"]
    indiceColores = 0

    matrizTemp = copy.deepcopy(matriz)
    for posFicha in solucion: 
        if (indiceColores == 7):
            indiceColores = 0 
        while matrizTemp[x][y] == -1:
                y+=1
                xPintar += aumento
                if y >= (n+2):
                    y = 0
                    xPintar = 50
                    x += 1
                    yPintar += aumento
        if int(posFicha) == 0:
            fichaAct = (matriz[x][y], matriz[x][y+1])
            matrizTemp[x][y] = -1
            matrizTemp[x][y+1] = -1
            y+=2
            canvas.create_rectangle(xPintar, yPintar, xPintar + aumento, yPintar + aumento, fill=colores[indiceColores])
            canvas.create_rectangle(xPintar + aumento, yPintar, xPintar + aumento * 2, yPintar + aumento, fill=colores[indiceColores])
            xPintar += aumento * 2
        else:
            fichaAct = (matriz[x][y], matriz[x+1][y])
            matrizTemp[x][y] = -1
            matrizTemp[x+1][y] = -1
            y+=1
            canvas.create_rectangle(xPintar, yPintar, xPintar + aumento, yPintar + aumento, fill=colores[indiceColores])
            canvas.create_rectangle(xPintar, yPintar + aumento, xPintar + aumento , yPintar + aumento * 2, fill=colores[indiceColores])
            xPintar += aumento
        if y >= (n+2):
            y = 0
            xPintar = 50
            x += 1
            yPintar += aumento
        indiceColores += 1

def colocarNumeros(num, matriz):
    """
    Funcionalidad: Coloca los números respectivos de la matriz generada
    Entradas: int num y list matriz
    Salidas: N/A
    """
    x = 50  
    y = 50
    ancho = num + 2 #LA FORMA DE LA MATRIZ DE DOMINO EN LA INTERFAZ
    alto = num + 1
    aumento = 600 / ancho

    indiceTextX = 0
    indiceTextY = 0

    colores = ["red", "green", "blue", "cyan", "yellow", "magenta"]
    indiceColores = 0

    for i in range (0, ancho*alto):
        canvas.create_text(x+(aumento/2),y+(aumento/2),fill="black",font="Times 20 italic bold", text=str(matriz[indiceTextX][indiceTextY]))
        if (i+1)%ancho == 0:
            y += aumento
            x = 50
            indiceTextX += 1
            indiceTextY = 0
            
        else:
            x += aumento
            indiceTextY += 1

def generarMatriz():
    """
    Funcionalidad: Genera la matriz correspondiente a analizar. Llama al algoritmo correspondiente en función a la opción seleccionada por el usuario
    Entradas: N/A
    Salidas: N/A
    """
    try:
        num = int(entradaTablero.get())

        #SE GENERAN LAS SOLUCIONES DE LA MATRIZ, POS 0 CONTIENE LAS SOLUCIONES Y POS 1 LA MATRIZ
        if (opcionAlgoritmo.get() == 1):
            start = time.time() 
            infoMatriz = fuerzaBruta(num)
            end = time.time()
        elif (opcionAlgoritmo.get() == 2):
            start = time.time() 
            infoMatriz = backtracking(num)
            end = time.time()

        #SE REUTILIZARÁ LA MATRIZ EN PROCESOS POSTERIORES
        global matrizBackup
        matrizBackup = infoMatriz[1]

        #print(infoMatriz)
        #VERIFICA CASO ESPECIAL DEL GENERADOR DE LA MATRIZ TABLERO DOBLE N
        if infoMatriz[1] == False:
            messagebox.showerror("ERROR", "El algoritmo que genera la matriz de números\ngeneró un False.")
        else:
            #FUNCIÓN QUE PINTA LOS CUADRADOS DE LAS FICHAS
            pintarMatriz(infoMatriz[0][0], num, infoMatriz[1])
            #FUNCIÓN QUE COLOCA LOS NÚMEROS EN LOS CUADRADOS
            colocarNumeros(num, infoMatriz[1])
            
            #ACTUALIZA LOS VALORES DE LA COMBOBOX CON LAS NUEVAS SOLUCIONES
            actualizarCB(infoMatriz[0])

            #CONFIGURACIÓN DE LOS BOTONES Y ENTRADAS RESPECTIVA
            boton1.config(state= "disable")
            boton2.config(state = "normal")
            boton3.config(state = "normal")
            entradaCont.config(state= "disable")
            entradaTiempo.config(state = "normal")
            entradaTiempo.insert(END, str(end - start))
            entradaTiempo.config(state = "disable")
    except UnboundLocalError:
        messagebox.showerror("ERROR", "Debe seleccionar un algoritmo\npara buscar las posibles soluciones.")
    except ValueError:
        messagebox.showerror("ERROR", "Debe ingresar un número entero\npara definir el tamaño del tablero")
    
def seleccionarOpcion():
    """
    Funcionalidad: Actualiza la matriz generada en función a la solución a mostrar seleccionada por el usuario
    Entradas: N/A
    Salidas: N/A
    """
    canvas.delete("all")
    num = int(entradaTablero.get())
    print (seleccionCB.get())
    print(matrizBackup)
    pintarMatriz(seleccionCB.get(), num, matrizBackup)
    colocarNumeros(num, matrizBackup)


#BOTÓN RADIO

opcionAlgoritmo = IntVar()

R1 = Radiobutton(ventana, text="Fuerza Bruta", variable=opcionAlgoritmo, value=1)
R1.place(x = 40, y =858)

R2 = Radiobutton(ventana, text="Backtracking", variable=opcionAlgoritmo, value=2)
R2.place(x = 560, y =858)

#BOTONES
boton1 = Button(ventana, text="Generar Matriz", command = generarMatriz, width= "14", height= "2", bg= "#5FEDD5", font = "Arial 13")
boton1.place(x = 337, y = 725 )

boton2 = Button(ventana, text = "Reiniciar matriz", command = limpiarMatriz, width= "14", height= "2", bg= "#5FEDD5", font = "Arial 13")
boton2.place(x = 185, y = 725 )
boton2.config(state = "disable")

boton3 = Button(ventana, text = "Seleccionar solución", command = seleccionarOpcion, width= "17", height= "2", bg= "#5FEDD5", font = "Arial 13")
boton3.place(x = 489, y = 725 )
boton3.config(state = "disable")

#CAJAS DE TEXTO DE ENTRADA
entradaTablero = StringVar()
entradaCont = Entry(ventana, textvariable = entradaTablero, width = "5", font = ("Arial", "32"), bg= "#5FEDD5")
entradaCont.place(x = 45, y = 725)

tiempo = StringVar()
entradaTiempo = Entry(ventana, textvariable = tiempo, width = "20", font = ("Arial", "20"), bg= "#5FEDD5")
entradaTiempo.place(x = 300, y = 790)
entradaTiempo.config(state = "disable")

#COMBOBOX

seleccionCB = StringVar()
drop = OptionMenu(ventana, seleccionCB, "")
drop.pack(pady = 15)

#LABEL DE TEXTO

canvas.create_text(190, 750 ,fill="black",font="Times 20 italic bold", text="Tiempo durado: ")

#LLAMADA PARA INICIAR EL PROGRAMA
ventana.mainloop()