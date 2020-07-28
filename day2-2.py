# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 10:21:20 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import random,time

while True:
    x,y,z=mc.player.getTilePos()
    color=random.randrange(0,16)
    mc.setBlocks(x+5,y-1,z+5,x-5,y-1,z-5,46)  