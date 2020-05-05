import pygame
import random
import math

SCREEN_DIM = (800, 600) 

class Vec2d:
    """x,y - координаты, speed - speed_x, speed_y"""
    def __init__(self, x, y, speed_x=0, speed_y=0):
        self.x = x
        self.y = y
        
        if speed_x == 0:
            self.speed_x = random.random() * 0.2
        else:
            self.speed_x = speed_x

        if speed_y == 0:
            self.speed_y = random.random() * 0.2
        else:
            self.speed_y = speed_y

    def __add__(self, obj):
        self.x += obj.x
        self.y += obj.y

    def __sub__(self, obj):
        self.x -= obj.x
        self.y -= obj.y

    def __mul__(self, k):
        self.x = self.x * k
        self.y = self.y * k

    def __len__(self):
        return math.sqrt(self.x * self.x + self.y * self.y)

    def vec(self):
        return ( (int(self.x), int(self.y)) )
        
    def step(self):
        self.x += self.speed_x
        self.y += self.speed_y

class Polyline:
    """Инициализирует списком Vec2d и кол-вом точек сглаживания"""
    def __init__(self, points=[], count=3):
        self.points = points
        self.count = count

    """Добавляет в ломаную точку Vec2d"""
    def append(self, point):
        self.points.append(point)
        print("Appended {}, {}".format(point.x, point.y))

    """Перерасчёт координат опорных точек"""
    def set_points(self):
        for p in range(len(self.points)):
            self.points[p].step()

            if self.points[p].x > SCREEN_DIM[0] or self.points[p].x < 0:
                self.points[p].speed_x = -self.points[p].speed_x

            if self.points[p].y > SCREEN_DIM[1] or self.points[p].y < 0:
                self.points[p].speed_y = -self.points[p].speed_y

    """Отрисовка ломаной"""
    def draw_points(self, gameDisplay, color=(255,255,255), width=3):
        for p in self.points:
            pygame.draw.circle(gameDisplay, color, p.vec(), width)

class Knot(Polyline):
    pass


# =======================================================================================
# Основная программа
# =======================================================================================
if __name__ == "__main__":
    pygame.init()
    gameDisplay = pygame.display.set_mode(SCREEN_DIM)
    pygame.display.set_caption("MyScreenSaver")

    steps = 20
    working = True
    show_help = False
    pause = True

    hue = 0
    color = pygame.Color(0)

    line = Polyline(count=steps)

    while working:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                working = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    working = False
                if event.key == pygame.K_r:
                    # TODO: re-initialize Polyline
                    points = []
                    speeds = []
                if event.key == pygame.K_p:
                    pause = not pause
                if event.key == pygame.K_q:
                    working = False
                if event.key == pygame.K_KP_PLUS:
                    steps += 1
                #if event.key == pygame.K_F1:
                #   show_help = not show_help
                if event.key == pygame.K_KP_MINUS:
                    steps -= 1 if steps > 1 else 0

            if event.type == pygame.MOUSEBUTTONDOWN:
                point = Vec2d(event.pos[0], event.pos[1])
                line.append(point)

        gameDisplay.fill((0, 0, 0))
        hue = (hue + 1) % 360
        color.hsla = (hue, 100, 50, 100)

        line.draw_points(gameDisplay)

        if not pause:
            line.set_points()

        pygame.display.flip()

    pygame.display.quit()
    pygame.quit()
    exit(0)
