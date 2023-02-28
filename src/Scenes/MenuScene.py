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
    AssetManager.createPanel("panel", 20, 22)

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

    btnLayout = GenerateGridLayout(
        self.game.screen.get_width() // 2,
        self.game.screen.get_height() // 2,
        len(panelBtnList),
        len(panelBtnList[0]),
        0,
        16,
        panelBtnSize[0] * panelBtnTheme["tileSize"][0],
        panelBtnSize[1] * panelBtnTheme["tileSize"][1],
    )

    for row in panelBtnList:
        for button in row:
            self.buttons.append(
                AssetManager.ButtonText(
                    panelBtnTheme,
                    next(btnLayout),
                    panelBtnSize,
                    button[0],
                    button[1],
                )
            )

    # testBtn = AssetManager.ButtonText(
    #     AssetManager.BUTTON_TYPES.PRIMARY,
    #     btnLayout.__next__(),
    #     (12, 1),
    #     "mon bouton 1",
    #     lambda: pygame.event.post(
    #         pygame.event.Event(CustomEvent.SwitchScene, {"id": SceneIds.Title})
    #     ),
    # )

    # testBtn2 = AssetManager.ButtonText(
    #     AssetManager.BUTTON_TYPES.PRIMARY,
    #     btnLayout.__next__(),
    #     (12, 1),
    #     "mon bouton 2",
    #     lambda: pygame.event.post(
    #         pygame.event.Event(CustomEvent.SwitchScene, {"id": SceneIds.Title})
    #     ),
    # )

    # self.buttons.append(testBtn)
    # self.buttons.append(testBtn2)

    drawCenter(self.game.screen, AssetManager.get("menu_background"))
    drawCenter(self.game.screen, AssetManager.get("panel"))


def run(self: Scene):
    assert self.game

    for button in self.buttons:
        button.render(self.game.screen)

    pass


def event(self: Scene, event: pygame.event.Event):
    if event.type == pygame.MOUSEBUTTONDOWN:
        for button in self.buttons:
            button.checkClick()
    elif event.type == pygame.MOUSEMOTION:
        for button in self.buttons:
            button.checkOver()


SCENE = Scene(SceneIds.Menu, createFunc=create, runFunc=run, handleEventsFunc=event)
