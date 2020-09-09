# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 20:08:35 2020

@author: Lenovo
"""


import pygame

pygame.init()
gameDisplay = pygame.display.set_mode((800, 800))
pygame.display.net_caption("PyChess")
clock = pygame.time.Clock()

quitgame = False