from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
import random
import pygame

class Asteroid(CircleShape):
	def __init__(self, x: float, y: float, radius: float) -> None:
		super().__init__(x, y, radius)

	def draw(self, screen, color="white", line_width=LINE_WIDTH):
		pygame.draw.circle(screen, color, self.position, self.radius, line_width)

	def update(self, dt):
		self.position += self.velocity * dt

	def split(self):
		self.kill()
		if self.radius <= ASTEROID_MIN_RADIUS:
			return
		else:
			log_event("asteroid_split")
			random_angle = random.uniform(20, 50)
			first_asteroid = Asteroid(self.position[0], self.position[1], self.radius)
			second_asteroid = Asteroid(self.position[0], self.position[1], self.radius)
			first_asteroid.velocity = self.velocity.rotate(random_angle) * 1.2
			second_asteroid.velocity = self.velocity.rotate(-random_angle) * 1.2
			first_asteroid.radius = self.radius - ASTEROID_MIN_RADIUS
			second_asteroid.radius = self.radius - ASTEROID_MIN_RADIUS
