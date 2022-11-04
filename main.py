from os.path import join

import pygame as pg
import sys
from os import path
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
        self.level_data = []

        self.load_data()

    def new(self):
        self.all_sprites = pg.sprite.Group()
        for row, tiles in enumerate(self.level_data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    Wall(self, col, row)
                if tile == 'P':
                    self.player = Player(self, col, row)


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

    def load_data(self):
        game_folder = path.dirname(__file__)
        file = path.join(game_folder, 'level', 'level.txt')
        with open(file, 'rt') as f:
            for line in f:
                self.level_data.append(line)

# create the game object
g = Game()
while True:
    g.new()
    g.run()
