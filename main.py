import pygame as pg
import sys

# WIN_SIZE = WIDTH, HEIGHT = 1920, 1080
# WIN_SIZE = WIDTH, HEIGHT = 1280, 720
WIN_SIZE = WIDTH, HEIGHT = 720, 480
pg.init()


class App:
    def __init__(self):
        self.screen = pg.display.set_mode(size=WIN_SIZE)
        self.clock = pg.time.Clock()

    def update(self):
        self.clock.tick(60)
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')

    def draw(self):
        self.screen.fill('black')
        pg.display.flip()

    def run(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
            self.update()
            self.draw()


if __name__ == '__main__':
    app = App()
    app.run()
