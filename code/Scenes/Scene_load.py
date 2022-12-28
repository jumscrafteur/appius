from Scene import *
import pygame
from Button import *
from Inputbox import InputBox
from const import *
from .Scene_ids import *
from Save import *



def SceneLoadCreate(self):
    self.images["fond"] = pygame.image.load(
        "assets/0_fired_00001.png").convert()
    
    self.box["inputbox"] = InputBox(
        self.game.screen_width/2, self.game.screen_height/2-200, 600, 50,  lambda : pygame.event.post(pygame.event.Event(
            event_types["LaunchGame"], {"name": 2})))
    
    self.buttons["btn1"] = Button_text(self.game.screen_width/2-150, self.game.screen_height /
                                       2+230, 300, 100, lambda: self.game.switchScene(SCENE_MENU_ID), "Back to Menu")
    
    self.buttons["btn2"] = Button_text(self.game.screen_width/2+150, self.game.screen_height /
                                       2+230, 300, 100, lambda: pygame.event.post(pygame.event.Event(
                                           event_types["LaunchGame"], {"name": 2})), "Go to Game")
    
    
    font_load = pygame.font.SysFont(font1, 42, True)
    scale =0
    for nom in Save.getSavesNames():
        scale += 30
        self.buttons[nom] = Button_text(self.game.screen_width/2, self.game.screen_height/2-75-scale, 
                                        200, 20, lambda : pygame.event.post(pygame.event.Event(
                                           event_types["LoadName"], {nom: 3})), nom, font_load)
    

def SceneLoadRun(self):

    pygame.time.Clock().tick(60)
    self.game.screen.blit(pygame.transform.scale(
        self.images["fond"], (self.game.screen_width, self.game.screen_height)), (0, 0))
    
    pygame.draw.rect(self.game.screen, (180,180,180), (self.game.screen_width/2-300, self.game.screen_height/2-250, 600, 500))
    pygame.draw.rect(self.game.screen, (150,150,150), (self.game.screen_width/2-250, self.game.screen_height/2-200, 500, 400))
    
    for key in self.buttons.keys():
        self.buttons[key].show(self.game.screen, False)
        
    for key in self.box.keys():
        self.box[key].show(self.game.screen)
    
    pygame.display.flip()


def SceneLoadGamehandleEventsFunc(self, event):
    if event.type == event_types["LaunchGame"]:
        self.game.save = self.box["inputbox"].text
        self.game.switchScene(SCENE_GAME_ID)
    
    if event.type == event_types["LoadName"]:
        for key in self.buttons.keys():
            self.box["inputbox"].text = self.buttons[key].text
            self.box["inputbox"].txt_render = self.box["inputbox"].font.render(self.box["inputbox"].text, True, (0, 0, 0))

            



SCENE = Scene(SCENE_LOADGAME_ID, 'Scene_newgame', createFunc=SceneLoadCreate,
              runFunc=SceneLoadRun, handleEventsFunc=SceneLoadGamehandleEventsFunc)
