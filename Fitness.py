from PIL import Image
import numpy as np

import pygame, math, random

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

            if(grosor < 1):
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
    

fitness()


im = Image.open(r"C:\Users\XPC\Documents\TEC\Semestre 3\Análisis de Algoritmos\Proyecto 02\Silueta.jpg")
col,row =  im.size
data = np.zeros((row*col, 5))
pixels = im.load()
for i in range(row):
    for j in range(col):
        r,g,b =  pixels[i,j]
        data[i*col + j,:] = r,g,b,i,j

im = Image.open(r"C:\Users\XPC\Documents\TEC\Semestre 3\Análisis de Algoritmos\Proyecto 02\imagen.jpg")
col,row =  im.size
data2 = np.zeros((row*col, 5))
pixels = im.load()
for i in range(row):
    for j in range(col):
        r,g,b =  pixels[i,j]
        data2[i*col + j,:] = r,g,b,i,j


"""

print("Data: ")
print(data)

print("Data2: ")
print(data2)

contador = 0

w = 0

for i in (data):
    if(((data[w][0] != 255) and (data[w][1] != 255) and (data[w][2] != 255)) and ((data2[w][0] == 255) and (data2[w][1] == 255) and (data2[w][2] == 255))):
        contador+=1

    w+=1

print("Contador:", contador)
print((contador*100)/(600*600), "%")


"""

def algoritmo_genetico():
    pass







def poblacion_inicial():

    i = 0
    lista_return = []
    lista = []

    while i < 6:
        num_ramificaciones_1 = random.randint(1, 30)
        num_ramificaciones_2 = random.randint(31, 50)

        angulo_bajo = random.randint(1, 25)
        angulo_alto = random.randint(26,90)

        profundidad = random.randint(1, 20)

        long_diametro = random.randint(5, 20)

        porcentaje = random.randint(1, 100)

        lista_num = [num_ramificaciones_1, num_ramificaciones_2]
        lista_angulos = [angulo_bajo, angulo_alto]

        lista = [lista_num, lista_angulos, profundidad, long_diametro, porcentaje]

        lista_return = lista_return + [lista]

        i += 1
    
    return lista_return
