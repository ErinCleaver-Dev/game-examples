import shapes
import pygame 

class Character_Squre(shapes.Squre):
    def __init__(self, x, y, width, height, color, screen_width, screen_height):
        super().__init__(x, y, width, height, color)
        self.move_val = 1
        self.location = True
        self.screen_width = screen_width
        self.screen_height = screen_height
        
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.x != 5:
            self.rect.x -=self.move_val
            print(self.rect)
        if keys[pygame.K_RIGHT] and self.rect.x != self.screen_width - 105:
            self.rect.x += self.move_val
        if keys[pygame.K_UP] and self.rect.y != 5:
            self.rect.y -= self.move_val
        if keys[pygame.K_DOWN] and self.rect.y != self.screen_height - 105:
            self.rect.y += self.move_val