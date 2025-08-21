from circleshape import CircleShape
from constants import SHOT_RADIUS
import pygame

class Shot(CircleShape):
    def __init__(self, x, y, velocity):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = velocity
    
    def update(self, dt):
        self.position += self.velocity * dt

    def draw(self, screen):
        pos = (int(self.position.x), int(self.position.y))
        pygame.draw.circle(screen, "white", pos, SHOT_RADIUS)