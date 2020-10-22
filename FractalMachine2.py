import pygame
import math
import random
from pygame.locals import *
pygame.init()

boxheight = 800
boxwidth = 800


centerx = boxwidth/2
centery = boxheight/2
scalexy = 390
screen = pygame.display.set_mode((boxheight,boxheight))

screen2 = pygame.Surface((boxheight,boxheight))

black = (0,0,0)
white = (255,255,255)




enablecursor = True
var1 = 0
var2 = 0
pos2 = (0,0)
prevpos = 0
sides = 4
v = ((640,320),(320,0),(0,320),(320,640))
pos = v[0]
speed = 0.001
truespeed = 1
scalefactor = 1.618
mode = 1
sda = 0
scolor3 = (255,255,255)
p = -1

frac1 = 1 
frac2 = 1



pdisables = [False,False,False,False]
pdisables2 = [False,False,False,False]

frameskip = 100
fskp = 0
cond = False 
counter = 0

rd = 0
running = True

colorchanges = False
colorphase = 0
colorchangerate = 3

possibleshape = True

def definecorners():
	global v
	global scalefactor
	global pdisables
	global possibleshape
	pdisables = []
	possibleshape = True
	v = []
	op1 = 0
	op2 = 0
	while op2 < sides:
		x1 = centerx + scalexy * math.cos((math.pi*2/sides*op2)-math.pi/2)
		y1 = centery + scalexy * math.sin((math.pi*2/sides*op2)-math.pi/2)
		v.append((x1,y1))
		op2 += 1
	v = tuple(v)
	for x in v:
		pdisables.append(False)
		pdisables2.append(False)
	ffs = []
	sfc = 0
	for k in range(1,math.ceil(sides/4)):
		ffs.append(math.cos(2 * math.pi * k / sides))
	sfc = sum(ffs)
	sfc *= 2
	sfc += 1
	scalefactor = sfc
	x = 0
	f = True
	resetboard()
		
	
def randomcolor():
	return (random.randint(0,255),random.randint(0,255),random.randint(0,255))

def colorchange():
	global scolor3
	colorphase2 = round(colorphase)
	if colorphase2 < 256:
		scolor3 = (255-colorphase2,colorphase2,0)
	elif colorphase2 < 512:
		scolor3 = (0,511-colorphase2,colorphase2-256)
	else:
		scolor3 = (colorphase2-512,0,767-colorphase2)

def resetboard():
	screen2.fill(black)
	possibleshape = True

while running:
	
	cond = False
	counter = 0
	if cond == False:
		while cond == False and possibleshape == True:
			
			counter += 1
			if counter > 100:
				possibleshape = False
			sda = random.randint(0,sides-1)
			
			if not pdisables[sda]:
				sda = (sda + prevpos) % sides
				if not pdisables2[sda]:
					cond = True
					rd = sda
	prevpos = rd
	if mode == 1:
		pos = ((pos[0] + v[rd][0])/2,(pos[1] + v[rd][1])/2)
		pos2 = (round(pos[0]),round(pos[1]))
	
	if mode == 2:
		pos = (( 2*pos[0] + v[rd][0])/3,(2* pos[1] + v[rd][1])/3)
		pos2 = (round(pos[0]),round(pos[1]))
	
	if mode == 3:
		pos = ((pos[0] + 2* v[rd][0])/3,( pos[1] + 2*v[rd][1])/3)
		pos2 = (round(pos[0]),round(pos[1]))
		
	if mode == 4:
		pos = ((pos[0] + scalefactor * v[rd][0])/(scalefactor+1),( pos[1] + scalefactor * v[rd][1])/(scalefactor+1))
		pos2 = (round(pos[0]),round(pos[1]))
		
	if mode == 5:
		pos = ((frac1 * pos[0] + frac2 * v[rd][0])/(frac1 + frac2),( frac1 * pos[1] + frac2 *v[rd][1])/(frac1 + frac2))
		pos2 = (round(pos[0]),round(pos[1]))
	

	screen2.set_at(pos2,scolor3)
	
	for event in pygame.event.get():
		if event.type == QUIT:
			running = False
		
		if event.type == KEYDOWN:
			if event.key == K_1:
				p += 1
				if p >= sides:
					p = -1 #default, no limit
			
			if event.key == K_2:
				p -= 1
				if p < -1:
					p = sides-1 #default, no limit
			
			if event.key == K_3:
				if pdisables[p]:
					pdisables[p] = False
				else:
					pdisables[p] = True
				resetboard()
			
			if event.key == K_4:
				if pdisables2[p]:
					pdisables2[p] = False
				else:
					pdisables2[p] = True
				resetboard()
			
			if event.key == K_a:
				sides += 1
				if p >= sides:
					p = -1
				definecorners()
			
			if event.key == K_s:
				sides -= 1
				if sides < 3:
					sides = 3
				if p >= sides:
					p = -1
				definecorners()
				
				
			if event.key == K_y:
				frac1 -= 1
				if frac1 < 1:
					frac1 = 1
				resetboard()
			
			if event.key == K_u:
				frac1 += 1
				resetboard()
			
			if event.key == K_h:
				frac2 -= 1
				if frac2 < 1:
					frac2 = 1
				resetboard()
			
			if event.key == K_j:
				frac2 += 1
				resetboard()
			
				
				
			if event.key == K_q:
				mode = 1
				resetboard()
			
			if event.key == K_w:
				mode = 2
				resetboard()
			
			if event.key == K_e:
				mode = 3
				resetboard()
			
			if event.key == K_r:
				mode = 4
				resetboard()
			
			if event.key == K_y:
				mode = 5
				resetboard()
			
			if event.key == K_l:
				frameskip = 100
				resetboard()
			
			if event.key == K_k:
				frameskip = 1000
				resetboard()
			
			if event.key == K_z:
				scolor3 = randomcolor()
			
			if event.key == K_x:
				scolor3 = white
				
			if event.key == K_c:
				if colorchanges == False:
					colorchanges = True
				else:
					colorchanges = False
			
			if event.key == K_v:
				colorchangerate += 1
				if colorchangerate > 5:
					colorchangerate = -2
				
			if event.key == K_p:
				if enablecursor == False:
					enablecursor = True
				else:
					enablecursor = False
				
			
			
			
	if colorchanges == True:
		colorchange()
		colorphase += 2**colorchangerate / 1000
		if colorphase > 767:
			colorphase = 0
			
	if fskp == frameskip:
		screen.blit(screen2,(0,0))
		fskp = 0
		if p != -1:
			pygame.draw.circle(screen,(255,0,0),(round(v[p][0]),round(v[p][1])),8,5)
		op1 = False
		for x in pdisables:
			if x:
				op1 = True
		if enablecursor == True:
			op1 = 0
			while op1 < sides:
				if not pdisables[op1]:
					pygame.draw.circle(screen,(0,0,255),(round(v[op1][0]),round(v[op1][1])),5,2)
				if not pdisables2[op1]:
					pygame.draw.circle(screen,(0,255,0),(round(v[op1][0]),round(v[op1][1])),2,2)
				op1 += 1
		pygame.display.update()
	fskp += 1
	
pygame.quit()