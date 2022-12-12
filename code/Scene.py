import pygame


class Scene():
    def __init__(self, id, name,
                 createFunc=lambda scene: None,
                 runFunc=lambda scene: None,
                 destroyFunc=lambda scene: None,
                 handleEventsFunc=lambda scene, event, : None
                 ):
        self.name = name
        self.id = id
        self.game = None
        self.createFunc = createFunc
        self.runFunc = runFunc
        self.destroyFunc = destroyFunc
        self.handleEventsFunc = handleEventsFunc

        self.images = {}
        self.buttons = {}
        self.box = {}

    def create(self, game):
        self.game = game
        self.createFunc(self)
        return

    def run(self):
        self.runFunc(self)

    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.end()
            for clé in self.box.keys():
                    self.box[clé].handle_event(event)
            if event.type == pygame.MOUSEBUTTONDOWN:
                for key in self.buttons.keys():
                    self.buttons[key].MouseonButton(event.pos)
            if event.type == pygame.USEREVENT:
                event.action()

            self.handleEventsFunc(self, event)

    def destroy(self):
        self.destroyFunc(self)
