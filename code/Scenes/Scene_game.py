from Scene import Scene
from .Scene_ids import SCENE_GAME_ID
from map_init.game.map import MapGame
import pygame
from Utils import cartCoToIsoCo


# NOTE de Hugo : Variable pour que je puisse debug sans casser le code pour vous.
REFACTO_HUGO = False


def SceneGameCreate(self):
    self.map = MapGame(self.game.screen, pygame.time.Clock())
    # TODO : modifier les valeurs de width and height
    self.camera = Camera(100, 100)


def SceneGameRun(self):
    if not REFACTO_HUGO:
        self.map.run()
    else:
        self.game.screen.fill((0, 0, 0))

        for building in self.game.save.map:
            # Get de position from de building
            gridCartPosX, gridCartPosY = building.pos

            # Space them according to the tile size
            mapCartPosX, mapCartPosY = gridCartPosX * 30, gridCartPosY * 30

            # Transfer to Isometric space
            mapIsoPosX, mapIsoPosY = cartCoToIsoCo(mapCartPosX, mapCartPosY)

            self.game.screen.blit(building.tileImage,
                                  (mapIsoPosX + self.camera.scroll.x, mapIsoPosY + self.camera.scroll.y))
        # self.game.screen.blit(self.map.world.land_tile,
        #                       (self.map.camera.scroll.x, self.map.camera.scroll.y))

        # for y in range(len(self.game.save.map)):
        #     for x in range(len(self.game.save.map[y])):

        #         render_pos = self.map.world.world[x][y]["render_pos"]

        #         if self.map.world.world[x][y]["tile"]["name"] != "":
        #             name_tile = self.map.world.world[x][y]["tile"]["name"]
        #             offset = self.map.world.world[x][y]["tile"]["offset"]
        #             self.game.screen.blit(self.map.world.tiles[name_tile], (
        #                 render_pos[0]+self.map.world.land_tile.get_width() *
        #                 0.5 + self.map.camera.scroll.x,
        #                 render_pos[1]+self.map.world.land_tile.get_height()*0 - offset + self.map.camera.scroll.y))

        #         p = self.map.world.world[x][y]["iso_poly"]
        #         p = [(x + self.map.world.land_tile.get_width() *
        #               0.5 + self.map.camera.scroll.x, y + self.map.world.land_tile.get_height()*0+self.map.camera.scroll.y) for x, y in p]

        self.map.hudleft.draw(self.game.screen)
        self.map.hudstick.draw(self.game.screen)
        self.map.hudup.draw(self.game.screen)
        self.map.infofps.draw(self.game.screen)
        self.map.infopop.draw(self.game.screen)

        pygame.display.flip()
    # pass


def SceneGameHandleEvents(self, event):
    if REFACTO_HUGO:
        if event.type in [pygame.KEYUP, pygame.KEYDOWN]:
            print(pygame.key.get_pressed()[pygame.K_UP])
            print(pygame.key.get_pressed()[pygame.K_DOWN])

        self.camera.movement_arrow(pygame.key.get_pressed())


SCENE = Scene(SCENE_GAME_ID, 'Scene_Menu', createFunc=SceneGameCreate,
              runFunc=SceneGameRun, handleEventsFunc=SceneGameHandleEvents)


class Camera:

    def __init__(self, width, height):

        self.width = width
        self.height = height

        self.scroll = pygame.Vector2(0, 500)
        self.mousseMouvSpeed = 10
        self.keyboardMouvSpeed = 5

    def movement_arrow(self, key_press):
        self.scroll.x += (key_press[pygame.K_LEFT] -
                          key_press[pygame.K_RIGHT])*self.keyboardMouvSpeed
        self.scroll.y += (key_press[pygame.K_UP] -
                          key_press[pygame.K_DOWN])*self.keyboardMouvSpeed

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
