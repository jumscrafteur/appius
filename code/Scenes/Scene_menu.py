from Scene import *
import pygame
from Button import *
from const import *





def SceneMenurun():
    fond = pygame.image.load("assets/0_fired_00001.png").convert()
    
    
    
    button_start = Button_text(screen_width/2, 128 , 200, 100, lambda : print("ok"),"Start Game")
    button_load = Button_text(screen_width/2, 384, 200, 100, lambda : print("ok"),"Load a Game")
    button_options = Button_text(screen_width/2, 640, 200, 100, lambda : print("ok"),"Options")
    button_exit = Button_text(screen_width/2, 896, 200, 100, lambda : print("ok"),"Exit Game")
    

MAIN_SCENE = Scene(1, 'Scene_Menu', runFunc=SceneMenurun)