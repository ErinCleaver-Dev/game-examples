import pygame


class Sprite():
    def __init__(self, file_name, hight = 0, width = 0):
        self.file_name = file_name
        self.sprite = pygame.image.load(self.file_name)
        self.hight = hight
        self.width = width
        pass
    
    def display_sprit(self):
        if self.hight != 0 and self.width !=0:
            self.sprite = pygame.transform.scale(self.sprite, (self.hight, self.width))
        return self.sprite
    
    def get_size(self):
        try:
            return (self.sprite.get_height(), self.sprite.get_width())
        except:
            pass
    