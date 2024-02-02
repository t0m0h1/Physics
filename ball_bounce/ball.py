import pygame
import math

class Ball:
    def __init__(self, screen, x, y, radius, colour, velocity, max_speed):
        self.screen = screen
        self.x = x
        self.y = y
        self.radius = radius
        self.colour = colour
        self.velocity = velocity
        self.max_speed = max_speed

def update(self, other_ball=None):
    self.x += self.velocity[0]
    self.y += self.velocity[1]

    # Check if the ball has hit the left or right side of the screen
    if self.x + self.radius > self.screen.get_width() or self.x - self.radius < 0:
        self.velocity[0] = -self.velocity[0]
    # Check if the ball has hit the top or bottom of the screen
    if self.y + self.radius > self.screen.get_height() or self.y - self.radius < 0:
        self.velocity[1] = -self.velocity[1]

    # Check for collision with another ball
    if other_ball:
        distance = math.sqrt((self.x - other_ball.x)**2 + (self.y - other_ball.y)**2)
        if distance < self.radius + other_ball.radius:
            # Calculate collision normal and tangent
            collision_normal = [other_ball.x - self.x, other_ball.y - self.y]
            collision_distance = math.sqrt(collision_normal[0]**2 + collision_normal[1]**2)
            collision_normal = [collision_normal[0] / collision_distance, collision_normal[1] / collision_distance]
            collision_tangent = [-collision_normal[1], collision_normal[0]]

            # Calculate relative velocity
            relative_velocity = [
                self.velocity[0] - other_ball.velocity[0],
                self.velocity[1] - other_ball.velocity[1]
            ]

            # Calculate dot products
            dot_normal = relative_velocity[0] * collision_normal[0] + relative_velocity[1] * collision_normal[1]
            dot_tangent = relative_velocity[0] * collision_tangent[0] + relative_velocity[1] * collision_tangent[1]

            # Update velocities
            self.velocity[0] -= dot_normal * collision_normal[0]
            self.velocity[1] -= dot_normal * collision_normal[1]

            # Separate the balls to prevent them from sticking together
            overlap = self.radius + other_ball.radius - distance
            self.x += collision_normal[0] * overlap / 2
            self.y += collision_normal[1] * overlap / 2
            other_ball.x -= collision_normal[0] * overlap / 2
            other_ball.y -= collision_normal[1] * overlap / 2

            # Ensure the new velocity magnitude does not exceed the maximum speed
            speed = math.sqrt(self.velocity[0]**2 + self.velocity[1]**2)
            if speed > self.max_speed:
                # Normalize the velocity vector and scale it to the maximum speed
                scale_factor = self.max_speed / speed
                self.velocity[0] *= scale_factor
                self.velocity[1] *= scale_factor

def draw(self):
    pygame.draw.circle(self.screen, self.colour, (int(self.x), int(self.y)), self.radius)