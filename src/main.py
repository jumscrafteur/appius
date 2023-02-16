from Const import SceneIds
from Game import Game
from Scenes import Scene1, Scene2

if __name__ == "__main__":
    g = Game()

    g.addScene(Scene1.SCENE)
    g.addScene(Scene2.SCENE)

    g.switchScene(SceneIds.Scene1)

    g.run()
