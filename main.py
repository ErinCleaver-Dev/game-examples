import game
import pygame 

# sprite1 = sprites.Sprite('sprites\organge blob.png', 50, 50)


hight = 500
width = 500
game = game.Game(width, hight, "Client")
game.start_game()


while game.is_running():
    game.quit_game()
    game.actions()
    game.display_squre()
    
pygame.quit()