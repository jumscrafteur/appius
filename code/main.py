from Game import Game
from Scenes import Scene_PreMenu, Scene_menu

if __name__ == '__main__':
    g = Game("")

    g.addScene(Scene_PreMenu.SCENE)
    g.addScene(Scene_menu.SCENE)

    g.run()
