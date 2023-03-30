import pygame
import math

# define the size of the cube and the focal length
cube_size = 200
focal_length = 500

# define the corners of the cube relative to its center
half_cube = cube_size // 2
corners = [(-half_cube, -half_cube, half_cube),
           (half_cube, -half_cube, half_cube),
           (half_cube, half_cube, half_cube),
           (-half_cube, half_cube, half_cube),
           (-half_cube, -half_cube, -half_cube),
           (half_cube, -half_cube, -half_cube),
           (half_cube, half_cube, -half_cube),
           (-half_cube, half_cube, -half_cube)]

# initialize Pygame and create a window
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Rotating Cube")

# define a function to draw the cube with a given rotation angle
def draw_cube(angle):
    positions = []

    # apply the rotation transform to each corner
    cos_angle = math.cos(angle)
    sin_angle = math.sin(angle)
    for x, y, z in corners:
        # rotate around the Y axis (vertical)
        rotated_x = x * cos_angle + z * sin_angle
        rotated_z = z * cos_angle - x * sin_angle
        # rotate around the X axis (horizontal)
        rotated_y = y * cos_angle + rotated_z * sin_angle
        rotated_z = rotated_z * cos_angle - y * sin_angle
        # calculate the apparent position based on the focal length
        app_x = int(rotated_x * focal_length / (rotated_z + focal_length) + width / 2)
        app_y = int(rotated_y * focal_length / (rotated_z + focal_length) + height / 2)
        positions.append((app_x, app_y))

    # draw the edges of the cube using the rotated positions
    pygame.draw.line(screen, (255, 255, 255), positions[0], positions[1])
    pygame.draw.line(screen, (255, 255, 255), positions[1], positions[2])
    pygame.draw.line(screen, (255, 255, 255), positions[2], positions[3])
    pygame.draw.line(screen, (255, 255, 255), positions[3], positions[0])
    pygame.draw.line(screen, (255, 255, 255), positions[4], positions[5])
    pygame.draw.line(screen, (255, 255, 255), positions[5], positions[6])
    pygame.draw.line(screen, (255, 255, 255), positions[6], positions[7])
    pygame.draw.line(screen, (255, 255, 255), positions[7], positions[4])
    pygame.draw.line(screen, (255, 255, 255), positions[0], positions[4])
    pygame.draw.line(screen, (255, 255, 255), positions[1], positions[5])
    pygame.draw.line(screen, (255, 255, 255), positions[2], positions[6])
    pygame.draw.line(screen, (255, 255, 255), positions[3], positions[7])

# initialize the rotation angle to zero
angle = 0

# start the main loop
# tick the clock to limit the frame rate to 30 frames per second
clock = pygame.time.Clock()
running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # fill the screen with black
    screen.fill((0, 0, 0))
    
    # update the rotation angle and draw the cube
    angle += 0.01
    draw_cube(angle)
    
    # update the display
    pygame.display.flip()

# quit Pygame properly
pygame.quit()
