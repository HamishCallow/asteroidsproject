from circleshape import CircleShape
from constants import *
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius, field):
        super().__init__(x, y, radius)
        self.field = field

    def draw(self, screen):
        pygame.draw.circle(
            screen, 
            "white", 
            (int(self.position.x), int(self.position.y)), 
            self.radius, 
            width=2
            )
        
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            new_trajectory1 = self.velocity.rotate(random_angle)
            new_trajectory2 = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            self.field.spawn(new_radius, self.position, new_trajectory1 * 1.2)
            self.field.spawn(new_radius, self.position, new_trajectory2 * 1.2)
