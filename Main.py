import pygame
import pygame.mixer
import numpy as np
import math


def desenha_cubo(vertices, dist_focal, angulo_x, angulo_y, angulo_z, tamanho_tela, tela):

    # Matrizes de rotação para cada eixo
    R_X = np.array([
        [1, 0, 0, 0],
        [0, math.cos(angulo_x), -math.sin(angulo_x), 0],
        [0, math.sin(angulo_x), math.cos(angulo_x), 0],
        [0, 0, 0, 1]
    ])

    R_Y = np.array([
        [math.cos(angulo_y), 0, math.sin(angulo_y), 0],
        [0, 1, 0, 0],
        [-math.sin(angulo_y), 0, math.cos(angulo_y), 0],
        [0, 0, 0, 1]
    ])

    R_Z = np.array([
        [math.cos(angulo_z), -math.sin(angulo_z), 0, 0],
        [math.sin(angulo_z), math.cos(angulo_z), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])

    # Matriz de rotação final
    R = R_X @ R_Y @ R_Z

    # Matrizes de translação do eixo Z e para o centro da tela
    T_Z = np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, dist_focal],
        [0, 0, 0, 1]
    ])

    T_CENTRO = np.array([
        [1, 0, 0, tamanho_tela[0] // 2],
        [0, 1, 0, tamanho_tela[1] // 2],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])

    # Matriz de projeção Pinhole
    P = np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 0, -dist_focal],
        [0, 0, -1/dist_focal, 0]
    ])

    # Matriz de transformação final
    M_T = T_CENTRO @ P @ T_Z @ R

    # Aplicando a transformação no cubo
    C = M_T @ vertices

    # Desenha as arestas do cubo
    pygame.draw.line(tela, (255, 255, 255), (C[0, 0], C[1, 0]), (C[0, 1], C[1, 1]))
    pygame.draw.line(tela, (255, 255, 255), (C[0, 1], C[1, 1]), (C[0, 2], C[1, 2]))
    pygame.draw.line(tela, (255, 255, 255), (C[0, 2], C[1, 2]), (C[0, 3], C[1, 3]))
    pygame.draw.line(tela, (255, 255, 255), (C[0, 3], C[1, 3]), (C[0, 0], C[1, 0]))
    pygame.draw.line(tela, (255, 255, 255), (C[0, 4], C[1, 4]), (C[0, 5], C[1, 5]))
    pygame.draw.line(tela, (255, 255, 255), (C[0, 5], C[1, 5]), (C[0, 6], C[1, 6]))
    pygame.draw.line(tela, (255, 255, 255), (C[0, 6], C[1, 6]), (C[0, 7], C[1, 7]))
    pygame.draw.line(tela, (255, 255, 255), (C[0, 7], C[1, 7]), (C[0, 4], C[1, 4]))
    pygame.draw.line(tela, (255, 255, 255), (C[0, 0], C[1, 0]), (C[0, 4], C[1, 4]))
    pygame.draw.line(tela, (255, 255, 255), (C[0, 1], C[1, 1]), (C[0, 5], C[1, 5]))
    pygame.draw.line(tela, (255, 255, 255), (C[0, 2], C[1, 2]), (C[0, 6], C[1, 6]))
    pygame.draw.line(tela, (255, 255, 255), (C[0, 3], C[1, 3]), (C[0, 7], C[1, 7]))

    # Desenha o slider
    fonte = pygame.font.Font(None, 24)
    label_surface = fonte.render("Focal Length:", True, (255, 255, 255))
    tela.blit(label_surface, (10, tamanho_tela[0] - 30))
    pygame.draw.rect(tela, (255, 255, 255), pygame.Rect(120, tamanho_tela[0] - 25, 500, 10))
    slider_pos = int((dist_focal - 100) * 500 / 900)
    pygame.draw.circle(tela, (255, 255, 255), (slider_pos + 120, tamanho_tela[0] - 20), 10)

def main():

    # Distância focal inicial e tamanho do cubo
    dist_focal = 500
    t_cubo = 200

    # Definindo os vértices do cubo
    metade_cubo = t_cubo // 2
    vertices = np.array([
        [-metade_cubo, -metade_cubo, -metade_cubo, 1], [metade_cubo, -metade_cubo, -metade_cubo, 1],
        [metade_cubo, metade_cubo, -metade_cubo, 1], [-metade_cubo, metade_cubo, -metade_cubo, 1],
        [-metade_cubo, -metade_cubo, metade_cubo, 1], [metade_cubo, -metade_cubo, metade_cubo, 1],
        [metade_cubo, metade_cubo, metade_cubo, 1], [-metade_cubo, metade_cubo, metade_cubo, 1]
    ]).T

    # Inicialização do Pygame
    pygame.init()
    pygame.mixer.init()
    pygame.display.set_caption("Cubo 3D Rotacionando")
    tamanho_tela = (800, 650)

    # Inicializando a tela
    tela = pygame.display.set_mode(tamanho_tela)
    tela.fill((0, 0, 0))

    # Inicializando as variáveis
    angulo_x, angulo_y, angulo_z = 0, 0, 0
    rotaciona_x, rotaciona_y, rotaciona_z = True, True, True
    muda_slider = False

    # Inicializando o clock
    clock = pygame.time.Clock()
    rodando = True

    # Loop principal
    while rodando:
        clock.tick(60)
        for event in pygame.event.get():
            if event == pygame.QUIT:
                rodando = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # verificar se o mouse está sobre o slider, ou se está sobre um dos botões de rotação
                x, y = event.pos
                if y >= tamanho_tela[0] - 35 and y <= tamanho_tela[0] - 15 and x >= 120 and x <= 620:
                    muda_slider = True
                elif x >= 10 and x <= 110 and y >= 50 and y <= 90:
                    rotaciona_x = not rotaciona_x
                elif x >= 10 and x <= 110 and y >= 100 and y <= 140:
                    rotaciona_y = not rotaciona_y
                elif x >= 10 and x <= 110 and y >= 150 and y <= 190:
                    rotaciona_z = not rotaciona_z

            elif event.type == pygame.MOUSEBUTTONUP:
                muda_slider = False

            elif event.type == pygame.MOUSEMOTION:
                # Atualiza a nova distância focal
                if muda_slider:
                    x, y = event.pos
                    nova_posicao_slider  = min(max(x - 120, 0), 500)
                    dist_focal = int(nova_posicao_slider * 900 / 500 + 100)

        # Atualiza os ângulos de rotação
        if rotaciona_x:
            angulo_x += 0.01
        if rotaciona_y:
            angulo_y += 0.01
        if rotaciona_z:
            angulo_z += 0.01

        # Aplica os cálculos no cubo
        desenha_cubo(vertices, dist_focal, angulo_x, angulo_y, angulo_z, tamanho_tela, tela)

        # Desenha os botões de rotação
        pygame.draw.rect(tela, (255, 0, 0), pygame.Rect(10, 50, 100, 40), not rotaciona_x)
        pygame.draw.rect(tela, (0, 255, 0), pygame.Rect(10, 100, 100, 40), not rotaciona_y)
        pygame.draw.rect(tela, (0, 0, 255), pygame.Rect(10, 150, 100, 40), not rotaciona_z)

        fonte = pygame.font.Font(None, 24)
        label_surface = fonte.render("Rotaciona X", True, (255, 255, 255))
        tela.blit(label_surface, (25, 58))

        label_surface = fonte.render("Rotaciona Y", True, (255, 255, 255))
        tela.blit(label_surface, (25, 108))

        label_surface = fonte.render("Rotaciona Z", True, (255, 255, 255))
        tela.blit(label_surface, (25, 158))

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()







