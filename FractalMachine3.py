'''


Fractal Generator v3.0
Creator: Lucian Reiter / Kontonkitsune
Updated: 10/21/2020

Uses:
Python,
Modules: pygame ; math ; random





'''





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
screen = pygame.display.set_mode((boxheight,boxheight),RESIZABLE)

screen2 = pygame.Surface((boxheight,boxheight))

black = (0,0,0)
white = (255,255,255)




enablecursor = True
var1 = 0
var2 = 0
pos2 = [(0,0)]
prevpos = [0,0,0,0]
sides = 4
v = ((640,320),(320,0),(0,320),(320,640))
pos = list(v)
speed = 0.001
truespeed = 1
scalefactor = 1.618
mode = 1
sda = 0
scolor3 = (255,255,255)
p = -1

frac1 = 1 
frac2 = 1


dotsize = 1

pdisables = [False,False,False,False]
pdisables2 = [False,False,False,False]
enablemiddle = False
enablemidpoint = False

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
	global screen2
	
	possibleshape = True
	pdisables = []
	v = []
	op1 = 0
	op2 = 0
	
	if enablemiddle:
		v.append((centerx,centery))
	
	while op2 < sides : #sides = 5 #
		x1 = centerx + scalexy * math.cos((math.pi*2/sides*op2)-math.pi/2)
		y1 = centery + scalexy * math.sin((math.pi*2/sides*op2)-math.pi/2)
		if enablemidpoint and op2 > 0:
			if enablemiddle:
				v.append(((v[2*op2-1][0]+x1)/2,(v[2*op2-1][1]+y1)/2))
			else: #0 (c)[0], 1 (t)[1], 2 (1.5)[1], 3 (2)[2], 4 (2.5)[2]{
				v.append(((v[2*op2-2][0]+x1)/2,(v[2*op2-2][1]+y1)/2))
		v.append((x1,y1))
		print(v)
		print(op2)
		op2 += 1
	
	x1 = centerx + scalexy * math.cos((math.pi*2/sides*op2)-math.pi/2)
	y1 = centery + scalexy * math.sin((math.pi*2/sides*op2)-math.pi/2)
	if enablemidpoint:
		if enablemiddle:
			v.append(((v[2*op2-1][0]+x1)/2,(v[2*op2-1][1]+y1)/2))
		else: #0 (c)[0], 1 (t)[1], 2 (1.5)[1], 3 (2)[2], 4 (2.5)[2]{
			v.append(((v[2*op2-2][0]+x1)/2,(v[2*op2-2][1]+y1)/2))
		
	v = tuple(v)
	pos = list(v)
	for x in v:
		pdisables.append(False)
		pdisables2.append(False)
	
	#scalefactor calculation
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

definecorners()

while running:
	
	cond = False
	counter = 0
	op9 = 0
	while op9 < len(pos):
		if cond == False:
			while cond == False and possibleshape == True:
				counter += 1
				if counter > 100:
					possibleshape = False
				sda = random.randint(0,len(v)-1)
				if not pdisables[sda]:
					sda = (sda + prevpos[op9]) % len(v)
					if not pdisables2[sda]:
						cond = True
						rd = sda
		prevpos[op9] = rd
		
	
		if mode == 1:
			pos[op9] = ((pos[op9][0] + v[rd][0])/2,(pos[op9][1] + v[rd][1])/2)
			pos2 = (round(pos[op9][0]),round(pos[op9][1]))
		
		if mode == 2:
			pos[op9] = (( 2*pos[op9][0] + v[rd][0])/3,(2* pos[op9][1] + v[rd][1])/3)
			pos2 = (round(pos[op9][0]),round(pos[op9][1]))
		
		if mode == 3:
			pos[op9] = ((pos[op9][0] + 2* v[rd][0])/3,( pos[op9][1] + 2*v[rd][1])/3)
			pos2 = (round(pos[op9][0]),round(pos[op9][1]))
			
		if mode == 4:
			pos[op9] = ((pos[op9][0] + scalefactor * v[rd][0])/(scalefactor+1),( pos[op9][1] + scalefactor * v[rd][1])/(scalefactor+1))
			pos2 = (round(pos[op9][0]),round(pos[op9][1]))
			
		if mode == 5:
			pos[op9] = ((frac1 * pos[op9][0] + frac2 * v[rd][0])/(frac1 + frac2),( frac1 * pos[op9][1] + frac2 *v[rd][1])/(frac1 + frac2))
			pos2 = (round(pos[op9][0]),round(pos[op9][1]))
		
		if dotsize == 1:
			screen2.set_at(pos2,scolor3)
		else:
			pygame.draw.circle(screen2,scolor3,pos2,dotsize,0)
		
		op9 += 1
	
	
	
	
	
	for event in pygame.event.get():
		if event.type == QUIT:
			running = False
		
		if event.type == VIDEORESIZE:
			screen = pygame.display.set_mode((event.w,event.h),RESIZABLE)
			screen2 = pygame.Surface((event.w,event.h))
			centerx = event.w / 2
			centery = event.h / 2
			if event.w > event.h:
				scalexy = event.h / 2 - 10
			else:
				scalexy = event.w / 2 - 10
			definecorners()
			
			
			
		if event.type == KEYDOWN:
			if event.key == K_1 or event.key == K_RIGHT:
				p += 1
				if p >= len(v):
					p = -1 #default, no limit
			
			if event.key == K_2 or event.key == K_LEFT:
				p -= 1
				if p < -1:
					p = len(v)-1 #default, no limit
			
			if event.key == K_3:
				pdisables[p] = not pdisables[p]
				resetboard()
			
			if event.key == K_4:
				pdisables2[p] = not pdisables2[p]
				resetboard()
			
			if event.key == K_n:
				enablemiddle = not enablemiddle
				definecorners()
				
			if event.key == K_m:
				enablemidpoint = not enablemidpoint
				definecorners()
				
			if event.key == K_a:
				sides += 1
				definecorners()
				if p >= len(v):
					p = -1
			
			if event.key == K_s:
				sides -= 1
				if sides < 3:
					sides = 3
				definecorners()
				if p >= len(v):
					p = -1
				
				
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
				colorchanges = not colorchanges
			
			if event.key == K_v:
				colorchangerate += 1
				if colorchangerate > 5:
					colorchangerate = -2
				
			if event.key == K_p:
				enablecursor = not enablecursor
			
			if event.key == K_o:
				dotsize += 1
				if dotsize >= 4:
					dotsize = 1
				
	screen.fill(black)
	if colorchanges == True:
		colorchange()
		colorphase += 2**colorchangerate / 1000
		if colorphase > 767:
			colorphase = 0
			
	if fskp == frameskip:
		screen.blit(screen2,(0,0))
		fskp = 0
		op1 = False
		for x in pdisables:
			if x:
				op1 = True
		if enablecursor == True:
			op1 = 0
			if p != -1:
				pygame.draw.circle(screen,(255,0,0),(round(v[p][0]),round(v[p][1])),8,5)
			while op1 < len(v):
				if not pdisables[op1]:
					pygame.draw.circle(screen,(0,0,255),(round(v[op1][0]),round(v[op1][1])),5,2)
				if not pdisables2[op1]:
					pygame.draw.circle(screen,(0,255,0),(round(v[op1][0]),round(v[op1][1])),2,2)
				op1 += 1
		pygame.display.update()
	fskp += 1
	
pygame.quit()