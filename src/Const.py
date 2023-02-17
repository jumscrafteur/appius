import os
from enum import Enum


class SceneIds(Enum):
    Title = 0
    Menu = 1
    Scene1 = 98
    Scene2 = 99


ASSET_PATH = os.path.join(os.path.dirname(__file__), "..", "assets")
