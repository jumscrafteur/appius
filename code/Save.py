class Save():
    def __init__(self):
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
            "risk_feu": [[0]*10]*10
        }
        self.walkers = []
        self.pop = 0
        self.PO = 0
        self.date = 0
        self.desirability = 0
        self.religions = {}
        self.name
        self.size = 0

    def serialize(self):
        # TODO : https://www.notion.so/Syst-me-de-sauvegarde-d5fece67d098448b8737b92e4dd3f8c1
        return

    def deserialize(self):
        # TODO : https://www.notion.so/Syst-me-de-sauvegarde-d5fece67d098448b8737b92e4dd3f8c1
        return
