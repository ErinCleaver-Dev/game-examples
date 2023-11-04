import pygame
import charater


class Game():
    def __init__(self, screen_width =640, screen_hight=480, title="Hello Pygame"):
        self.screen_width = screen_width;
        self.screen_hight= screen_hight;
        self.title = title
        self.running = True
        self.window = ''
        self.player = charater.Character_Squre(5, 5, 100, 100, (0, 255, 0), self.screen_width, self.screen_hight)
        pass
    
    def start_game(self):
        pygame.init()
        self.window = pygame.display.set_mode((self.screen_width, self.screen_hight), 0, 32)
        pygame.display.set_caption(self.title)
        self.window.fill((0, 0, 0))
    
    def is_running(self):
        return self.running
    
    def actions(self):
        self.player.move()
    
    def quit_game(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
    
    def display_character(self, sprit, image_size):
        try:
            self.window.blit(sprit, (self.window.get_width()/2 - image_size[0]/2, self.window.get_height()/2 - image_size[1]/2))
        except TypeError as error: 
            print(image_size[0]/2)
            
    def display_squre(self):
        self.window.fill((0, 0, 0))
        self.player.draw(self.window)
        pygame.display.update()
        