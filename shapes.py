import pygame 

class Squre(): 
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        
    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)
        
    