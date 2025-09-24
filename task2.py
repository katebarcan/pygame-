import pygame as pg

FPS = 60
WIN_WIDTH = 400
WIN_HEIGHT = 100
WHITE = (255, 255, 255)
ORANGE = (255, 150, 100)

pg.init()
sc = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
sc.fill(WHITE)
pg.display.set_caption("Игра")
clock = pg.time.Clock()

r = 30
x = 10
y = WIN_HEIGHT // 2 - 25
pg.draw.rect(sc, ORANGE, (x, y, 40, 40))
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

    
    if x == WIN_WIDTH:
        x -= 2  # перемещаем его за левую
    else:  # если еще нет
        x += 2  # то на следующей итерации цикла круг отобразится немного правее

    sc.fill(WHITE)  # заливаем фон, стирая предыдущий круг
    pg.draw.rect(sc, ORANGE, (x, y, 40, 40))  # рисуем новый, сдвинутый круг

    pg.display.update() 
