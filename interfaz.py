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
x = 50
y = 50
"""
num = 10
ancho = 12
alto = 11
"""
num = 2         #FUTURA ENTRADA DEL USUARIO, DETERMINA EL ANCHO, ALTO Y AUMENTO PARA DEFINIR
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


clicked = StringVar()
clicked.set([listaSoluciones[0]])

drop = OptionMenu(ventana, clicked, *listaSoluciones)
drop.pack(pady = 15)

ventana.mainloop()