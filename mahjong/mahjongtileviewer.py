# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 16:33:55 2023

@author: Eurydice
"""

import pygame,sys, math, glob, os

from pygame.locals import *

pygame.init()
FPS = 60
FramePerSec = pygame.time.Clock()
xaxis = 1600
yaxis = 720
window = pygame.display.set_mode((xaxis,yaxis))

basesizex = 600
basesizey = 800
scale = 8

scalesizex = basesizex / scale
scalesizey = basesizey / scale
mindistx = 2
mindisty = 20

def imgen(file):
    pic = pygame.image.load(file)
    pic = pygame.transform.scale(pic,(75,100))
    return(pic)

front = imgen('front.png')
back = imgen('back.png')
ton = imgen('ton.svg')
nan = imgen('nan.svg')
sha = imgen('shaa.svg')
pei = imgen('pei.svg')
haku = imgen('haku.svg')
hatsu = imgen('hatsu.svg')
chun = imgen('chun.svg')
man1 = imgen('man1.svg')
man2 = imgen('man2.svg')
man3 = imgen('man3.svg')
man4 = imgen('man4.svg')
man5 = imgen('man5.svg')
man6 = imgen('man6.svg')
man7 = imgen('man7.svg')
man8 = imgen('man8.svg')
man9 = imgen('man9.svg')
man0 = imgen('man5-dora.svg')
sou1 = imgen('sou1.png')
sou2 = imgen('sou2.svg')
sou3 = imgen('sou3.svg')
sou4 = imgen('sou4.svg')
sou5 = imgen('sou5.svg')
sou6 = imgen('sou6.svg')
sou7 = imgen('sou7.svg')
sou8 = imgen('sou8.svg')
sou9 = imgen('sou9.svg')
sou0 = imgen('sou5-dora.svg')
pin1 = imgen('pin1.png')
pin2 = imgen('pin2.png') 
pin3 = imgen('pin3.svg') 
pin4 = imgen('pin4.svg') 
pin5 = imgen('pin5.svg') 
pin6 = imgen('pin6.svg') 
pin7 = imgen('pin7.svg') 
pin8 = imgen('pin8.svg') 
pin9 = imgen('pin9.svg') 
pin0 = imgen('pin5-dora.svg') 

pygame.display.set_caption("Riichi tiler")
pygame.image.load
xcoord = scalesizex
ycoord = mindisty

delrightdist = (xaxis - scalesizex)%(scalesizex + mindistx)
def imgshow(pic):
    window.blit(front,(xcoord,ycoord))
    window.blit(pic,(xcoord,ycoord))    

while True:
    pygame.display.update()
    FramePerSec.tick(FPS)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
#            print(event.key)
            if event.key ==pygame.K_1:
                imgshow(ton)
            if event.key ==pygame.K_2:
                imgshow(nan)
            if event.key ==pygame.K_3:
                imgshow(sha)
            if event.key ==pygame.K_4:
                imgshow(pei)
            if event.key ==pygame.K_5:
                imgshow(haku)
            if event.key ==pygame.K_6:
                imgshow(hatsu)
            if event.key ==pygame.K_7:
                imgshow(chun)
            if event.key ==pygame.K_8:
                imgshow(man0)
            if event.key ==pygame.K_9:
                imgshow(sou0)
            if event.key ==pygame.K_0:
                imgshow(pin0)
            if event.key ==pygame.K_q:
                imgshow(man1)
            if event.key ==pygame.K_w:
                imgshow(man2)
            if event.key ==pygame.K_e:
                imgshow(man3)
            if event.key ==pygame.K_r:
                imgshow(man4)
            if event.key ==pygame.K_t:
                imgshow(man5)
            if event.key ==pygame.K_y:
                imgshow(man6)
            if event.key ==pygame.K_u:
                imgshow(man7)
            if event.key ==pygame.K_i:
                imgshow(man8)
            if event.key ==pygame.K_o:
                imgshow(man9)
            if event.key ==pygame.K_p:
                imgshow(man0)
            if event.key ==pygame.K_a:
                imgshow(sou1)
            if event.key ==pygame.K_s:
                imgshow(sou2)
            if event.key ==pygame.K_d:
                imgshow(sou3)
            if event.key ==pygame.K_f:
                imgshow(sou4)
            if event.key ==pygame.K_g:
                imgshow(sou5)
            if event.key ==pygame.K_h:
                imgshow(sou6)
            if event.key ==pygame.K_j:
                imgshow(sou7)
            if event.key ==pygame.K_k:
                imgshow(sou8)
            if event.key ==pygame.K_l:
                imgshow(sou9)
            if event.key ==pygame.K_SEMICOLON:
                imgshow(sou0)
            if event.key ==pygame.K_z:
                imgshow(pin1)
            if event.key ==pygame.K_x:
                imgshow(pin2)
            if event.key ==pygame.K_c:
                imgshow(pin3)
            if event.key ==pygame.K_v:
                imgshow(pin4)
            if event.key ==pygame.K_b:
                imgshow(pin5)
            if event.key ==pygame.K_n:
                imgshow(pin6)
            if event.key ==pygame.K_m:
                imgshow(pin7)
            if event.key ==pygame.K_COMMA:
                imgshow(pin8)
            if event.key ==pygame.K_PERIOD:
                imgshow(pin9)
            if event.key ==pygame.K_SLASH:
                imgshow(pin0)
            if event.key ==pygame.K_SPACE:
                pygame.draw.rect(window,(0,0,0),pygame.Rect(xcoord,ycoord,scalesizex,scalesizey))
            if (event.key >= 97 and  event.key <= 122) or (event.key >= 46 and event.key <= 57) or event.key == 44 or event.key==59 or event.key==32:
                xcoord += scalesizex + mindistx
            keys = pygame.key.get_pressed()
            if keys[pygame.K_BACKSPACE]:
                xcoord -= scalesizex + mindistx
                if xcoord <scalesizex and ycoord>mindisty:
                    xcoord = xaxis - delrightdist - mindistx - scalesizex
                    ycoord -= scalesizey + mindisty
                elif xcoord<scalesizex and ycoord<=mindisty:
                    xcoord += scalesizex + mindistx
                pygame.draw.rect(window,(0,0,0),pygame.Rect(xcoord,ycoord,scalesizex,scalesizey))
            if xcoord > (xaxis - scalesizex):
                xcoord = scalesizex
                ycoord += scalesizey + mindisty
    keys = pygame.key.get_pressed()
    if keys[pygame.K_DELETE]:
        xcoord -= scalesizex + mindistx
        if xcoord <scalesizex and ycoord>mindisty:
            xcoord = xaxis - delrightdist - mindistx - scalesizex
            ycoord -= scalesizey + mindisty
        elif xcoord<scalesizex and ycoord<=mindisty:
            xcoord += scalesizex + mindistx
        pygame.draw.rect(window,(0,0,0),pygame.Rect(xcoord,ycoord,scalesizex,scalesizey))
    if xcoord > (xaxis - scalesizex):
        xcoord = scalesizex
        ycoord += scalesizey + mindisty
    

    
