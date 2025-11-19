import pygame as pg
import random

FPS = 60
WIN_WIDTH, WIN_HEIGHT = 1000, 600
RED = (194, 0, 0)

class Food:
    SIZE = 40

    def __init(self):
        self.random_size = random.randint(5, 20)
        random_x, random_y = random.randint(self.random_size, WIN_WIDTH - self.random_size), random.randint(self.random_size, WIN_HEIGHT - self.random_size)

        self.surf = pg.Surface((Food.SIZE * 2, Food.SIZE * 2), pg.SRCALPHA)
        self.rect = self.surf.get_rect(center=(random_x, random_y))
        self.surf.fill((0, 0, 0, 0))
        pg.draw.circle(self.surf, (*RED, 255), (self.rect.width / 2, self.rect.height / 2), self.size)

        self.active = True
        self.mask = pg.mask.from_surface(self.surf)

    def draw(self, screen):
        screen.blit(self.surf, self.rect)

class Player:
    COLOR = (27, 4, 143)
    WIDTH, HEIGHT = 150, 250
    SPEED = 3

    def __init__(self):
        self.surf = pg.Surface((Player.WIDTH, Player.HEIGHT), pg.SRCALPHA)
        self.rect = self.surf.get_rect(center=(WIN_WIDTH / 2, WIN_HEIGHT / 2))
        self.surf.fill((0, 0, 0, 0))
        pg.draw.circle(self.surf, (*Player.COLOR, 255),(self.rect.width / 2, self.rect.height / 3 - 30), 30)

        self.speed = Player.SPEED
        self.mask = pg.mask.from_surface(self.surf) 
        
    def move(self, dx=0, dy=0):
        if self.rect.left + dx * self.speed) > 0 and 
