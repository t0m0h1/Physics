import pygame
import math

class Ball: # Create a class for the ball which takes in the screen, the x and y position, the x and y velocity, the radius and the colour
    def __init__(self, screen, x, y, radius, colour, velocity):
        self.screen = screen
        self.x = x
        self.y = y
        self.radius = radius
        self.colour = colour
        self.velocity = velocity

    def update(self, other_ball=None):
        self.x += self.velocity[0]
        self.y += self.velocity[1]

        # Check if the ball has hit the left or right side of the screen
        if self.x + self.radius > self.screen.get_width() or self.x - self.radius < 0:
            self.velocity[0] = -self.velocity[0]
        # check if the ball has hit the top or bottom of the screen
        if self.y + self.radius > self.screen.get_height() or self.y - self.radius < 0:
            self.velocity[1] = -self.velocity[1]
            
            
            
            
            # Check for collision with another ball
        if other_ball:
            distance = math.sqrt((self.x - other_ball.x)**2 + (self.y - other_ball.y)**2)
            if distance < self.radius + other_ball.radius:
                
                # Balls are colliding, update velocities based on Pythagorean theorem
                # we can use pythagoras to calculate the magnitude of the velocity
                relative_velocity = [self.velocity[0] - other_ball.velocity[0], self.velocity[1] - other_ball.velocity[1]]
                collision_angle = math.atan2(other_ball.y - self.y, other_ball.x - self.x)
                magnitude = math.sqrt(relative_velocity[0]**2 + relative_velocity[1]**2)

                new_velocity_self = [
                    magnitude * math.cos(collision_angle),
                    magnitude * math.sin(collision_angle)
                ]

                new_velocity_other = [
                    other_ball.velocity[0] + (self.velocity[0] - new_velocity_self[0]),
                    other_ball.velocity[1] + (self.velocity[1] - new_velocity_self[1])
                ]

                self.velocity = new_velocity_self
                other_ball.velocity = new_velocity_other
    





    def draw(self):
        pygame.draw.circle(self.screen, self.colour, (int(self.x), int(self.y)), self.radius)

