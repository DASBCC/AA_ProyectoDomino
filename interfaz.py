from FuerzaBruta import fuerzaBruta, posiblesSoluciones
from tkinter import *

#VENTANA PRINCIPAL
ventana = Tk()
ventana.geometry("700x800")
ventana.title("Proyecto: Domino")
ventana.resizable(False,False)
ventana.config(background="#212227")
titulo = Label(text = "Proyecto Domino", font = "Arial 20", bg = "#212227", fg = "white")
titulo.pack(pady = 10)

canvas = Canvas(width=400, height=300, bg='white')
canvas.pack(expand=YES, fill=BOTH)


def limpiarMatriz():
    canvas.delete("all")
    entradaCont.config(state = "normal")
    boton1.config(state = "normal")
    entradaCont.delete(0, "end")
    boton2.config(state = "disable")
    seleccionCB.set('')
    drop['menu'].delete(0, 'end')

def actualizarCB(opciones):
    # Reset var and delete all old options
    #seleccionCB.set('')
    #drop['menu'].delete(0, 'end')

    for opcion in opciones:
        drop['menu'].add_command(label=opcion, command= lambda opAct = opcion: seleccionCB.set(opAct))
    seleccionCB.set(opciones[0])


def generarMatriz():
    num = int(entradaTablero.get())
    x = 50
    y = 50
    ancho = num + 2 #LA FORMA DE LA MATRIZ DE DOMINO EN LA INTERFAZ
    alto = num + 1
    aumento = 600 / ancho

    for i in range (0, ancho*alto):
        canvas.create_rectangle(x, y, x + aumento, y + aumento, fill='red')
        #if x == 600:
        if (i+1)%ancho == 0:
            y += aumento
            x = 50
        else:
            x += aumento


    listaSoluciones = fuerzaBruta(2)

    
    
    #clicked.set([listaSoluciones[0]])

    #drop = OptionMenu(ventana, clicked, *listaSoluciones)
    #drop.pack(pady = 15)
    #seleccionCB.set(listaSoluciones[0])
    
    actualizarCB(listaSoluciones)

    boton1.config(state= "disable")
    boton2.config(state = "normal")
    entradaCont.config(state= "disable")
    



boton1 = Button(ventana, text="Generar Matriz", command = generarMatriz, width= "15", height= "2", bg= "#5FEDD5", font = "Arial 13")
boton1.place(x = 475, y = 625 )

boton2 = Button(ventana, text = "Reiniciar matriz", command = limpiarMatriz, width= "15", height= "2", bg= "#5FEDD5", font = "Arial 13")
boton2.place(x = 265, y = 625 )
boton2.config(state = "disable")

entradaTablero = StringVar()
entradaCont = Entry(ventana, textvariable = entradaTablero, width = "5", font = ("Arial", "32"), bg= "#5FEDD5")
entradaCont.place(x = 80, y = 625)


seleccionCB = StringVar()
drop = OptionMenu(ventana, seleccionCB, "")
drop.pack(pady = 15)




ventana.mainloop()