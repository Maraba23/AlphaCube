import numpy as np
import matplotlib.pyplot as plt
import pygame
import time
import math
import random

############## COLORS ##############

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

####################################

############## Cube ##############
pontos = []

pontos.append(np.matrix([-1, -1, 1]))
pontos.append(np.matrix([1, -1, 1]))
pontos.append(np.matrix([1,  1, 1]))
pontos.append(np.matrix([-1, 1, 1]))
pontos.append(np.matrix([-1, -1, -1]))
pontos.append(np.matrix([1, -1, -1]))
pontos.append(np.matrix([1, 1, -1]))
pontos.append(np.matrix([-1, 1, -1]))

matriz_de_projecao = np.matrix([[1, 0, 0], [0, 1, 0], [0, 0, 0]])

angulo = 0

pontos_2d = [[n,n] for n in range(len(pontos))]

def linha(p1, p2, pontos):
    pygame.draw.line(screen, RED, (pontos[p1][0], pontos[p1][1]), (pontos[p2][0], pontos[p2][1]), 1)


####################################


screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("AlphaCube")

clock = pygame.time.Clock()
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()

    ############# Matriz de rotação #############
    # referencia: https://en.wikipedia.org/wiki/Rotation_matrix
    R_z = np.matrix([
        [math.cos(angulo), -math.sin(angulo), 0],
        [math.sin(angulo), math.cos(angulo), 0],
        [0, 0, 1]
    ])

    R_y = np.matrix([
        [math.cos(angulo), 0, math.sin(angulo)],
        [0, 1, 0],
        [-math.sin(angulo), 0, math.cos(angulo)]
    ])

    R_x = np.matrix([
        [1, 0, 0],
        [0, math.cos(angulo), -math.sin(angulo)],
        [0, math.sin(angulo), math.cos(angulo)]
    ])

    screen.fill((0, 0, 0))

    angulo += 0.01

    i = 0
    for ponto in pontos:
        Xd = R_z @ ponto.T
        Xd = R_y @ Xd
        Xd = R_x @ Xd
        para2d = matriz_de_projecao @ Xd

        pontos_2d[i] = [int(para2d[0, 0] * 100 + 400), int(para2d[1, 0] * 100 + 300)]

        pygame.draw.circle(screen, RED, (int(para2d[0, 0] * 100 + 400), int(para2d[1, 0] * 100 + 300)), 5)
        i += 1

    linha(0, 1, pontos_2d)
    linha(1, 2, pontos_2d)
    linha(2, 3, pontos_2d)
    linha(3, 0, pontos_2d)
    linha(4, 5, pontos_2d)
    linha(5, 6, pontos_2d)
    linha(6, 7, pontos_2d)
    linha(7, 4, pontos_2d)
    linha(0, 4, pontos_2d)
    linha(1, 5, pontos_2d)
    linha(2, 6, pontos_2d)
    linha(3, 7, pontos_2d)

    pygame.display.update()