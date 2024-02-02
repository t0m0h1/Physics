import pygame
import math

class Ball:
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
                self.velocity = [
                    collision_normal[0] * dot_normal,
                    collision_normal[1] * dot_normal
                ]
                self.velocity[0] += collision_tangent[0] * dot_tangent
                self.velocity[1] += collision_tangent[1] * dot_tangent

    def draw(self):
        pygame.draw.circle(self.screen, self.colour, (int(self.x), int(self.y)), self.radius)
