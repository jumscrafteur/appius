from Const import SceneIds
from Game import Game
from Scenes import MenuScene, Scene1, Scene2, TitleScene

if __name__ == "__main__":
    g = Game()

    g.addScene(Scene1.SCENE)
    g.addScene(Scene2.SCENE)
    g.addScene(TitleScene.SCENE)
    g.addScene(MenuScene.SCENE)

    g.switchScene(SceneIds.Title)

    g.run()
