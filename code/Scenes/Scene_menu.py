from Scene import *
import pygame
from Button import *
from const import *





def SceneMenuCreate(self):
    fond = pygame.image.load("assets/0_fired_00001.png").convert()
    
    self.buttons["button_start"] = Button_text(screen_width/2, 128 , 200, 100, lambda : self.game.actualScene = 2 ,"Start Game")
    self.buttons["button_load"] = Button_text(screen_width/2, 384, 200, 100, lambda : print("ok"),"Load a Game")
    self.buttons["button_options"] = Button_text(screen_width/2, 640, 200, 100, lambda : print("ok"),"Options")
    self.buttons["button_exit"] = Button_text(screen_width/2, 896, 200, 100, lambda : print("ok"),"Exit Game")
    
def SceneMenuRun(self):
    for key in self.buttons.keys():
        self.buttons[key].show(self.game.screen)
    

MAIN_SCENE = Scene(1, 'Scene_Menu', createFunc= SceneMenuCreate, runFunc=SceneMenuRun)