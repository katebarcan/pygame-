import pygame as pg
FPS = 60
WIN_WIDTH, WIN_HEIGHT = 1000, 600
WHITE, BLACK = (255, 255, 255), (0, 0, 0)
GREEN_MINT = (225, 247, 228)

pg.init()
screen = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pg.display.set_caption("Игра")
pg.display.set_icon(pg.images.load(r"images\icon.ico"))
clock = pg.time.Clock()

car_surf = pg.image.load(r"images\car_processed.png").convert_alpha()
car_rect = car_surf.get_rect(center=(WIN_WIDTH / 2, WIN_HEIGHT / 2))

screen.fill(GREEN_MINT)
screen.blit(car_surf, car_rect)
pg.display.update()
pg.time.wait(2 * 1000)
