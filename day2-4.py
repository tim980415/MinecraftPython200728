# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 11:30:09 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import random,time

while True:
    x,y,z=mc.player.getTilePos()
    color=random.randrange(0,9)
    mc.setBlock(x,y,z-1,46,color)
    time.sleep(0.2)