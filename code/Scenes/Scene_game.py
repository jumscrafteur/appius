from Scene import Scene
from .Scene_ids import SCENE_GAME_ID
from map_init.game.map import MapGame
import pygame


# NOTE de Hugo : Variable pour que je puisse debug sans casser le code pour vous.
REFACTO_HUGO = False


def SceneGameCreate(self):
    self.map = MapGame(self.game.screen, pygame.time.Clock())


def SceneGameRun(self):
    if not REFACTO_HUGO:
        self.map.run()
    else:
        return

    self.game.screen.fill((0, 0, 0))
    self.game.screen.blit(self.map.world.land_tile,
                          (self.map.camera.scroll.x, self.map.camera.scroll.y))

    for y in range(len(self.game.save.map)):
        for x in range(len(self.game.save.map[y])):

            render_pos = self.map.world.world[x][y]["render_pos"]

            if self.map.world.world[x][y]["tile"]["name"] != "":
                name_tile = self.map.world.world[x][y]["tile"]["name"]
                offset = self.map.world.world[x][y]["tile"]["offset"]
                self.game.screen.blit(self.map.world.tiles[name_tile], (
                    render_pos[0]+self.map.world.land_tile.get_width() *
                    0.5 + self.map.camera.scroll.x,
                    render_pos[1]+self.map.world.land_tile.get_height()*0 - offset + self.map.camera.scroll.y))

            p = self.map.world.world[x][y]["iso_poly"]
            p = [(x + self.map.world.land_tile.get_width() *
                  0.5 + self.map.camera.scroll.x, y + self.map.world.land_tile.get_height()*0+self.map.camera.scroll.y) for x, y in p]

    self.map.hudleft.draw(self.game.screen)
    self.map.hudstick.draw(self.game.screen)
    self.map.hudup.draw(self.game.screen)
    self.map.infofps.draw(self.game.screen)
    self.map.infopop.draw(self.game.screen)

    pygame.display.flip()
    pass


def SceneGameHandleEvents(self, event):
    pass


SCENE = Scene(SCENE_GAME_ID, 'Scene_Menu', createFunc=SceneGameCreate,
              runFunc=SceneGameRun)
