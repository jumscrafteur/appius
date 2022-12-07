import pygame 
from const import font1


class Button:
    
    def __init__(self,  x, y, width, height, action):
        self.x= x
        self.y = y
        self.width = width
        self.height = height
        self.action = action
        
    def MouseonButton(self, posMouse):
        if(posMouse[0] > (self.x - self.width/2) and posMouse[0] < (self.x + self.width/2)):
            if (posMouse[1] > (self.y - self.height/2) and posMouse[1] < (self.y + self.height/2)):
                 pygame.event.post(pygame.event.Event(
                    pygame.USEREVENT, {"action": self.action}))
                
        
    
        
        
class Button_img(Button):
    def __init__(self, x, y, action,  image):
        self.image = pygame.image.load(image).convert()
        super().__init__(x, y, self.image.get_width(), self.image.get_height(), action)
        self.rect = self.image.get_rect(center=(self.x, self.y))
        
    def show(self, screen):
        screen.blit(pygame.transform.scale(self.image, (self.image.get_width(), self.image.get_height())), self.rect)
    
    
class Button_text(Button):
    
    def __init__(self, x, y, width, height, action, text, font=font1):
        self.text = text
        font = pygame.font.SysFont(font1, 24)
        self.font = font
        self.width = width
        self.height = height
        self.text_render = font.render(self.text, 1, (0,0,0))
        super().__init__(x, y, width, height, action)
        
    def show(self, screen, border=None):
            pygame.draw.rect(screen, (225,225,225), ((self.x-self.width/2), (self.y-self.height/2), self.width, self.height))
            screen.blit(self.text_render, (self.x-self.text_render.get_width()/2, self.y-self.text_render.get_height()/2))
        
    
    
        