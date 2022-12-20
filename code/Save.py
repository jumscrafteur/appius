import os
import pathlib
import pickle

from Building import *


class Save():
    def __init__(self, name):
        # NOTE : Carte temporaire
        self.map = Buildings()
        for y in range(40):
            for x in range(40):
                self.map.ajouter(Grass((x, y)))
        self.walkers = []
        self.pop = 0
        self.PO = 0
        self.date = 0
        self.desirability = 0
        self.religions = {}
        self.name = name
        self.size = 0

    def serialize(self):
        path = pathlib.PurePath(os.path.dirname(
            os.path.abspath(__file__)), "../saves")
        with open(pathlib.Path(path, f"{self.name}.save"), "wb") as f:
            pickle.dump(self, f)

    @staticmethod
    def deserialize(path: str) -> object:
        with open(path, "rb") as f:
            return pickle.load(f)

    @staticmethod
    def getSavesNames():
        path = pathlib.PurePath(os.path.dirname(
            os.path.abspath(__file__)), "../saves")

        return [
            fileName.split(".")[0]
            for fileName in os.listdir(path)
            if fileName.endswith(".save")]
