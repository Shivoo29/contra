import pygame 

class Bullet:
    def __init__(self, screen, pos):
        self.screen = screen
        self.image = pygame.Surface((5, 10))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(center=pos)

    def update(self):
        self.rect.y -= 10

    def draw(self):
        self.screen.blit(self.image, self.rect)
