import pygame
import sys
from ball import Ball

pygame.init() # Initialise pygame

screen = pygame.display.set_mode((400, 300)) # Create a screen with a size of 400x300
pygame.display.set_caption("Ball Bounce Simulation")
clock = pygame.time.Clock()

# Instatiate our ball
red_ball = Ball(screen, 100, 100, 20, (255, 0, 0), [2, 2])
blue_ball = Ball(screen, 200, 200, 20, (0, 0, 255), [-2, -2])

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255, 255, 255)) # Fill the screen with white

    red_ball.update(blue_ball)
    red_ball.draw()
    blue_ball.update(red_ball)
    blue_ball.draw()

    pygame.display.flip()
    clock.tick(60) # Limit the framerate to 60fps