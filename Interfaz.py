from tkinter import *
from tkinter import messagebox

global num_ram, ang_ram, prof, diam, decre


#Ventana Pricipal-----------------------------------------------------------------------------------

#Paleta de Colores:
# 1. d8e3e7
# 2. 51c4d3
# 3. 126e82
# 4. 132c33

def ven_prin(): # ventana principal
    #Ventana principal

    ven = Tk()
    ven.title("Árboles Genéticos")
    ven.iconbitmap('arbol.ico')
    ven.geometry('1000x720+250+35')
    ven.config(bg= '#d8e3e7')
    ven.resizable(width= False, height= False)

    titu = Label(ven, text= "Árboles Genéticos", bg= "#51c4d3", fg= "#132c33", font=("Times", 24), padx= 40)
    titu.place(x= 350, y= 20)

    gen = Label(ven, text= "Generación #", bg= "#d8e3e7", fg= "#132c33", font=("Times", 24), padx= 40)
    gen.place(x= 380, y= 120)

    rami = Label(ven, text= "Número de Ramificaciones", bg= "#d8e3e7", fg= "#51c4d3", font=("Times", 14))
    rami.place(x= 30, y= 175)
    num_ram = Label(ven, text= "##", bg= "#d8e3e7", fg= "#132c33", font=("Times", 14))
    num_ram.place(x= 115, y= 200)

    angu = Label(ven, text= "Ángulo de las Ramificaciones", bg= "#d8e3e7", fg= "#51c4d3", font=("Times", 14))
    angu.place(x= 260, y= 175)
    num_ang = Label(ven, text= "##°", bg= "#d8e3e7", fg= "#132c33", font=("Times", 14))
    num_ang.place(x= 357, y= 200)

    prof = Label(ven, text= "Profundidad", bg= "#d8e3e7", fg= "#51c4d3", font=("Times", 14))
    prof.place(x= 510, y= 175)
    num_pla = Label(ven, text= "##", bg= "#d8e3e7", fg= "#132c33", font=("Times", 14))
    num_pla.place(x= 545, y= 200)

    diam = Label(ven, text= "Diámetro Tronco", bg= "#d8e3e7", fg= "#51c4d3", font=("Times", 14))
    diam.place(x= 635, y= 175)
    num_dia = Label(ven, text= "##", bg= "#d8e3e7", fg= "#132c33", font=("Times", 14))
    num_dia.place(x= 685, y= 200)

    porc = Label(ven, text= "% Decremento Tronco", bg= "#d8e3e7", fg= "#51c4d3", font=("Times", 14))
    porc.place(x= 790, y= 175)
    num_por = Label(ven, text= "##%", bg= "#d8e3e7", fg= "#132c33", font=("Times", 14))
    num_por.place(x= 855, y= 200)

    ven.mainloop()

ven_prin()