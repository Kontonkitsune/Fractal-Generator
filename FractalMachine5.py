'''


Fractal Generator v5.0
Creator: Lucian Reiter / Kontonkitsune
Updated: 10/21/2020

Uses:
Python,
Modules: pygame ; math ; random





'''

version = 5



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
pygame.display.set_caption("Fractal Generator v0.5")
screen2 = pygame.Surface((boxheight,boxheight))

black = (0,0,0)
white = (255,255,255)
yellow = (255,255,0)
blue = (0,0,255)
green = (0,255,0)

bgcolor = black

coloroption = False


enablecursor = True
toggleinfo = False
var1 = 0
var2 = 0
pos2 = [(0,0)]
prevpos = [0,0,0,0]
sides = version
v = ((640,320),(320,0),(0,320),(320,640))
pos = list(v)
speed = 0.001
truespeed = 1
scalefactor = 1.618
mode = 4
sda = 0
scolor3 = (255,255,255)
p = -1
simplecolor = 1
frac1 = 1 
frac2 = 1

cursorposition = 0

dotsize = 1

pdisables = [False,False,False,False,False]
pdisables2 = [False,False,False,False,False]
enablemiddle = False
enablemidpoint = False

frameskip = 100
fskp = 0
fskip = 2

cond = False 
counter = 0

generoptions = False

graphicsoptionsenable = False

rd = 0
running = True

showdisables = False

colorchanges = False
colorphase = 0
colorchangerate = 3

possibleshape = True


def definecorners():
	global v
	global scalefactor
	global pdisables
	global pdisables2
	global possibleshape
	global screen2
	
	possibleshape = True
	pdisables = []
	pdisables2 = []
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
#
def randomcolor():
	return (random.randint(0,255),random.randint(0,255),random.randint(0,255))
#
def colorchange():
	global scolor3
	global colorphase
	
	colorphase2 = round(colorphase)
	if colorphase2 < 256:
		scolor3 = (255-colorphase2,colorphase2,0)
	elif colorphase2 < 512:
		scolor3 = (0,511-colorphase2,colorphase2-256)
	else:
		scolor3 = (colorphase2-512,0,767-colorphase2)
	
	colorphase += 2**colorchangerate / 1000
	if colorphase > 767:
		colorphase = 0
#
def resetboard():
	guifont = pygame.font.Font('freesansbold.ttf', fontsize1)
	screen2.fill(black)
	possibleshape = True
#
fontsize1 = 30
guifont = pygame.font.Font('freesansbold.ttf', fontsize1) 
text = ""
text2 = ""
buttonlist = []
opvar1 = 0
def textline(txt,buttonmask="null",txtcolor=white):
	global text2
	global opvar1
	global cursorposition
	global buttonlist
	buttonlist.append(buttonmask)
	if opvar1 == cursorposition:
		text2 = guifont.render(txt, True, yellow)
	else:
		text2 = guifont.render(txt, True, txtcolor)
	screen.blit(text2,(0,opvar1 * fontsize1))
	opvar1 += 1

def textgui():
	global opvar1
	opvar1 = 0
	global buttonlist
	buttonlist = []
	textline("Fractal Generator v0.%s" % version)
	
	textline("Generation Options","options",blue)
	if generoptions:
		textline("Clear","clear")
		textline("Sides: %s" % sides,"sides")

		if mode == 1:
			text = "Jump Mode: 1/2"
		elif mode == 2:
			text = "Jump Mode: 1/3"
		elif mode == 3:
			text = "Jump Mode: 2/3"
		elif mode == 4:
			text = "Jump Mode: (Relative to scale)"
		elif mode == 5:
			text = "Jump Mode: %s/%s (Custom)" % (frac1,frac1 + frac2)
		textline(text,"mode")
		
		if mode == 5:
			textline("Multiple 1: %s" % frac1,"frac1")
			textline("Multiple 2: %s" % frac2,"frac2")
		
		
		textline("Midpoints?: %s" % enablemidpoint,"mpenable")
		textline("Middle point?: %s" % enablemiddle,"cpenable")
	
	textline("Graphics Options","goptions",blue)
	if graphicsoptionsenable:
		textline("Frameskip: %s" % (frameskip),"frameskip")
		textline("Show Points: %s" % enablecursor,"enablecursor")
		textline("Point Size: %s" % dotsize,"dotsize")
		
		pointcolor = "Opposite"
		if simplecolor == 2:
			pointcolor = "Random"
		
		
		textline("Point Color: %s" % pointcolor,"pointcolor",green)
		if simplecolor == 2:
			textline("Randomize","randomcolor")
			textline("Color Change?: %s" % colorchanges,"colorchange?",green)
			if colorchanges:
				textline("Color Change Rate: %s" % (2**colorchangerate),"colorchangerate")
	
	textline("Show Disables","showdisables",blue)
	
	if showdisables:
		textlist1 = []
		op8 = 0
		while op8 < len(pdisables):
			if pdisables[op8]:
				textlist1.append(op8)
			op8 += 1
		textline("Relative Disables: %s" % (textlist1))
		
		textlist1 = []
		op8 = 0
		while op8 < len(pdisables2):
			if pdisables2[op8]:
				textlist1.append(op8)
			op8 += 1
		textline("Absolute Disables: %s" % (textlist1))
	
	
	
#Main Loop
definecorners()
while running:
	
	### ---------------------------------PLOTTING----------------------------------###
	
	cond = False
	counter = 0
	op9 = 0
	if simplecolor == 1:
		scolor3 = (255-bgcolor[0],255-bgcolor[1],255-bgcolor[2])
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
	
	
	
	### ---------------------------------CONTROLS----------------------------------###
	
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
			if event.key == K_i:
				toggleinfo = not toggleinfo
			
			if toggleinfo:
				
				if event.key == K_DOWN:
					cursorposition += 1
					if cursorposition >= opvar1:
						cursorposition = opvar1-1
				
				if event.key == K_UP:
					cursorposition -= 1
					if cursorposition < 0:
						cursorposition = 0 
				
				if event.key == K_RIGHT:
					if buttonlist[cursorposition] == "mode":
						mode += 1
						if mode > 5:
							mode = 1
						resetboard()
					if buttonlist[cursorposition] == "frac1":
						frac1 += 1
						resetboard()
					if buttonlist[cursorposition] == "frac2":
						frac2 += 1
						resetboard()
					if buttonlist[cursorposition] == "colorchangerate":
						colorchangerate += 1
						if colorchangerate > 7:
							colorchangerate = -4
					if buttonlist[cursorposition] == "dotsize":
						dotsize += 1
						if dotsize > 5:
							dotsize = 1
					if buttonlist[cursorposition] == "pointcolor":
						simplecolor += 1
						if simplecolor > 2:
							simplecolor = 1
					if buttonlist[cursorposition] == "frameskip":
						fskip += 1
						if fskip > 3:
							fskip = 0
						frameskip = 10**fskip
						fskp = 0
					if buttonlist[cursorposition] == "sides":
						sides += 1
						definecorners()
						if p >= len(v):
							p = -1
					
				if event.key == K_LEFT:
					if buttonlist[cursorposition] == "mode":
						mode -= 1
						if mode < 1:
							mode = 5
						resetboard()
					if buttonlist[cursorposition] == "frac1":
						frac1 -= 1
						if frac1 < 1:
							frac1 = 1
						resetboard()
					if buttonlist[cursorposition] == "frac2":
						frac2 -= 1
						if frac2 < 1:
							frac2 = 1
						resetboard()
					if buttonlist[cursorposition] == "colorchangerate":
						colorchangerate -= 1
						if colorchangerate < -4:
							colorchangerate = 7
					if buttonlist[cursorposition] == "dotsize":
						dotsize -= 1
						if dotsize < 1:
							dotsize = 5
					if buttonlist[cursorposition] == "pointcolor":
						simplecolor -= 1
						if simplecolor < 1:
							simplecolor = 2
					if buttonlist[cursorposition] == "frameskip":
						fskip -= 1
						if fskip < 0:
							fskip = 3
						frameskip = 10**fskip
						fskp = 0
					if buttonlist[cursorposition] == "sides":
						sides -= 1
						definecorners()
						if sides < 3:
							sides = 3
						if p >= len(v):
							p = -1
				
				if event.key == K_LEFT or event.key == K_RIGHT or event.key == K_z:
					if buttonlist[cursorposition] == "colorchange?":
						colorchanges = not colorchanges
					if buttonlist[cursorposition] == "mpenable":
						enablemidpoint = not enablemidpoint
						definecorners()
					if buttonlist[cursorposition] == "cpenable":
						enablemiddle = not enablemiddle
						definecorners()
					if buttonlist[cursorposition] == "showdisables":
						showdisables = not showdisables
					if buttonlist[cursorposition] == "enablecursor":
						enablecursor = not enablecursor
					if buttonlist[cursorposition] == "randomcolor":
						colorphase = random.randint(0,767)
						colorchange()
					if buttonlist[cursorposition] == "options":
						generoptions = not generoptions
					if buttonlist[cursorposition] == "clear":
						definecorners()
					
					if buttonlist[cursorposition] == "goptions":
						graphicsoptionsenable = not graphicsoptionsenable
					
			else:
				if event.key == K_RIGHT:
					p += 1
					if p >= len(v):
						p = -1 #default, no limit
			
				if event.key == K_LEFT:
					p -= 1
					if p < -1:
						p = len(v)-1 #default, no limit
			
				if event.key == K_z:
					pdisables[p] = not pdisables[p]
					resetboard()
				
				if event.key == K_x:
					pdisables2[p] = not pdisables2[p]
					resetboard()
			
	
	### ---------------------------------Color change----------------------------------###
	
	
	if colorchanges == True:
		colorchange()
	
	screen.fill(bgcolor)
	
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
		if toggleinfo:
			textgui()
		pygame.display.update()
	fskp += 1
	
	
	
pygame.quit()