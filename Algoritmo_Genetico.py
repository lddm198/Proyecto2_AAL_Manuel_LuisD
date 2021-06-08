from tkinter import *
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import numpy as np
import pygame, math, random

global num_ram, ang_ram, prof, diam, decre, contador_gen, contador_fotos

#Algoritmo Genético --------------------------------------------------------------------------------

contador_gen = 0
contador_fotos = 0
lista_generaciones = []

pygame.init()
window = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Fractal Tree")
screen = pygame.display.get_surface()

def drawTree(x1, y1, angle, depth, lista):
    lista=lista
    fork_angle = random.randint(int(lista[1][0]), int(lista[1][1]))
    base_len = random.randint(6, 12)
    num_ramificaciones = random.randint(int(lista[0][0]), int(lista[0][1]))

    if depth > 0:

        if(depth == lista[2]):
            x2 = x1 + int(math.cos(math.radians(angle)) * depth * base_len)
            y2 = y1 + int(math.sin(math.radians(angle)) * depth * base_len)
            pygame.draw.line(screen, (255,255,255), (x1, y1), (x2, y2), lista[3])
            for x in range(num_ramificaciones):
                rdm = random.random()
                if(rdm >= 0.5):
                    fork_angle = random.randint(int(lista[1][0]), int(lista[1][1]))
                    drawTree(x2, y2, angle + fork_angle, depth - 1, lista)
                else:
                    fork_angle = random.randint(int(lista[1][0]), int(lista[1][1]))
                    drawTree(x2, y2, angle - fork_angle, depth - 1, lista)

        else:
            proporcion = lista[4]
            grosor = int(round(lista[3]*(1-((proporcion)/100)),0))

            if(grosor <= 1):
                grosor = 1

            x2 = x1 + int(math.cos(math.radians(angle)) * depth * base_len)
            y2 = y1 + int(math.sin(math.radians(angle)) * depth * base_len)
            pygame.draw.line(screen, (255,255,255), (x1, y1), (x2, y2), grosor)

            lista[3] = grosor

            for x in range(num_ramificaciones):
                rdm = random.random()
                if(rdm >= 0.5):
                    fork_angle = random.randint(int(lista[1][0]), int(lista[1][1]))
                    drawTree(x2, y2, angle + fork_angle, depth - 1, lista)
                else:
                    fork_angle = random.randint(int(lista[1][0]), int(lista[1][1]))
                    drawTree(x2, y2, angle - fork_angle, depth - 1, lista)

def fitness():
    #Esta es la función Fitness donde se puede parametrizar los árboles

    while True:

        try:
            print("Digite los rangos separados de un '-' y sin espacios por favor")
            print()
            num_ramificaciones = input("Digite el rango de ramificaciones que desea: ")
            angulo_ramificaciones = input("Digite el rango de los ángulos que desea: ") 
            profundidad = int(input("Digite la profundidad del árbol que desea: "))
            long_diametro_tronco = int(input("Digite la longitud del diámetro del tronco que desea: "))
            proporcion_decremento_tronco = int(input("Digite la proporcion (%) de decremento del tronco en cada nivel que desea: "))

            num_ramificaciones = num_ramificaciones.split('-') 
            angulo_ramificaciones = angulo_ramificaciones.split('-')

        except ValueError:
            print("Uno de los datos ingresado no es valido")
            print("Vuelva a intentarlo porfavor")
            print()
            continue

        lista_parametros = [num_ramificaciones, angulo_ramificaciones, profundidad, long_diametro_tronco, proporcion_decremento_tronco]

        drawTree(300, 550, -90, profundidad, lista_parametros)
        pygame.display.flip()
        pygame.image.save(screen, 'imagen.jpg')
        break

def fitness_aux(lista_parametros):
    global contador_gen, contador_fotos
    #Esta es la función Fitness donde se puede parametrizar los árboles

    drawTree(300, 550, -90, lista_parametros[2], lista_parametros)
    pygame.display.flip()
    pygame.image.save(screen, 'imagen{}{}.jpg'.format(contador_gen, contador_fotos))
    screen.fill((0,0,0))

    im = Image.open("Silueta.jpg")
    col,row =  im.size
    data = np.zeros((row*col, 5))
    pixels = im.load()
    for i in range(row):
        for j in range(col):
            r,g,b =  pixels[i,j]
            data[i*col + j,:] = r,g,b,i,j

    im = Image.open("imagen{}{}.jpg".format(contador_gen, contador_fotos))
    col,row =  im.size
    data2 = np.zeros((row*col, 5))
    pixels = im.load()
    for i in range(row):
        for j in range(col):
            r,g,b =  pixels[i,j]
            data2[i*col + j,:] = r,g,b,i,j

    contador = 0

    w = 0

    print("ARBOL imagen{}{}".format(contador_gen, contador_fotos))

    for i in (data):
        if(((data[w][0] != 255) and (data[w][1] != 255) and (data[w][2] != 255)) and ((data2[w][0] == 255) and (data2[w][1] == 255) and (data2[w][2] == 255))):
            contador+=1

        w+=1

    print("Contador:", contador)
    print((contador*100)/(600*600), "%")
    porcentaje = (contador*100)/(600*600)
    print("============================================")

    contador_fotos += 1
    return [lista_parametros ,porcentaje]

def poblacion_inicial():

    i = 0
    lista_return = []
    lista = []

    while i < 6:
        num_ramificaciones_1 = random.randint(1, 3)
        num_ramificaciones_2 = random.randint(4, 5)

        angulo_bajo = random.randint(1, 25)
        angulo_alto = random.randint(26,45)

        profundidad = random.randint(5, 9)

        long_diametro = random.randint(6, 10)

        porcentaje = random.randint(10, 49)

        lista_num = [num_ramificaciones_1, num_ramificaciones_2]
        lista_angulos = [angulo_bajo, angulo_alto]

        lista = [lista_num, lista_angulos, profundidad, long_diametro, porcentaje]

        lista_return = lista_return + [lista]

        i += 1
    
    return lista_return

def nueva_generacion(lista_arboles):

    arbol1 = lista_arboles[0][0]
    arbol2 = lista_arboles[1][0]
    arbol3 = lista_arboles[2][0]

    lista = []
    lista_return = []

    i = 0
    while i < 6:
        rng1 = random.randint(0,2)
        rng2 = random.randint(0,2)
        rng3 = random.randint(0,2)
        rng4 = random.randint(0,2)
        rng5 = random.randint(0,2)

        rng_mutacion = random.random()

        nuevo_arbol = [lista_arboles[rng1][0][0], lista_arboles[rng2][0][1], lista_arboles[rng3][0][2], lista_arboles[rng4][0][3],lista_arboles[rng5][0][4]]

        if(rng_mutacion < 0.05):
            rng_cromosoma = random.randint(0,4)
            if(rng_cromosoma == 0):
                nuevo_arbol[rng_cromosoma] = [random.randint(1,3), random.randint(4,7)]      
            elif(rng_cromosoma == 1):
                nuevo_arbol[rng_cromosoma] = [random.randint(10,15), random.randint(16,35)]
            elif(rng_cromosoma == 2):
                nuevo_arbol[rng_cromosoma] = random.randint(5, 9)
            elif(rng_cromosoma == 3):
                nuevo_arbol[rng_cromosoma] = random.randint(6, 10)
            elif(rng_cromosoma == 4):
                nuevo_arbol[rng_cromosoma] = random.randint(10, 49)

        if nuevo_arbol in lista:
            continue
        else:
            lista = lista + [nuevo_arbol]

        i += 1

    return lista

def algoritmo_genetico():
    global contador_gen, contador_fotos
    poblacion_inicial_ = poblacion_inicial()

    lista_porcentajes = []
    lista = []

    print("POBLACION INICIAL: ", poblacion_inicial_)
    w = 0
    for arbol in poblacion_inicial_:
        lista = lista + [fitness_aux(arbol)]
        lista_porcentajes = lista_porcentajes + [lista[w][1]]
        w+=1
    contador_fotos = 0
    contador_gen += 1

    lista_generaciones.append(lista)
    
    lista_porcentajes.sort()

    lista_porcentajes_seleccionados = lista_porcentajes[3:]

    lista_mejores_arboles = []

    for elemento in lista:
        if(elemento[1] in lista_porcentajes_seleccionados):
            lista_mejores_arboles = lista_mejores_arboles + [elemento]

    print("Mejores arboles: ", lista_mejores_arboles)
    z = 7
    while z > 0:
        print("Generacion: ", contador_gen)
        lista_porcentajes = []
        lista = []

        nueva_gen = nueva_generacion(lista_mejores_arboles)
        w = 0
        for arbol in nueva_gen:
            lista = lista + [fitness_aux(arbol)]
            lista_porcentajes = lista_porcentajes + [lista[w][1]]
            w += 1
        contador_fotos = 0
        contador_gen += 1

        lista_generaciones.append(lista)

        lista_porcentajes.sort()

        lista_porcentajes_seleccionados = lista_porcentajes[3:]

        lista_mejores_arboles = []

        for elemento in lista_porcentajes_seleccionados:
            if elemento > 25:
                flag = True
                break
            else:
                flag = False

        if flag == True:
            break

        for elemento in lista:
            if(elemento[1] in lista_porcentajes_seleccionados):
                lista_mejores_arboles = lista_mejores_arboles + [elemento]

        print("Mejores arboles: ", lista_mejores_arboles)
        z -= 1

algoritmo_genetico()

#Ventana Pricipal-----------------------------------------------------------------------------------

#Paleta de Colores:
# 1. d8e3e7
# 2. 51c4d3
# 3. 126e82
# 4. 132c33

def ven_prin(): # Ventana principal
 
    ven = Tk()
    ven.title("Árboles Genéticos")
    ven.iconbitmap('logo_arbol.ico')
    ven.geometry('1300x910+300+15')
    ven.config(bg= '#d8e3e7')
    ven.resizable(width= False, height= False)

    global cont_gen, lis_num, lis_ang, lis_pro, lis_dia, lis_dec

    cont_gen = 0

    prim_gen = lista_generaciones[0]
    prim_gen.sort(reverse = True, key = lambda prim_gen: prim_gen[1])

    lis_num = ["##-##"]
    lis_ang = ["##°-##°"]
    lis_pro = ["##"]
    lis_dia = ["##"]
    lis_dec = ["##%"]

    for arbol in prim_gen:
        lis_num.append(str(arbol[0][0][0])+"-"+str(arbol[0][0][1]))
        lis_ang.append(str(arbol[0][1][0])+"°-"+str(arbol[0][1][1])+"°")
        lis_pro.append(str(arbol[0][2]))
        lis_dia.append(str(arbol[0][3]))
        lis_dec.append(str(arbol[0][4])+"%")
        

    #Labels de titulos y datos -------------------------------------------------------------------------------

    titu = Label(ven, text= "Árboles Genéticos", bg= "#51c4d3", fg= "#132c33", font=("Times", 24), padx= 40) #Label del titulo 
    titu.place(x= 480, y= 20)

    gen = Label(ven, text= "Generación 0", bg= "#d8e3e7", fg= "#132c33", font=("Times", 24), padx= 40) #La generación que se esta mostrando
    gen.place(x=510, y= 100)

    rami = Label(ven, text= "Número de Ramificaciones", bg= "#d8e3e7", fg= "#51c4d3", font=("Times", 14)) #Número de ramificaciones de esta generación
    rami.place(x= 85, y= 175)
    var_ram = StringVar(ven)
    num_ram = ttk.OptionMenu(ven, var_ram, *lis_num)
    num_ram.place(x= 150, y= 200)

    angu = Label(ven, text= "Ángulo de las Ramificaciones", bg= "#d8e3e7", fg= "#51c4d3", font=("Times", 14)) #Ángulo de las ramificaciones
    angu.place(x= 370, y= 175)
    var_ang = StringVar(ven)
    num_ang = ttk.OptionMenu(ven, var_ang, *lis_ang)
    num_ang.place(x= 437, y= 200)

    prof = Label(ven, text= "Profundidad", bg= "#d8e3e7", fg= "#51c4d3", font=("Times", 14)) #Profundidad del arbol
    prof.place(x= 665, y= 175)
    var_pro = StringVar(ven)
    num_pro = ttk.OptionMenu(ven, var_pro, *lis_pro)
    num_pro.place(x= 690, y= 200)

    diam = Label(ven, text= "Diámetro Tronco", bg= "#d8e3e7", fg= "#51c4d3", font=("Times", 14)) #Diámetro del tronco
    diam.place(x= 840, y= 175)
    var_dia = StringVar(ven)
    num_dia = ttk.OptionMenu(ven, var_dia, *lis_dia)
    num_dia.place(x= 880, y= 200)

    porc = Label(ven, text= "% Decremento Tronco", bg= "#d8e3e7", fg= "#51c4d3", font=("Times", 14)) #Porcentaje del decremento del tronco
    porc.place(x= 1045, y= 175)
    var_por = StringVar(ven)
    num_por = ttk.OptionMenu(ven, var_por, *lis_dec)
    num_por.place(x= 1105, y= 200)

    #Imagenes de los árboles -------------------------------------------------------------------------------------

    def imagenes():
        global cont_gen

        imag1 = Image.open("imagen"+ str(cont_gen) +"0.jpg")                 
        imag1 = imag1.resize((200, 200), Image.ANTIALIAS)
        arb1 = ImageTk.PhotoImage(imag1)
        label1 = Label(image = arb1)
        label1.image = arb1
        label1.place(x= 533, y= 250)

        imag2 = Image.open("imagen"+ str(cont_gen) +"1.jpg")                
        imag2 = imag2.resize((200, 200), Image.ANTIALIAS)
        arb2 = ImageTk.PhotoImage(imag2)
        label2 = Label(image = arb2)
        label2.image = arb2
        label2.place(x= 385, y= 480)

        imag3 = Image.open("imagen"+ str(cont_gen) +"2.jpg")               
        imag3 = imag3.resize((200, 200), Image.ANTIALIAS)
        arb3 = ImageTk.PhotoImage(imag3)
        label3 = Label(image = arb3)
        label3.image = arb3
        label3.place(x= 685, y= 480)

        posX = 300
        cont = 3
        tot = len(prim_gen)

        while cont < tot:                                 #Ciclo para desplegar las 7 restantes
            imag = Image.open("imagen"+ str(cont_gen) + str(cont) +".jpg")
            imag = imag.resize((160, 160), Image.ANTIALIAS)
            arb = ImageTk.PhotoImage(imag)
            labelX = Label(image = arb)
            labelX.image = arb
            labelX.place(x= posX, y= 710)

            posX += 257
            cont += 1

    imagenes()

    #Botones de siguiente y anterior ---------------------------------------------------------------------------------

    def atras():
        global cont_gen, lis_num, lis_ang, lis_pro, lis_dia, lis_dec

        bot_ade.config(state= NORMAL)
        cont_gen -= 1
        gen.config(text="Generación "+str(cont_gen))

        lis_num = ["##-##"]
        lis_ang = ["##°-##°"]
        lis_pro = ["##"]
        lis_dia = ["##"]
        lis_dec = ["##%"]

        gen_act = lista_generaciones[cont_gen]

        for arbol in gen_act:
            lis_num.append(str(arbol[0][0][0])+"-"+str(arbol[0][0][1]))
            lis_ang.append(str(arbol[0][1][0])+"°-"+str(arbol[0][1][1])+"°")
            lis_pro.append(str(arbol[0][2]))
            lis_dia.append(str(arbol[0][3]))
            lis_dec.append(str(arbol[0][4])+"%")

        num_ram = ttk.OptionMenu(ven, var_ram, *lis_num)
        num_ram.place(x= 150, y= 200)
        num_ang = ttk.OptionMenu(ven, var_ang, *lis_ang)
        num_ang.place(x= 437, y= 200)
        num_pro = ttk.OptionMenu(ven, var_pro, *lis_pro)
        num_pro.place(x= 690, y= 200)
        num_dia = ttk.OptionMenu(ven, var_dia, *lis_dia)
        num_dia.place(x= 880, y= 200)
        num_por = ttk.OptionMenu(ven, var_por, *lis_dec)
        num_por.place(x= 1105, y= 200)

        imagenes()
        
        if(cont_gen-1 == -1):
            bot_ant.config(state= DISABLED)

        return

    def adelante():
        global cont_gen, lis_num, lis_ang, lis_pro, lis_dia, lis_dec

        bot_ant.config(state= NORMAL)
        cont_gen += 1
        gen.config(text="Generación "+str(cont_gen))

        lis_num = ["##-##"]
        lis_ang = ["##°-##°"]
        lis_pro = ["##"]
        lis_dia = ["##"]
        lis_dec = ["##%"]

        gen_act = lista_generaciones[cont_gen]

        for arbol in gen_act:
            lis_num.append(str(arbol[0][0][0])+"-"+str(arbol[0][0][1]))
            lis_ang.append(str(arbol[0][1][0])+"°-"+str(arbol[0][1][1])+"°")
            lis_pro.append(str(arbol[0][2]))
            lis_dia.append(str(arbol[0][3]))
            lis_dec.append(str(arbol[0][4])+"%")

        num_ram = ttk.OptionMenu(ven, var_ram, *lis_num)
        num_ram.place(x= 150, y= 200)
        num_ang = ttk.OptionMenu(ven, var_ang, *lis_ang)
        num_ang.place(x= 437, y= 200)
        num_pro = ttk.OptionMenu(ven, var_pro, *lis_pro)
        num_pro.place(x= 690, y= 200)
        num_dia = ttk.OptionMenu(ven, var_dia, *lis_dia)
        num_dia.place(x= 880, y= 200)
        num_por = ttk.OptionMenu(ven, var_por, *lis_dec)
        num_por.place(x= 1105, y= 200)

        imagenes()

        if(cont_gen+1 == len(lista_generaciones)):
            bot_ade.config(state= DISABLED)

        return

    photo1 = PhotoImage(file = "atras.png")   #Botón para ir atrás
    photoimage1 = photo1.subsample(1, 1)
    bot_ant = Button(ven, image = photoimage1, bg= "#d8e3e7", activebackground= "#d8e3e7", relief= GROOVE, state= DISABLED, command=atras)
    bot_ant.place(x= 100, y= 425)

    photo2 = PhotoImage(file = "adelante.png")   #Botón para ir adelante
    photoimage2 = photo2.subsample(1, 1)
    bot_ade = Button(ven, image = photoimage2, bg= "#d8e3e7", activebackground= "#d8e3e7", relief= GROOVE, command=adelante)
    bot_ade.place(x= 1095, y= 425)

    ven.mainloop()

ven_prin()