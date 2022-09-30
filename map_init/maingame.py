import pygame as pg
from game.game import Game

SCREENSIZE = WIDTH, HEIGHT = 1200, 800


def main():

    running = True
    playing = True

    pg.init()
    pg.mixer.init()
    screen = pg.display.set_mode(SCREENSIZE)
    clock = pg.time.Clock()

    # implement menu
    # implement game
    game = Game(screen, clock)
    while running:
        # menu

        while playing:
            # game loop
            game.run()


if __name__ == "__main__":
    main()
