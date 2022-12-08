import pygame


class Game():
    def __init__(self, save):
        pygame.init()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

        [(self.screen_width, self.screen_height
          )] = pygame.display.get_desktop_sizes()

        self.save = save

        self.actualScene = None
        self.running = True
        self.sceneMap = {}

    def addScene(self, scene) -> None:
        if scene.id in self.sceneMap.keys():
            raise Exception(
                f"The scene {self.sceneMap[scene.id]} already have id : {scene.id}")

        if self.actualScene == None:
            self.actualScene = scene.id

        self.sceneMap[scene.id] = scene

    def run(self):
        while self.running:

            # Verifie if the scene selected exist
            if self.actualScene not in self.sceneMap.keys():
                raise Exception(
                    f"Invalid Scene ID ({self.actualScene}) valid : [{self.sceneMap.keys()}]")

            # Change the scene to the selected scene
            scene = self.sceneMap[self.actualScene]

            # Initialise the scene
            scene.create(self)

            # Run the scene
            while self.actualScene == scene.id:
                scene.run()

            # End the scene
            scene.destroy()
