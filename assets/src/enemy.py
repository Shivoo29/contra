import pygame
import random


pygame.init()

class Enemy(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height, images):
        super().__init__()
        

        self.images = [pygame.image.load(image).convert_alpha() for image in images]
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        

        self.rect.x = random.randint(screen_width, screen_width + 50)  
        self.rect.y = random.randint(0, screen_height - self.rect.height)
        

        self.speed_x = random.randint(-5, -2)
        self.speed_y = random.choice([-1, 1])
        
    def update(self):

        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        
 
        if self.rect.top < 0 or self.rect.bottom > pygame.display.get_surface().get_height():
            self.speed_y *= -1
        

        self.index = (self.index + 1) % len(self.images)
        self.image = self.images[self.index]
        

        if self.rect.right < 0:
            self.kill()


if __name__ == "__main__":

    screen_width, screen_height = 800, 600
    

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Enemy Example")
    

    enemy_images = [
        'assets/images/enemy1.png',
        'path/to/enemy2.png',
        
    ]

    all_enemies = pygame.sprite.Group()
    

    for _ in range(5):
        enemy = Enemy(screen_width, screen_height, enemy_images)
        all_enemies.add(enemy)
    

    running = True
    clock = pygame.time.Clock()
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        

        all_enemies.update()
        

        screen.fill((0, 0, 0)) 
        all_enemies.draw(screen)
        
   
        pygame.display.flip()
        

        clock.tick(60)
    
    pygame.quit()
