from Scene import Scene
from const import *
from .Scene_ids import SCENE_GAME_ID
from gamehud import *
import pygame
from World import World
from Camera import Camera
from Minimap import Minimap
from Evenement import Evenement


def SceneGameCreate(self):

    self.clock = pygame.time.Clock()
    self.hudup = Hudupper(0, 0, self.game.screen_width)
    self.hudleft = Hudbigleft(
        self.game.screen_width, self.game.screen_height)
    self.infofps = InfoShow(
        self.game.screen_width*0.5, 2, f"", 18, (255, 255, 255))
    self.infopop = InfoShow(
        self.game.screen_width*0.6, 2, f"Pop    xxxx", 18, (255, 255, 255))
    self.infoPO = InfoShow(
        self.game.screen_width*0.7, 2, f"PO    xxxx", 18, (255, 255, 255))

    self.hud_manager = {"up": self.hudup, "main": self.hudleft,
                        "fps": self.infofps, "pop": self.infopop, "Po": self.infoPO}

    # world
    self.world = World(40, 40, self.game.screen_width, self.game.screen_height,
                       self.hud_manager, self.game.save.map, self.game.save)
    # camera
    self.camera = Camera(self.game.screen_width,
                         self.game.screen_height, self.world.boundary)
    self.zoom = 1
    # tracking mouse action
    self.drag_start = None
    self.drag_end = None
    self.dragging = False
    # mini map
    self.mini_map = Minimap(
        self.world.boundary[0], self.world.boundary[1], 144, 111, self.world.world, ((self.game.screen_width - 154, 60)))
    self.counter = 0

    self.evenement = Evenement()


def SceneGameRun(self):

    #
    self.clock.tick(60)
    self.counter = int(self.game.tick/10)
    self.hud_manager["fps"].text = 'fps={}'.format(round(self.clock.get_fps()))
    self.hud_manager["Po"].text = 'Po={}'.format(round(self.game.save.PO))
    # update
    self.camera.movement_arrow()
    # self.camera.movement_mouse()
    mouse_pos = pygame.mouse.get_pos()
    mouse_action = pygame.mouse.get_pressed()

    self.camera.movement_arrow()
    self.hud_manager["main"].update(mouse_pos, mouse_action)
    self.world.update(self.drag_start, self.drag_end,
                      mouse_pos, mouse_action, self.camera, self.mini_map)

    self.mini_map.update_mode_interactive(mouse_pos, mouse_action, self.camera)
    self.world.update_live_event()

    # DRAW TO MAP
    # 1er layer: draw only grass and roads
    self.world.layer_1_draw(self.camera, self.game.screen)
    # ----------------------------------------------
    # 2nd layer: draw walker

    # --------------------------------------------------
    # 3rd layer: draw tree,mountain,rock,  and building
    self.world.layer_3_draw(self.camera, self.game.screen, self.counter)
    # --------------------------------
    # 4th layer : draw temporary changement (when we build in drag & drop)
    self.world.layer_4_draw(self.camera, self.game.screen)
    # self.world.draw_grid(self.camera, self.game.screen)

    for hud in self.hud_manager.items():
        hud[1].draw(self.game.screen)
    # mini_map
    self.mini_map.draw(self.game.screen, self.camera)
    # print(f"game tick{self.counter}")
    self.evenement.update(self.world.world)
    pg.display.flip()


def SceneGameHandleEvents(self, event):
    if event.type in [pygame.KEYDOWN]:
        if event.unicode == 'g':
            if self.world.grid:
                self.world.grid = False
            else:
                self.world.grid = True
        elif event.unicode == 'n':
            self.world.overlay_mode = "normal"
        elif event.unicode == 'f':
            self.world.overlay_mode = "fire"
    if event.type in [pygame.KEYUP, pygame.KEYDOWN]:
        if event.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_DOWN, pygame.K_UP]:
            self.camera.keys[event.key] = not self.camera.keys[event.key]
        # elif event.unicode == '+':
        #     self.world.zoom += scaleDelta
        # elif event.unicode == '-':
        #     self.world.zoom = self.zoom - scaleDelta if self.world.zoom - \
        #         scaleDelta > 0 else self.world.zoom
    elif event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
            self.drag_start = event.pos

    elif event.type == pygame.MOUSEBUTTONUP:
        if event.button == 1:
            self.drag_start = None
            self.drag_end = None
    elif event.type == pygame.MOUSEMOTION:
        self.camera.mousePos = event.pos
        self.drag_end = event.pos


SCENE = Scene(SCENE_GAME_ID, 'Scene_Menu', createFunc=SceneGameCreate,
              runFunc=SceneGameRun, handleEventsFunc=SceneGameHandleEvents)
