import os
import pathlib
import pickle
import shutil


class Save():
    def __init__(self, name):
        # NOTE : Carte temporaire
        self.layers = {
            "paths": [[1, 1, 1, 0, 0, 0, 0, 0, 0, 1],
                      [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
                      [1, 1, 1, 0, 0, 0, 0, 0, 0, 1],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                      [0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
                      [0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
                      [0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
                      [1, 1, 1, 1, 1, 1, 0, 0, 0, 1],
                      [0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
                      [0, 0, 0, 0, 0, 1, 0, 0, 0, 1]],
            "risk_feu": [[0]*10]*10,
            "Buildings": ""
        }
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
        
        

