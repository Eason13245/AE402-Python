#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 19:42:29 2020

@author: gaoyixun
"""


import pygame
BLACK = (0,0,0)
WHITE = (255,255,255)
pygame.init()
size = (700,500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Drawing board")
done = False


while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
            
clock = pygame.time.Clock()
screen.fill(WHITE)
pygame.draw.circle(screen,BLACK (100,100) (20))
pygame.draw.circle(screen,BLACK (140,100) (20))
pygame.draw.circle(screen,BLACK (100,140) (20))
pygame.draw.circle(screen,BLACK (140,140) (20))
pygame.display.flip()