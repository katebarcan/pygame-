import pygame as pg
import random

FPS = 60
WIDTH, HEIGHT = 800, 600

SHIP_SIZE = (100, 100)
ASTEROID_SIZE = (100, 100)
FIREBALL_SIZE = (25, 50)

class Ship(pg.sprite.Sprite):
    speed = 6

    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(r"images\ship.png").convert_alpha()
        self.image = pg.transform.scale(self.image, SHIP_SIZE)
        self.rect = self.image.get_rect(center=(WIDTH / 2, HEIGHT / 2))
        self.mask = pg.mask.from_surface(self.image)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self, dx=0, dy=0):
        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed


class Asteroid(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(r"images\asteroid.png").convert_alpha()
        self.image = pg.transform.scale(self.image, ASTEROID_SIZE)
        self.rect = self.image.get_rect(center=(x, y))
        self.mask = pg.mask.from_surface(self.image)
        self.speed = random.randint(2, 4)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.kill()





pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Игра")
clock = pg.time.Clock()

# здесь происходит создание игровых объектов:
# ...

# если надо до игрового цикла (=на самом старте игры) отобразить объекты, то отрисовываем их здесь:
# ...
pg.display.update()


flag_play = True
while flag_play:
    clock.tick(FPS)


    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            flag_play = False
            break
    if not flag_play:
        break

    # изменение характеристик объектов:
    # ...

    # перерисовка экрана:
    # ...

    pg.display.update()
