import pygame as pg
FPS = 60
WIDTH, HEIGHT = 1000, 600

ORANGE = (235, 210, 155)
BLUE = (166, 200, 237)
BROWN = (189, 165, 123)
YELLOW = (231, 240, 55)
CYAN = (197, 240, 240)


pg.init()
sc = pg.display.set_mode((WIDTH, HEIGHT))
sc.fill(BLUE)
pg.display.set_caption("Игра")
clock = pg.time.Clock()

pg.draw.rect(sc, ORANGE, (WIDTH / 2, HEIGHT / 2, 200, 250))
pg.draw.polygon(sc, BROWN, [[WIDTH / 2, HEIGHT / 2], [WIDTH / 2 + 200, HEIGHT / 2], [WIDTH / 2 + 100, HEIGHT / 2 - 100]])
pg.draw.circle(sc, YELLOW, (100, 100), 70)
pg.draw.circle(sc, CYAN, (100, 250), 30)
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

    # изменение объектов
    # ...

    # обновление экрана
    pg.display.update()
