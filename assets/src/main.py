import pygame
from player import Player
from utils import PLAYER_IMAGE_PATH

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width, screen_height = 800, 600

# Create a Pygame window
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Contra-like Shooter")

# Create player
player = Player(screen_width, screen_height)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update player
    keys = pygame.key.get_pressed()
    player.update(keys)

    # Draw everything
    screen.fill((0, 0, 0))  # Clear the screen with black
    screen.blit(player.image, player.rect)  # Draw the player
    pygame.display.flip()  # Update the display

    clock.tick(60)  # Cap the frame rate at 60 FPS

pygame.quit()
