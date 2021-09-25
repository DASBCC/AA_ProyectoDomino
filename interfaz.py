from FuerzaBruta import fuerzaBruta, posiblesSoluciones
from tkinter import *
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

#variable que almacena la matriz mientras no se genere una nueva matriz
matrizBackup = ""
#canvas.create_rectangle(50, 50, 50 + 50, 50 + 50, fill="red")
#canvas.create_rectangle(100, 50, 150, 100, fill="blue") #aumentar label en x
#canvas.create_rectangle(50, 100, 100, 150, fill="green") #aumentar label en y 


def limpiarMatriz():
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
    # Reset var and delete all old options
    #seleccionCB.set('')
    #drop['menu'].delete(0, 'end')

    for opcion in opciones:
        drop['menu'].add_command(label=opcion, command= lambda opAct = opcion: seleccionCB.set(opAct))
    seleccionCB.set(opciones[0])


def pintarMatriz(solucion, n, matriz):
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

    num = int(entradaTablero.get())

    #SE GENERAN LAS SOLUCIONES DE LA MATRIZ, POS 0 CONTIENE LAS SOLUCIONES Y POS 1 LA MATRIZ
    start = time.time() 
    infoMatriz = fuerzaBruta(num)
    end = time.time()

    global matrizBackup
    matrizBackup = infoMatriz[1]

    print(infoMatriz)

    pintarMatriz(infoMatriz[0][0], num, infoMatriz[1])

    colocarNumeros(num, infoMatriz[1])
    
    #clicked.set([listaSoluciones[0]])

    #drop = OptionMenu(ventana, clicked, *listaSoluciones)
    #drop.pack(pady = 15)
    #seleccionCB.set(listaSoluciones[0])
    
    actualizarCB(infoMatriz[0])

    boton1.config(state= "disable")
    boton2.config(state = "normal")
    boton3.config(state = "normal")
    entradaCont.config(state= "disable")
    entradaTiempo.config(state = "normal")
    entradaTiempo.insert(END, str(end - start))
    entradaTiempo.config(state = "disable")
    
def seleccionarOpcion():
    canvas.delete("all")
    
    num = int(entradaTablero.get())
    print (seleccionCB.get())
    print(matrizBackup)
    pintarMatriz(seleccionCB.get(), num, matrizBackup)
    colocarNumeros(num, matrizBackup)


boton1 = Button(ventana, text="Generar Matriz", command = generarMatriz, width= "14", height= "2", bg= "#5FEDD5", font = "Arial 13")
boton1.place(x = 337, y = 725 )

boton2 = Button(ventana, text = "Reiniciar matriz", command = limpiarMatriz, width= "14", height= "2", bg= "#5FEDD5", font = "Arial 13")
boton2.place(x = 185, y = 725 )
boton2.config(state = "disable")

boton3 = Button(ventana, text = "Seleccionar solución", command = seleccionarOpcion, width= "17", height= "2", bg= "#5FEDD5", font = "Arial 13")
boton3.place(x = 489, y = 725 )
boton3.config(state = "disable")

entradaTablero = StringVar()
entradaCont = Entry(ventana, textvariable = entradaTablero, width = "5", font = ("Arial", "32"), bg= "#5FEDD5")
entradaCont.place(x = 45, y = 725)


seleccionCB = StringVar()
drop = OptionMenu(ventana, seleccionCB, "")
drop.pack(pady = 15)

canvas.create_text(190, 750 ,fill="black",font="Times 20 italic bold", text="Tiempo durado: ")
tiempo = StringVar()
entradaTiempo = Entry(ventana, textvariable = tiempo, width = "20", font = ("Arial", "20"), bg= "#5FEDD5")
entradaTiempo.place(x = 300, y = 790)
entradaTiempo.config(state = "disable")


ventana.mainloop()