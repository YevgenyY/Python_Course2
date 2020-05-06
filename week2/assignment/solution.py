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
        r = Vec2d(self.x + obj.x, self.y + obj.y, self.speed_x + obj.speed_x, self.speed_y + obj.speed_y)

        return r

    def __sub__(self, obj):
        r = Vec2d(self.x - obj.x, self.y - obj.y, self.speed_x - obj.speed_x, self.speed_y - obj.speed_y)

        return r

    def __mul__(self, k):
        r = Vec2d(self.x *k, self.y * k, self.speed_x, self.speed_y)

        return r

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
        self.smooth = [] # List для точек сглаживания

    """Добавляет в ломаную точку Vec2d"""
    def append(self, point):
        self.points.append(point)

    """Отрисовка опорных точек"""
    def draw_points(self, gameDisplay, color=(255,255,255), width=3):
        for p in self.points:
            pygame.draw.circle(gameDisplay, color, p.vec(), width)

    """Отрисовка ломаной"""
    def draw_line(self, gameDisplay, color=(255,255,255), width=3):
        for p_n in range(-1, len(self.smooth) - 1):
                pygame.draw.line(gameDisplay, color,
                    ( int(self.smooth[p_n].x), int(self.smooth[p_n].y) ),
                    ( int(self.smooth[p_n + 1].x), int(self.smooth[p_n+1].y) ),
                    width)


    def reset(self):
        self.points=[]

class Knot(Polyline):
    def get_point(self, points, alpha, deg=None):
        if deg is None:
            deg = len(points) - 1
        if deg == 0:
            return points[0]
        return (points[deg] * alpha) + ( self.get_point(points, alpha, deg - 1) * (1-alpha) )

    def get_points(self, base_points, count):
        alpha = 1 / count
        res = []
        for i in range(count):
            res.append(self.get_point(base_points, i * alpha))

        return res

    def set_points(self):
        """Перерасчёт координат опорных точек"""
        for p in range(len(self.points)):
            self.points[p].step()

            if self.points[p].x > SCREEN_DIM[0] or self.points[p].x < 0:
                self.points[p].speed_x = -self.points[p].speed_x

            if self.points[p].y > SCREEN_DIM[1] or self.points[p].y < 0:
                self.points[p].speed_y = -self.points[p].speed_y

        """Перерасчёт координат точек сглаживания"""
        if len(self.points) < 3:
            return

        self.smooth = []

        points = self.points.copy()

        for i in range(-2, len(points) -2):
            ptn = []
            ptn.append( (points[i] + points[i + 1]) * 0.5 )
            ptn.append( points[i + 1] )
            ptn.append( (points[i + 1] + points[i + 2]) * 0.5 )

            self.smooth.extend(self.get_points(ptn, self.count))


# =======================================================================================
# Основная программа
# =======================================================================================
if __name__ == "__main__":
    pygame.init()
    gameDisplay = pygame.display.set_mode(SCREEN_DIM)
    pygame.display.set_caption("MyScreenSaver")

    steps = 34 
    working = True
    show_help = False
    pause = True

    hue = 0
    color = pygame.Color(0)

    line = Knot(count=steps)

    while working:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                working = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    working = False
                if event.key == pygame.K_r:
                    # re-initialize Polyline
                    line.reset()
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
                line.set_points()

        gameDisplay.fill((0, 0, 0))
        hue = (hue + 1) % 360
        color.hsla = (hue, 100, 50, 100)

        line.draw_points(gameDisplay)
        line.draw_line(gameDisplay)

        if not pause:
            line.set_points()

        pygame.display.flip()

    pygame.display.quit()
    pygame.quit()
    exit(0)
