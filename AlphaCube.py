import pygame
import math
import numpy as np

# define the size of the cube and the initial focal length
cube_size = 200
focal_length = 500

# define the corners of the cube relative to its center
half_cube = cube_size // 2
corners = np.array([[-half_cube, -half_cube, half_cube],
                    [half_cube, -half_cube, half_cube],
                    [half_cube, half_cube, half_cube],
                    [-half_cube, half_cube, half_cube],
                    [-half_cube, -half_cube, -half_cube],
                    [half_cube, -half_cube, -half_cube],
                    [half_cube, half_cube, -half_cube],
                    [-half_cube, half_cube, -half_cube]]).T

def draw_cube(angle_x, angle_y, angle_z, focal_length):
    positions = []

    # define the transformation matrices for rotating around the X, Y, and Z axes
    cos_x, sin_x = math.cos(angle_x), math.sin(angle_x)
    cos_y, sin_y = math.cos(angle_y), math.sin(angle_y)
    cos_z, sin_z = math.cos(angle_z), math.sin(angle_z)

    rotate_x = np.array([[1, 0, 0], [0, cos_x, -sin_x], [0, sin_x, cos_x]])
    rotate_y = np.array([[cos_y, 0, sin_y], [0, 1, 0], [-sin_y, 0, cos_y]])
    rotate_z = np.array([[cos_z, -sin_z, 0], [sin_z, cos_z, 0], [0, 0, 1]])

    # apply the transformation matrices to each corner
    rotated_corners = np.dot(rotate_z, corners)
    rotated_corners = np.dot(rotate_y, rotated_corners)
    rotated_corners = np.dot(rotate_x, rotated_corners)

    # calculate the apparent position based on the focal length
    app_x = rotated_corners[0] * focal_length / (rotated_corners[2] + focal_length) + width / 2
    app_y = rotated_corners[1] * focal_length / (rotated_corners[2] + focal_length) + height / 2

    # draw the edges of the cube using the transformed positions
    pygame.draw.line(screen, (255, 255, 255), (app_x[0], app_y[0]), (app_x[1], app_y[1]))
    pygame.draw.line(screen, (255, 255, 255), (app_x[1], app_y[1]), (app_x[2], app_y[2]))
    pygame.draw.line(screen, (255, 255, 255), (app_x[2], app_y[2]), (app_x[3], app_y[3]))
    pygame.draw.line(screen, (255, 255, 255), (app_x[3], app_y[3]), (app_x[0], app_y[0]))
    pygame.draw.line(screen, (255, 255, 255), (app_x[4], app_y[4]), (app_x[5], app_y[5]))
    pygame.draw.line(screen, (255, 255, 255), (app_x[5], app_y[5]), (app_x[6], app_y[6]))
    pygame.draw.line(screen, (255, 255, 255), (app_x[6], app_y[6]), (app_x[7], app_y[7]))
    pygame.draw.line(screen, (255, 255, 255), (app_x[7], app_y[7]), (app_x[4], app_y[4]))
    pygame.draw.line(screen, (255, 255, 255), (app_x[0], app_y[0]), (app_x[4], app_y[4]))
    pygame.draw.line(screen, (255, 255, 255), (app_x[1], app_y[1]), (app_x[5], app_y[5]))
    pygame.draw.line(screen, (255, 255, 255), (app_x[2], app_y[2]), (app_x[6], app_y[6]))
    pygame.draw.line(screen, (255, 255, 255), (app_x[3], app_y[3]), (app_x[7], app_y[7]))

    # draw the focal distance slider and text label
    font = pygame.font.Font(None, 24)
    label_surface = font.render("Focal Length:", True, (255, 255, 255))
    screen.blit(label_surface, (10, height - 30))
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(120, height - 25, 500, 10))
    slider_pos = int((focal_length - 100) * 500 / 900)
    pygame.draw.circle(screen, (255, 255, 255), (slider_pos + 120, height - 20), 10)

# initialize Pygame and create a window
pygame.init()
width, height = 800, 650
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Rotating Cube")

# initialize the rotation angles to zero and set up the focal distance slider
angle_x, angle_y, angle_z = 0, 0, 0
rotate_x_enabled = True
rotate_y_enabled = True
rotate_z_enabled = True
focal_slider_changed = False

# start the main loop
# tick the clock to limit the frame rate to 60 frames per second
clock = pygame.time.Clock()
running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # check if the user clicked on the focal distance slider
            x, y = event.pos
            if y >= height - 35 and y <= height - 15 and x >= 120 and x <= 620:
                focal_slider_changed = True
            elif x >= 10 and x <= 110 and y >= 50 and y <= 90:
                rotate_x_enabled = not rotate_x_enabled
            elif x >= 10 and x <= 110 and y >= 100 and y <= 140:
                rotate_y_enabled = not rotate_y_enabled
            elif x >= 10 and x <= 110 and y >= 150 and y <= 190:
                rotate_z_enabled = not rotate_z_enabled

        elif event.type == pygame.MOUSEBUTTONUP:
            focal_slider_changed = False

        elif event.type == pygame.MOUSEMOTION:
            # update the focal distance value based on the position of the slider
            if focal_slider_changed:
                x, y = event.pos
                new_slider_pos = min(max(x - 120, 0), 500)
                focal_length = int(new_slider_pos * 900 / 500 + 100)

    # fill the screen with black
    screen.fill((0, 0, 0))

    # update the rotation angles and draw the cube with the current focal distance
    if rotate_x_enabled:
        angle_x += 0.01
    if rotate_y_enabled:
        angle_y += 0.01
    if rotate_z_enabled:
        angle_z += 0.01

    draw_cube(angle_x, angle_y, angle_z, focal_length)

    # draw the button boxes and text labels
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(10, 50, 100, 40), not rotate_x_enabled)
    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(10, 100, 100, 40), not rotate_y_enabled)
    pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(10, 150, 100, 40), not rotate_z_enabled)

    font = pygame.font.Font(None, 24)
    label_surface = font.render("Rotate X", True, (255, 255, 255))
    screen.blit(label_surface, (25, 58))

    label_surface = font.render("Rotate Y", True, (255, 255, 255))
    screen.blit(label_surface, (25, 108))

    label_surface = font.render("Rotate Z", True, (255, 255, 255))
    screen.blit(label_surface, (25, 158))

    # update the display
    pygame.display.flip()

# quit Pygame properly
pygame.quit()
