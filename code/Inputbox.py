import pygame 
from const import font1



class InputBox:
    def __init__(self,  x, y, width, height, text='', font=font1):
        self.x= x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(((self.x-self.width/2), (self.y-self.height/2), self.width, self.height))
        self.text = text
        self.color = pygame.Color(109,109,109)
        font = pygame.font.SysFont(font1, 32, True)
        self.font = font
        self.txt_render = self.font.render(text, True, self.color)
        self.active = False
        
        
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:

            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
                
            if self.active:
                self.color =(190,190,190)
            else:
                self.color = pygame.Color(109,109,109)
                
        
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(f"vous avez écrit : {self.text}")
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.txt_render = self.font.render(self.text, True, (0,0,0))

    def show(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        screen.blit(self.txt_render, (self.rect.x, self.rect.y))
        
