**Ball Bounce Simulation**

This Python program uses the Pygame library to simulate the bouncing of two balls in a 2D space. The balls can collide with each other and the edges of the screen.

**Ball Class**

The Ball class represents a ball in the simulation. Each ball has the following properties:

- screen: The Pygame surface where the ball is drawn.

- x and y: The current position of the ball.

- radius: The radius of the ball.

- color: The color of the ball.

- velocity: A list of two elements representing the velocity of the ball in the x and y directions.

- max_speed: The maximum speed of the ball.
- 

The Ball class has two methods:

- draw(): Draws the ball on the screen.

- update(other_ball): Updates the position of the ball based on its velocity, checks for collisions with the edges of the screen and the other ball, and adjusts the velocity accordingly.



**Collision Detection and Response**

The update method checks for collisions with the edges of the screen and reverses the direction of the velocity if a collision is detected.

The method also checks for collisions with another ball. If a collision is detected, it calculates the collision normal and tangent, the relative velocity, and the dot products of the relative velocity with the collision normal and tangent. It then updates the velocities of the two balls based on these calculations.

The method also ensures that the magnitude of the new velocity does not exceed the maximum speed of the ball. If it does, it normalizes the velocity vector and scales it to the maximum speed.

**Pythagorean Theorem**
The Pythagorean theorem is used in the update method to calculate the distance between the centers of the two balls. This is done with the following line of code:

The Pythagorean theorem states that in a right triangle, the square of the length of the hypotenuse (the side opposite the right angle) is equal to the sum of the squares of the lengths of the other two sides. This can be written as a² + b² = c².

In this case, the lengths of the two sides of the triangle are (self.x - other_ball.x) and (self.y - other_ball.y), which represent the differences in the x and y coordinates of the two balls. The length of the hypotenuse is the distance between the centers of the two balls.

**Run the simulation**
- run main.py
