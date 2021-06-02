from PIL import Image
import numpy as np

import pygame, math, random

pygame.init()
window = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Fractal Tree")
screen = pygame.display.get_surface()

def drawTree(x1, y1, angle, depth):
    fork_angle = random.randint(10, 25)
    fork_angle2 = random.randint(10, 25)
    base_len = random.randint(6, 12)

    if depth > 0:

        if (depth >= 7):
            x2 = x1 + int(math.cos(math.radians(angle)) * depth * base_len)
            y2 = y1 + int(math.sin(math.radians(angle)) * depth * base_len)
            pygame.draw.line(screen, (255,255,255), (x1, y1), (x2, y2), 5)
            drawTree(x2, y2, angle + fork_angle2, depth - 1)
            drawTree(x2, y2, angle - fork_angle, depth - 1)

        else:

            base_len = random.randint(6, 9)
            x2 = x1 + int(math.cos(math.radians(angle)) * depth * base_len)
            y2 = y1 + int(math.sin(math.radians(angle)) * depth * base_len)
            pygame.draw.line(screen, (255,255,255), (x1, y1), (x2, y2), 2)
            drawTree(x2, y2, angle + fork_angle, depth - 1)
            drawTree(x2, y2, angle - fork_angle, depth - 1)
            drawTree(x2, y2, angle + fork_angle2, depth - 1)
            drawTree(x2, y2, angle - fork_angle, depth - 1)

 
def input(event):
    if event.type == pygame.QUIT:
        exit(0)
 
drawTree(300, 550, -90, 9)
pygame.display.flip()
pygame.image.save(screen, 'imagen.jpg')

#while True:
    #input(pygame.event.wait())


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
    if(((data[w][0] != 255) and (data[w][1] != 255) and (data[w][2] != 255)) and (data2[w][0] == 255) and (data2[w][1] == 255) and (data2[w][2] == 255)):
        contador+=1

    w+=1

print("Contador:", contador)
print((contador*100)/(600*600), "%")
