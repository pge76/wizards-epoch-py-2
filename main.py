import pygame as pg
import sys
from settings import *
from player import Player
from wall import Wall
from sprites import *


class Game:

    def __init__(self):
        pg.init()
        pg.display.set_caption(TITLE)
        pg.key.set_repeat(KEY_REPEAT_START, KEY_REPEAT_INTERVAL) # quick and dirty

        self.player = None
        self.walls = pg.sprite.Group()
        self.dt = 0
        self.all_sprites = None
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()
        self.playing = True

        self.load_data()

    def load_data(self):
        pass

    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.player = Player(self, 10, 10)
        for x in range(10,20):
            Wall(self, x, 20)

    def run(self):
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        self.all_sprites.update()

    def draw(self):
        self.screen.fill(BGCOLOR)
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        pg.display.flip()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
                if event.key == pg.K_w:
                    self.player.move(dy=-1)
                if event.key == pg.K_a:
                    self.player.move(dx=-1)
                if event.key == pg.K_d:
                    self.player.move(dx=1)
                if event.key == pg.K_s:
                    self.player.move(dy=1)

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))


# create the game object
g = Game()
while True:
    g.new()
    g.run()
