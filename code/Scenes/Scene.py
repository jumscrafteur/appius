class Scene():
    def __init__(self, id, name,
                 createFunc=lambda scene: None,
                 runFunc=lambda scene: None,
                 destroyFunc=lambda scene: None
                 ):
        self.name = name
        self.id = id
        self.game = None
        self.createFunc = createFunc
        self.runFunc = runFunc
        self.destroyFunc = destroyFunc

        self.images = {}
        self.buttons = {}

    def create(self, game):
        self.game = game
        self.createFunc(self)
        return

    def run(self) -> None:
        self.runFunc(self)

    def destroy(self) -> None:
        self.destroyFunc(self)
