import pygame
from utils import PLAYER_IMAGE_PATH

class Player(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.image = pygame.image.load(PLAYER_IMAGE_PATH).convert_alpha()
        self.rect = self.image.get_rect(center=(screen_width // 2, screen_height - 50))

    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if keys[pygame.K_UP]:
            self.rect.y -= 5
        if keys[pygame.K_DOWN]:
            self.rect.y += 5

        # Ensure the player stays within the screen bounds
        self.rect.clamp_ip(pygame.Rect(0, 0, screen_width, screen_height))
