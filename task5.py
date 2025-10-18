import pygame as pg

FPS = 60
WIDTH, HEIGHT = 1000, 600
CANNON_WIDTH, CANNON_HEIGHT = * 1 / 4, HEIGHT * 1 / 4
MINT = (230, 254, 212)
ORANGE = (255, 150, 100)
BROWN = (87, 20, 8)
GRAY = (186, 184, 182)

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Игра")
clock = pg.time.Clock()

background = pg.Surface((WIDTH, HEIGHT))
background.fill(BROWN)
pg.draw.rect(background, GRAY, (0, 100, WIDTH, 120))
pg.draw.rect(background, GRAY, (0, 350, WIDTH, 120))

cannon = pg.Surface((CANNON_WIDTH, CANNON_HEIGHT), pg.SRCALPHA)
cannon.fill((0, 0, 0, 0))
pg.draw.

screen.blit(background, (0, 0))
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

    screen.blit(background, (0, 0))
    pg.display.update()
