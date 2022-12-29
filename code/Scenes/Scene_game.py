from Scene import Scene
from .Scene_ids import SCENE_GAME_ID
from map_init.game.map import MapGame
import pygame
from Utils import cartCoToIsoCo


# NOTE de Hugo : Variable pour que je puisse debug sans casser le code pour vous.
REFACTO_HUGO = True


def SceneGameCreate(self):
    self.map = MapGame(self.game.screen, pygame.time.Clock())
    # TODO : modifier les valeurs de width and height
    self.camera = Camera(self.game.screen_width, self.game.screen_height)


def SceneGameRun(self):
    if not REFACTO_HUGO:
        self.map.run()
    else:
        self.game.screen.fill((0, 0, 0))
        self.camera.movement_arrow()

        for building in self.game.save.map:
            # Get de position from de building
            gridCartPosX, gridCartPosY = building.pos

            # Space them according to the tile size
            mapCartPosX, mapCartPosY = gridCartPosX * 30, gridCartPosY * 30

            # Transfer to Isometric space
            mapIsoPosX, mapIsoPosY = cartCoToIsoCo(mapCartPosX, mapCartPosY)

            self.game.screen.blit(building.tileImage,
                                  (mapIsoPosX + self.camera.scroll.x, mapIsoPosY + self.camera.scroll.y))

        self.map.hudleft.draw(self.game.screen)
        # self.map.hudstick.draw(self.game.screen)
        self.map.hudup.draw(self.game.screen)
        self.map.infofps.draw(self.game.screen)
        self.map.infopop.draw(self.game.screen)

        pygame.display.flip()


def SceneGameHandleEvents(self, event):
    if REFACTO_HUGO:
        if event.type in [pygame.KEYUP, pygame.KEYDOWN] and event.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_DOWN, pygame.K_UP]:
            self.camera.keys[event.key] = not self.camera.keys[event.key]

        # self.camera.movement_arrow(pygame.key.get_pressed())


# 1073741906
# 1073741903

# 1073741905
# 1073741904


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

        self.scroll = pygame.Vector2(width/2, height/2)
        self.mousseMouvSpeed = 10
        self.keyboardMouvSpeed = 10

    def movement_arrow(self):
        self.scroll.x += (self.keys[pygame.K_LEFT] -
                          self.keys[pygame.K_RIGHT])*self.keyboardMouvSpeed
        self.scroll.y += (self.keys[pygame.K_UP] -
                          self.keys[pygame.K_DOWN])*self.keyboardMouvSpeed

    def movement_mouse(self, mouse_pos):

        # x movement
        if mouse_pos[0] > self.width * 0.97:
            self.scroll.x += -self.mousseMouvSpeed
        elif mouse_pos[0] < self.width * 0.03:
            self.scroll.x += self.mousseMouvSpeed

        # y movement
        if mouse_pos[1] > self.height * 0.97:
            self.scroll.y += -self.mousseMouvSpeed
        elif mouse_pos[1] < self.height * 0.03:
            self.scroll.y += self.mousseMouvSpeed
