from Scene import Scene
from .Scene_ids import SCENE_GAME_ID
from map_init.game.map import MapGame
import pygame
from Utils import cartCoToIsoCo


def SceneGameCreate(self):
    self.map = MapGame(self.game.screen, pygame.time.Clock())
    # TODO : modifier les valeurs de width and height
    self.camera = Camera(self.game.screen_width, self.game.screen_height)


def SceneGameRun(self):
    self.game.screen.fill((0, 0, 0))
    self.camera.movement_arrow()
    self.camera.movement_mouse()

    mapRender = pygame.Surface(
        (self.game.screen_width, self.game.screen_height))

    test = pygame.image.load("newland/Land2a_00034.png").convert_alpha()

    for building in self.game.save.map:
        # Get de position from de building
        gridCartPosX, gridCartPosY = building.pos

        # Space them according to the tile size
        mapCartPosX, mapCartPosY = gridCartPosX * 60, gridCartPosY * 60

        # Transfer to Isometric space
        mapIsoPosX, mapIsoPosY = cartCoToIsoCo(mapCartPosX, mapCartPosY)

        renderPosX = mapIsoPosX + self.camera.scroll.x
        renderPosY = mapIsoPosY + self.camera.scroll.y

        if building.risk_collapse > .5:
            mapRender.blit(test,
                           (renderPosX, renderPosY))
        else:
            mapRender.blit(building.tileImage.convert_alpha(),
                           (renderPosX, renderPosY))

    self.game.screen.blit(mapRender, (0, 0))

    self.map.hudleft.draw(self.game.screen)
    self.map.hudup.draw(self.game.screen)
    self.map.infofps.draw(self.game.screen)
    self.map.infopop.draw(self.game.screen)

    pygame.display.flip()


def SceneGameHandleEvents(self, event):
    if event.type in [pygame.KEYUP, pygame.KEYDOWN] and event.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_DOWN, pygame.K_UP]:
        self.camera.keys[event.key] = not self.camera.keys[event.key]
    elif event.type == pygame.MOUSEMOTION:
        self.camera.mousePos = event.pos
        pass


SCENE = Scene(SCENE_GAME_ID, 'Scene_Menu', createFunc=SceneGameCreate,
              runFunc=SceneGameRun, handleEventsFunc=SceneGameHandleEvents)


class Camera:

    def __init__(self, width, height):

        self.width = width
        self.height = height

        self.keys = {
            pygame.K_UP: False,
            pygame.K_LEFT: False,
            pygame.K_DOWN: False,
            pygame.K_RIGHT: False,
        }
        self.mousePos = (width/2, height/2)

        self.scroll = pygame.Vector2(width/2, height/2)
        self.mousseMouvSpeed = 20
        self.keyboardMouvSpeed = 20

    def movement_arrow(self):
        self.scroll.x += (self.keys[pygame.K_LEFT] -
                          self.keys[pygame.K_RIGHT])*self.keyboardMouvSpeed
        self.scroll.y += (self.keys[pygame.K_UP] -
                          self.keys[pygame.K_DOWN])*self.keyboardMouvSpeed

    def movement_mouse(self):

        # x movement
        if self.mousePos[0] > self.width * 0.97:
            self.scroll.x += -self.mousseMouvSpeed
        elif self.mousePos[0] < self.width * 0.03:
            self.scroll.x += self.mousseMouvSpeed

        # y movement
        if self.mousePos[1] > self.height * 0.97:
            self.scroll.y += -self.mousseMouvSpeed
        elif self.mousePos[1] < self.height * 0.03:
            self.scroll.y += self.mousseMouvSpeed
