# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 15:41:48 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z=mc.player.getTilePos()
mc.setSign(x,y,z,63,0,"i love","minecraft","and Python" )