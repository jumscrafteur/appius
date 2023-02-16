from Const import SCENES_IDS
from Game import Game
from Scenes import Scene1, Scene2

if __name__ == "__main__":
    g = Game()

    g.addScene(Scene1.SCENE)
    g.addScene(Scene2.SCENE)

    g.switchScene(SCENES_IDS["Scene1"])

    g.run()
