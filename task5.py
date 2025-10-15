import random
import pygame as pg

FPS = 60
WIDTH, HEIGHT = 600, 500
MINT = (230, 254, 212)
ORANGE = (255, 150, 100)

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Игра")
clock = pg.time.Clock()


r = 30
x, y = random.randint(r, WIDTH - r), random.randint(r, HEIGHT - r)
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

    pressed = pg.mouse.get_pressed()
    if pressed[1]:
        pos = pg.mouse.get_pos()
    dist = ((pos[0] - x) ** 2 + (pos[1] - y) ** 2) ** 0.5
    if dist >= r:





    screen.fill(MINT)
    pg.draw.circle(screen, ORANGE, (x, y), r)

    pg.display.update()
