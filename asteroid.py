import pygame
import random

from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt):
        self.position = self.position + self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        vec_a = self.velocity.rotate(angle)
        vec_b = self.velocity.rotate(angle * -1)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_a = Asteroid(self.position[0], self.position[1], new_radius)
        asteroid_a.velocity = vec_a * 1.2
        asteroid_b = Asteroid(self.position[0], self.position[1], new_radius)
        asteroid_b.velocity = vec_b * 1.2
