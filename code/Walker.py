class Walker():
    def __init__(self, save):
        self.range = 0
        self.building = None
        self.type = None
        # TODO : change to a map class
        self.map = None
        self.path = []
        self.dir = (0, 0)
        self.pos = (0, 0)

    def move():
        # TODO :https://www.notion.so/Syst-me-de-mouvement-d89eda3bfd07423aac03172de8d46827
        return

    def work():
        # NE PAS MODIFIER
        return


class Engineer(Walker):
    def __init__(self, save):
        Walker.__init__(self, save)
        self.type = "Engineer"

    def work():
        # TODO : https://www.notion.so/Syst-me-de-metier-bf7209c3a02f48bfb3ebee1af0316be7
        return


print("iness test")