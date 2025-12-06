import pygame as pg

FPS = 60
WIN_WIDTH, WIN_HEIGHT = 1000, 600
WHITE, BLACK = (255, 255, 255), (0, 0, 0)
GREEN_MINT = (225, 247, 228)

class Car:
    speed = 5

    def __init__(self):
        self.car_surf = pg.image.load(r"images\car.png").convert_alpha()
        self.car_rect = self.car_surf.get_rect(center=(WIN_WIDTH / 2, WIN_HEIGHT / 2))
        self.direction = "up"

    def rotate(self, new_direction):
        # self.direction = "up", new_direction="left" => +90
        # self.direction = "up", new_direction="right" => +270
        # self.direction = "up", new_direction="bottom" => +180
        #



    def draw(self, screen):
        screen.blit(self.car_surf, self.car_rect)


pg.init()
screen = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pg.display.set_caption("Игра")
clock = pg.time.Clock()

my_car = Car()

screen.fill(GREEN_MINT)
my_car.draw(screen)
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



    screen.fill(GREEN_MINT)
    my_car.draw(screen)
    pg.display.update()
