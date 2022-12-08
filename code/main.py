from Game import Game
from Scenes import Scene_PreMenu

if __name__ == '__main__':
    g = Game("")

    g.addScene(Scene_PreMenu.SCENE)

    g.run()
