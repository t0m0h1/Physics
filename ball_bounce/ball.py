import pygame

class Ball: # Create a class for the ball which takes in the screen, the x and y position, the x and y velocity, the radius and the colour
    def __init__(self, screen, x, y, radius, colour, velocity):
        self.screen = screen
        self.x = x
        self.y = y
        self.radius = radius
        self.colour = colour
        self.velocity = velocity

    def update(self):
        self.x += self.velocity[0]
        self.y += self.velocity[1]

        # Check if the ball has hit the left or right side of the screen
        if self.x + self.radius > self.screen.get_width() or self.x - self.radius < 0:
            self.velocity[0] = -self.velocity[0]
        # check if the ball has hit the top or bottom of the screen
        if self.y + self.radius > self.screen.get_height() or self.y - self.radius < 0:
            self.velocity[1] = -self.velocity[1]
    
    def draw(self):
        pygame.draw.circle(self.screen, self.colour, (int(self.x), int(self.y)), self.radius)

