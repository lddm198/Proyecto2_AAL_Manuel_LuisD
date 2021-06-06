from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

global num_ram, ang_ram, prof, diam, decre


#Ventana Pricipal-----------------------------------------------------------------------------------

#Paleta de Colores:
# 1. d8e3e7
# 2. 51c4d3
# 3. 126e82
# 4. 132c33

def ven_prin(): # Ventana principal

    ven = Tk()
    ven.title("Árboles Genéticos")
    ven.iconbitmap('arbol.ico')
    ven.geometry('1300x910+300+15')
    ven.config(bg= '#d8e3e7')
    ven.resizable(width= False, height= False)

    #Labels de titulos y datos -------------------------------------------------------------------------------

    cont_gen = 1

    titu = Label(ven, text= "Árboles Genéticos", bg= "#51c4d3", fg= "#132c33", font=("Times", 24), padx= 40) #Label del titulo 
    titu.place(x= 480, y= 20)

    gen = Label(ven, text= "Generación 1", bg= "#d8e3e7", fg= "#132c33", font=("Times", 24), padx= 40) #La generación que se esta mostrando
    gen.place(x=510, y= 100)

    rami = Label(ven, text= "Número de Ramificaciones", bg= "#d8e3e7", fg= "#51c4d3", font=("Times", 14)) #Número de ramificaciones de esta generación
    rami.place(x= 85, y= 175)
    num_ram = Label(ven, text= "##", bg= "#d8e3e7", fg= "#132c33", font=("Times", 14))
    num_ram.place(x= 175, y= 200)

    angu = Label(ven, text= "Ángulo de las Ramificaciones", bg= "#d8e3e7", fg= "#51c4d3", font=("Times", 14)) #Ángulo de las ramificaciones
    angu.place(x= 370, y= 175)
    num_ang = Label(ven, text= "##°", bg= "#d8e3e7", fg= "#132c33", font=("Times", 14))
    num_ang.place(x= 465, y= 200)

    prof = Label(ven, text= "Profundidad", bg= "#d8e3e7", fg= "#51c4d3", font=("Times", 14)) #Profundidad del arbol
    prof.place(x= 665, y= 175)
    num_pla = Label(ven, text= "##", bg= "#d8e3e7", fg= "#132c33", font=("Times", 14))
    num_pla.place(x= 700, y= 200)

    diam = Label(ven, text= "Diámetro Tronco", bg= "#d8e3e7", fg= "#51c4d3", font=("Times", 14)) #Diámetro del tronco
    diam.place(x= 840, y= 175)
    num_dia = Label(ven, text= "##", bg= "#d8e3e7", fg= "#132c33", font=("Times", 14))
    num_dia.place(x= 890, y= 200)

    porc = Label(ven, text= "% Decremento Tronco", bg= "#d8e3e7", fg= "#51c4d3", font=("Times", 14)) #Porcentaje del decremento del tronco
    porc.place(x= 1045, y= 175)
    num_por = Label(ven, text= "##%", bg= "#d8e3e7", fg= "#132c33", font=("Times", 14))
    num_por.place(x= 1120, y= 200)

    #Imagenes de los árboles -------------------------------------------------------------------------------------

    imag1 = Image.open("Silueta.jpg")                 #Top 1 arbol con mayor % de parecido
    imag1 = imag1.resize((200, 200), Image.ANTIALIAS)
    arb1 = ImageTk.PhotoImage(imag1)
    label1 = Label(image = arb1)
    label1.image = arb1
    label1.place(x= 533, y= 250)

    imag2 = Image.open("Silueta.jpg")                 #Top 2 arbol con mayor % de parecido
    imag2 = imag2.resize((200, 200), Image.ANTIALIAS)
    arb2 = ImageTk.PhotoImage(imag2)
    label2 = Label(image = arb2)
    label2.image = arb2
    label2.place(x= 385, y= 480)

    imag3 = Image.open("Silueta.jpg")                #Top 3 arbol con mayor % de parecido
    imag3 = imag3.resize((200, 200), Image.ANTIALIAS)
    arb3 = ImageTk.PhotoImage(imag3)
    label3 = Label(image = arb3)
    label3.image = arb3
    label3.place(x= 685, y= 480)

    posX = 80
    cont = 4

    while cont <= 10:                                 #Ciclo para desplegar las 7 restantes
        imag = Image.open("num" +str(cont)+ ".png")
        imag = imag.resize((150, 150), Image.ANTIALIAS)
        arb = ImageTk.PhotoImage(imag)
        labelX = Label(image = arb)
        labelX.image = arb
        labelX.place(x= posX, y= 710)

        posX += 165
        cont += 1

    #Botones de siguiente y anterior ---------------------------------------------------------------------------------

    def atras():
        print("<")
        return

    def adelante():
        print(">")
        return

    photo1 = PhotoImage(file = "atras.png")   #Botón para ir atrás
    photoimage1 = photo1.subsample(1, 1)
    bot_ant = Button(ven, image = photoimage1, bg= "#d8e3e7", activebackground= "#d8e3e7", relief= GROOVE, command=atras)
    bot_ant.place(x= 100, y= 425)

    photo2 = PhotoImage(file = "adelante.png")   #Botón para ir adelante
    photoimage2 = photo2.subsample(1, 1)
    bot_ant = Button(ven, image = photoimage2, bg= "#d8e3e7", activebackground= "#d8e3e7", relief= GROOVE, command=adelante)
    bot_ant.place(x= 1095, y= 425)

    ven.mainloop()

ven_prin()