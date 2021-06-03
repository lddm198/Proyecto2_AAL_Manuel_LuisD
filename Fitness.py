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
            grosor = lista[4]
            grosor = int(round(lista[3]*(1-((grosor)/100)),0))
            x2 = x1 + int(math.cos(math.radians(angle)) * depth * base_len)
            y2 = y1 + int(math.sin(math.radians(angle)) * depth * base_len)
            pygame.draw.line(screen, (255,255,255), (x1, y1), (x2, y2), 2)

            #lista[4] = grosor

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

    print("Digite los rangos separados de un '-' y sin espacios por favor")
    print()
    num_ramificaciones = input("Digite el rango de ramificaciones que desea: ")
    angulo_ramificaciones = input("Digite el rango de los ángulos que desea: ")
    profundidad = int(input("Digite la profundidad del árbol que desea: "))
    long_diametro_tronco = int(input("Digite la longitud del diámetro del tronco que desea: "))
    proporcion_decremento_tronco = int(input("Digite la proporcion (%) de decremento del tronco en cada nivel que desea: "))

    num_ramificaciones = num_ramificaciones.split('-')
    angulo_ramificaciones = angulo_ramificaciones.split('-')

    lista_parametros = [num_ramificaciones, angulo_ramificaciones, profundidad, long_diametro_tronco, proporcion_decremento_tronco]


    drawTree(300, 550, -90, profundidad, lista_parametros)
    pygame.display.flip()
    pygame.image.save(screen, 'imagen.jpg')


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
w=0
for i in (data):
    if((data[w][0] != 255) and (data[w][1] != 255) and (data[w][2] != 255)):
        lista = data[w]
        break
    w+=1

print("Lista Data: ", lista)

w=0
for i in (data):
    if((data2[w][0] == 255) and (data2[w][1] == 255) and (data2[w][2] == 255)):
        lista = data2[w]
        break
    w+=1

print("Lista Data2: ", lista)
"""