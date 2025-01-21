import circleshape
import pygame
import constants

class Shot(circleshape.CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y,constants.SHOT_RADIUS)

    def draw(self, screen):
        # sub-classes must override
         pygame.draw.circle(screen,color='white',center=self.position,radius=self.radius,width=2)

    def update(self, dt):
        self.position += self.velocity * dt