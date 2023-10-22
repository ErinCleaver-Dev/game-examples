import game
import pygame 
import sprites

sprite1 = sprites.Sprite('sprites\organge blob.png', 50, 50)

hight = 500
width = 500
game = game.Game(width, hight, "Hello Sprite")
game.start_game()

while game.is_running():
    game.quit_game()
    game.display_character(sprite1.display_sprit(), sprite1.get_size())
    
pygame.quit()