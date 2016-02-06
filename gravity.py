import pygame
import sys
from pygame.locals import *
import os
import math
from random import *
from itertools import combinations

pygame.init()

position = [400, 25]
os.environ['SDL_VIDEO_WINDOW_POS'] = str(position[0]) + "," + str(position[1])

FPS = 35
fpsClock = pygame.time.Clock()

width = 700
height = 700

CANVAS = pygame.display.set_mode((width, height))

pygame.display.set_caption('Gravity')

G = .1

def collision(circles):
	circle1 = circles[0]
	circle2 = circles[1]
	if ((((circle1.x-circle2.x)**2 + (circle1.y-circle2.y)**2)) < (circle1.radius+circle2.radius)**2):
		return True
	else:
		return False

class Circle:
	def __init__(self, color, x, y, mass, radius, speedx, speedy, accx, accy):
		self.color = color
		self.x = x
		self.y = y
		self.mass = mass
		self.radius = radius
		self.speedx = speedx
		self.speedy = speedy
		self.accx = accx
		self.accy = accy
	def gravityForce(self, bodies):
		forcex = 0
		forcey = 0
		for t in bodies:
			if t is self:
				continue
			distx = (t.x - self.x)
			disty = (t.y - self.y)
			forcex += (G * self.mass * t.mass * distx)/((distx**2 + disty**2+1e-4)**1.5)
			forcey += (G * self.mass * t.mass * disty)/((distx**2 + disty**2+1e-4)**1.5)
		self.accx = forcex / self.mass
		self.accy = forcey / self.mass
	def move (self):
		self.x += self.speedx
		self.y += self.speedy
		self.speedx += self.accx
		self.speedy += self.accy
	def make(self):
		pygame.draw.circle(CANVAS, self.color, (int(self.x), int(self.y)), self.radius, 0)

WHITE = (255,255,255)
BLUE = (0,0,255)

moon = Circle(WHITE, 500, 500, 40, 20, -1, 0, 0, 0)
bodies = []
# for i in range(100):
# 	mass = randint(1,4000)
# 	color = (randint(0,255), randint(0,255), randint(0,255))
# 	position = (randint(100,600), randint(100,600))
# 	body = Circle(color, position[0], position[1], mass, int(math.log(mass)), 0,0, 0, 0)
# 	bodies.append(body)

sun = Circle((0,255,0), 350, 350, 1e4, int(math.log(1e12)), 0,0, 0, 0)
bodies.append(sun)

earth = Circle(BLUE, 500, 350, 500, int(math.log(500)), 0, -(.1 * 1e4/160)**.5, 0, 0)
bodies.append(earth)

# mars = Circle((255,0,0), 100, 350, 75, int(math.log(500)),0, (.1 * 1e4/260)**.5, 0, 0)
# bodies.append(mars)
pan = False
startpantime = 0
while True:

	if pygame.mouse.get_pressed()[0] == 1:
		if not pan:
			startpantime = pygame.time.get_ticks()
			start = pygame.mouse.get_pos()
		pan = True
	else:
		pan = False
	if (pygame.mouse.get_pressed()[0] == 1) and ((pygame.time.get_ticks() - startpantime) > 10):
		if pan:
			end = pygame.mouse.get_pos()
			movex = start[0] - end[0]
			movey = start[1] - end[1]
			for b in bodies:
				b.x = b.x + movex
				b.y = b.y + movey
			pan = False
			startpantime = 0
	CANVAS.fill((0,0,0))
	for b in bodies:
		b.make()
		b.gravityForce(bodies)
		b.move()
		#elastic collision walls
		if b.x >= width-5 or b.x <= 5:
			b.speedx = -b.speedx
		elif b.y >= height-5 or b.y <= 5:
			b.speedy = -b.speedy
	bodycom = []
	bodycom = list(combinations(bodies, 2))
	used = []
	for i in bodycom:
		if collision(i):
			skip = False
			for p in used:
				if p in i:
					skip = True
			if skip:
				continue
			massTotal = i[0].mass+i[1].mass
			xspeed = (i[0].mass*i[0].speedx + i[1].mass*i[1].speedx) / (massTotal)
			yspeed = (i[0].mass*i[0].speedy + i[1].mass*i[1].speedy) / (massTotal)
			if i[0].mass > i[1].mass:
				used.append(i[0])
				used.append(i[1])
				body = Circle(i[0].color, i[0].x, i[0].y, massTotal, int(math.log(massTotal)), xspeed,yspeed, 0, 0)
				bodies.remove(i[0])
				bodies.remove(i[1])
				bodies.append(body)
			else:
				used.append(i[1])
				used.append(i[0])
				body = Circle(i[1].color, i[1].x, i[1].y, massTotal, int(math.log(massTotal)), xspeed,yspeed, 0, 0)
				bodies.remove(i[0])
				bodies.remove(i[1])
				bodies.append(body)
	for event in pygame.event.get():
                key = pygame.key.get_pressed()
                if key[K_ESCAPE]:
                    pygame.quit()
                    sys.exit()
                    break
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                    break


	pygame.display.update()
	fpsClock.tick(FPS)