import os
from enum import IntEnum

import pygame


class SceneIds(IntEnum):
    Title = 0
    Menu = 1
    Scene1 = 98
    Scene2 = 99


class CustomEvent:
    SwitchScene = pygame.event.custom_type()


ASSET_PATH = os.path.join(os.path.dirname(__file__), "..", "assets")
