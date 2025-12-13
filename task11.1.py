import pygame as pg
import random

FPS = 60
WIDTH, HEIGHT = 1000, 600

class Car(pg.sprite.Sprite):
    speed = 5

    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(r"images\car.png").convert_alpha()
        self.rect = self.image.get_rect(center=(WIDTH / 2, HEIGHT / 2))
        self.mask = pg.mask.from_surface(self.image)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self, dx=0, dy=0):
        if (self.rect.left + dx * self.speed) > 0 and (self.rect.right + dx * self.speed) < WIDTH:
            self.rect.x += dx * self.speed
        if (self.rect.top + dy * self.speed) > 0 and (self.rect.bottom + dy * self.speed) < HEIGHT:
            self.rect.y += dy * self.speed

class EnemyCar(pg.sprite.Sprite):

    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        images = [r"images\car2.png", r"images\car3.png", r"images\car4.png"]
        selected_image = random.choice(images)
        self.image = pg.image.load(selected_image).convert_alpha()
        self.rect = self.image.get_rect(center=())
        self.mask = pg.mask.from_surface(self.image)



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
