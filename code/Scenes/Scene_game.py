from Scene import Scene
from const import *
from .Scene_ids import SCENE_GAME_ID
from gamehud import *
from const import TILE_SIZE, TEMP_TILE
import pygame
from Utils import mouse_to_grid, can_place_tile
from Building import Housing


def SceneGameCreate(self):

    self.clock = pygame.time.Clock()
    self.hudup = Hudupper(0, 0, self.game.screen_width)
    self.hudleft = Hudbigleft(
        self.game.screen_width-24, self.game.screen_height+25)
    self.infofps = InfoShow(
        self.game.screen_width*0.5, 2, f"", 18, (255, 255, 255))
    self.infopop = InfoShow(
        self.game.screen_width*0.6, 2, f"Pop    xxxx", 18, (255, 255, 255))

    self.hud_manager = {"up": self.hudup, "main": self.hudleft,
                        "fps": self.infofps, "pop": self.infopop}

    # world
    self.world = World(40, 40, self.game.screen_width, self.game.screen_height,
                       self.hud_manager, self.game.save.map)
    # camera
    self.camera = Camera(self.game.screen_width,
                         self.game.screen_height, self.world.boundary)
    self.zoom = 1


def SceneGameRun(self):

    #
    self.clock.tick(60)
    self.hud_manager["fps"].text = 'fps={}'.format(round(self.clock.get_fps()))
    # update
    self.camera.movement_arrow()
    self.camera.movement_mouse()
    mouse_pos = pygame.mouse.get_pos()
    mouse_action = pygame.mouse.get_pressed()

    self.camera.movement_arrow()
    self.hud_manager["main"].update(mouse_pos, mouse_action)
    self.world.update(mouse_pos, mouse_action, self.camera)
    # draw
    self.world.draw(self.camera, self.game.screen)
    self.world.draw_grid(self.camera, self.game.screen)

    for hud in self.hud_manager.items():
        hud[1].draw(self.game.screen)

    pg.display.flip()


def SceneGameHandleEvents(self, event):
    if event.type in [pygame.KEYUP, pygame.KEYDOWN]:
        if event.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_DOWN, pygame.K_UP]:
            self.camera.keys[event.key] = not self.camera.keys[event.key]
        # elif event.unicode == '+':
        #     self.world.zoom += scaleDelta
        # elif event.unicode == '-':
        #     self.world.zoom = self.zoom - scaleDelta if self.world.zoom - \
        #         scaleDelta > 0 else self.world.zoom
    elif event.type == pygame.MOUSEMOTION:
        self.camera.mousePos = event.pos
        pass


SCENE = Scene(SCENE_GAME_ID, 'Scene_Menu', createFunc=SceneGameCreate,
              runFunc=SceneGameRun, handleEventsFunc=SceneGameHandleEvents)


class Camera:

    def __init__(self, width, height, boundary):

        self.width = width
        self.height = height

        self.keys = {
            pygame.K_UP: False,
            pygame.K_LEFT: False,
            pygame.K_DOWN: False,
            pygame.K_RIGHT: False,
        }
        self.boundary = boundary
        self.mousePos = (0, 0)
        self.scroll = pygame.Vector2(0, 0)
        self.scroll.x = -self.boundary[0]*0.4
        self.scroll.y = -self.boundary[1]*0.004
        self.mousseMouvSpeed = 20
        self.keyboardMouvSpeed = 20

    def movement_arrow(self):
        # print(f"scroll:{self.scroll.x,self.scroll.y}")

        if self.scroll.x > self.boundary[0]*0.05:
            self.scroll.x = self.boundary[0]*0.05
        elif self.scroll.x < -self.boundary[0]*0.775:
            self.scroll.x = -self.boundary[0]*0.775
        elif self.scroll.y > self.boundary[1]*0.08:
            self.scroll.y = self.boundary[1]*0.08
        elif self.scroll.y < -self.boundary[1]*0.75:
            self.scroll.y = -self.boundary[1]*0.75
        self.scroll.x += (self.keys[pygame.K_LEFT] -
                          self.keys[pygame.K_RIGHT])*self.keyboardMouvSpeed
        self.scroll.y += (self.keys[pygame.K_UP] -
                          self.keys[pygame.K_DOWN])*self.keyboardMouvSpeed

    def movement_mouse(self):

        # x movement# map boundary
        if self.scroll.x > self.boundary[0]*0.05:
            self.scroll.x = self.boundary[0]*0.05
        elif self.scroll.x < -self.boundary[0]*0.775:
            self.scroll.x = -self.boundary[0]*0.775
        elif self.scroll.y > self.boundary[1]*0.08:
            self.scroll.y = self.boundary[1]*0.08
        elif self.scroll.y < -self.boundary[1]*0.75:
            self.scroll.y = -self.boundary[1]*0.75

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


class World:

    def __init__(self, grid_l_x, grid_l_y, width, height, hud, world):
        # props
        self.grid_lx = grid_l_x
        self.grid_ly = grid_l_y
        self.width = width
        self.height = height
        self.hud = hud
        self.world = world
        self.boundary = [self.grid_lx *
                         TILE_SIZE * 2, self.grid_ly * TILE_SIZE]

        # rendering
        self.render = self.creation_surface()
        # etc
        self.temp_tile = None
        # self.zoom = 1

    def creation_surface(self):
        mapRender = pygame.Surface(
            (self.boundary[0], self.boundary[1]))
        for x in self.world:
            for building in x:
                building.map[0] += self.boundary[0]/2
                mapRender.blit(building.tileImage,
                               (building.map[0], building.map[1]))

        render = {"map": mapRender}
        return render

    def update(self, mouse_pos, mouse_action, camera):
        self.temp_tile = None
        if self.hud["main"].interaction != None:
            grid_pos = mouse_to_grid(
                mouse_pos[0]-self.boundary[0]*0.5, mouse_pos[1], camera.scroll)

            # print(f"grid{grid_pos}")
            if can_place_tile(self, grid_pos, mouse_pos):
                img = TEMP_TILE[self.hud["main"].interaction]
                img.set_alpha(100)

                render_pos = self.world.Building[grid_pos[0]][grid_pos[1]
                                                              ].map
                iso_poly = self.world.Building[grid_pos[0]][grid_pos[1]
                                                            ].iso_poly
                collision = self.world.Building[grid_pos[0]
                                                ][grid_pos[1]].collision
                # print(
                #     f"pos{iso_poly},collision{collision},name{self.world.Building[grid_pos[0]][grid_pos[1]]}")
                self.temp_tile = {
                    "image": img,
                    "render_pos": render_pos,
                    "iso_poly": iso_poly,
                    "collision": collision
                }
                if mouse_action[0] and not collision:
                    self.world.Building[grid_pos[0]].remove(
                        self.world.Building[grid_pos[0]][grid_pos[1]])
                    self.world.Building[grid_pos[0]].insert(grid_pos[1],
                                                            Housing((grid_pos[0], grid_pos[1])))

                    temp = self.world.Building[grid_pos[0]][grid_pos[1]]
                    temp.map[0] += self.boundary[0]/2
                    self.render["map"].blit(
                        temp.tileImage, (temp.map[0], temp.map[1]))
                    self.hud["main"].interaction = None

    def draw_grid(self, camera, screen):
        for x in self.world:
            for building in x:
                grid = building.iso_poly
                grid = [(x + self.boundary[0]/2 + camera.scroll.x, y+camera.scroll.y)
                        for x, y in grid]
                pygame.draw.polygon(screen, (0, 0, 0), grid, 1)

    def draw(self, camera, screen):
        screen.fill((0, 0, 0))
        # self.render["map"] = pygame.transform.scale(
        #     self.render["map"],  (self.render["map"].get_width(), self.render["map"].get_width()))
        screen.blit(self.render["map"],
                    (camera.scroll.x, camera.scroll.y))
        if self.temp_tile != None:
            iso_poly = self.temp_tile["iso_poly"]
            iso_poly = [(x + self.boundary[0]/2 +
                         camera.scroll.x, y + camera.scroll.y) for x, y in iso_poly]
            if self.temp_tile["collision"]:
                pygame.draw.polygon(screen, (255, 0, 0), iso_poly, 3)
            else:
                pygame.draw.polygon(screen, (255, 255, 255), iso_poly, 3)
            render_pos = self.temp_tile["render_pos"]
            screen.blit(
                self.temp_tile["image"],
                (
                    render_pos[0] + camera.scroll.x,
                    render_pos[1] + camera.scroll.y
                )
            )
