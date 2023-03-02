import AssetManager
import pygame
from Const import CustomEvent, SceneIds
from LayoutManager import GenerateGridLayout, drawCenter
from Scene import Scene


def create(self: Scene):
    assert self.game

    AssetManager.load("menu_background", "0/fired/00001.png")
    AssetManager.transform(
        "menu_background", lambda asset: pygame.transform.scale_by(asset, 1.5)
    )

    p = AssetManager.Panel(True)

    AssetManager.createPanelBackground("panel", 20, 22)
    p.setBackground("panel")

    panelBtnSize = (17, 1)
    panelBtnTheme = AssetManager.BUTTON_TYPES.PRIMARY

    panelBtnList = [
        [
            (
                "Start new career",
                lambda: pygame.event.post(
                    pygame.event.Event(CustomEvent.SwitchScene, {"id": SceneIds.Title})
                ),
            ),
            (
                "Load saved game",
                lambda: pygame.event.post(
                    pygame.event.Event(CustomEvent.SwitchScene, {"id": SceneIds.Title})
                ),
            ),
            (
                "City Construction Kit",
                lambda: pygame.event.post(
                    pygame.event.Event(CustomEvent.SwitchScene, {"id": SceneIds.Title})
                ),
            ),
            (
                "Caesar III assignment editor",
                lambda: pygame.event.post(
                    pygame.event.Event(CustomEvent.SwitchScene, {"id": SceneIds.Title})
                ),
            ),
            (
                "Options",
                lambda: pygame.event.post(
                    pygame.event.Event(CustomEvent.SwitchScene, {"id": SceneIds.Title})
                ),
            ),
            (
                "Exit",
                self.game.end,
            ),
        ]
    ]

    assert p.backgroundSurfaceAsset

    panelBgSurface = AssetManager.get(p.backgroundSurfaceAsset)

    btnLayout = GenerateGridLayout(
        panelBgSurface.get_width() // 2,
        panelBgSurface.get_height() // 2,
        len(panelBtnList),
        len(panelBtnList[0]),
        0,
        16,
        panelBtnSize[0] * panelBtnTheme["tileSize"][0],
        panelBtnSize[1] * panelBtnTheme["tileSize"][1],
    )

    for row in panelBtnList:
        for button in row:
            p.addButton(
                AssetManager.ButtonText(
                    panelBtnTheme,
                    next(btnLayout),
                    panelBtnSize,
                    button[0],
                    button[1],
                )
            )

    self.panels.append(p)


def run(self: Scene):
    assert self.game
    drawCenter(self.game.screen, AssetManager.get("menu_background"))

    for button in self.buttons:
        button.render(self.game.screen)

    for panel in self.panels:
        panel.render(self.game.screen)

    pass


def event(self: Scene, event: pygame.event.Event):
    if event.type == pygame.MOUSEBUTTONDOWN:
        for panel in self.panels:
            panel.checkClick()
        for button in self.buttons:
            button.checkClick()

    elif event.type == pygame.MOUSEMOTION:
        for button in self.buttons:
            button.checkOver()
        for panel in self.panels:
            panel.checkOver()

    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            self.panels[0].setVisibility(not self.panels[0].visible)


SCENE = Scene(SceneIds.Menu, createFunc=create, runFunc=run, handleEventsFunc=event)
