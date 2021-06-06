from PIL import Image
import numpy as np

import pygame, math, random


global contador_gen, contador_fotos
contador_gen = 0
contador_fotos = 0

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


"""
def input(event):
    if event.type == pygame.QUIT:
        exit(0)
"""

#while True:
    #input(pygame.event.wait())



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

        lista_porcentajes.sort()

        lista_porcentajes_seleccionados = lista_porcentajes[3:]

        lista_mejores_arboles = []

        for elemento in lista:
            if(elemento[1] in lista_porcentajes_seleccionados):
                lista_mejores_arboles = lista_mejores_arboles + [elemento]

        print("Mejores arboles: ", lista_mejores_arboles)
        z -= 1



algoritmo_genetico()
