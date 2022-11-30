import pygame, sys, math, random


pygame.init()
clock = pygame.time.Clock()

screenx,screeny = 1000,800

window = pygame.display.set_mode([screenx,screeny])
pygame.display.set_caption("Flocking boids")

class Boid:
    def __init__(self, x, y):
        self.pos = pygame.math.Vector2(x,y)

        self.r = 5
        self.color = (255,255,255)

        self.set_dist = 15
        self.set_angle = 50

    def check_area(self, other):
        self.distance = self.pos - other.pos
        self.angle = math.atan(self.distance.y / self.distance.x)

        if self.distance.magnitude() <= self.set_dist and (self.angle >= self.set_angle or self.angle >= -self.set_angle):
            print("yes")
            return True

    def draw(self, window):
        self.pos -= self.distance.normalize()
        pygame.draw.circle(window, self.color, self.pos, self.r)


n = 3
objs = []
for i in range(n):
    x = random.randint(20,700)
    y = random.randint(20,700)

    objs.append(Boid(x, y))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    window.fill((0,0,0))

    for i in range(n):
        for j in range(n):
            if i != j:
                objs[i].check_area(objs[j])
        objs[i].draw(window)

    pygame.display.flip()
    clock.tick(60)
    pygame.display.update()
