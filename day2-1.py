# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 09:35:13 2020

@author: user
"""


from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z=mc.player.getTilePos()
mc.setBlock(x+1,y,z,46)
mc.setBlock(x-1,y,z,46)
mc.setBlock(x,y,z+1,46)
mc.setBlock(x,y,z-1,46)
mc.setBlock(x+1,y,z+1,46)
mc.setBlock(x-1,y,z+1,46)
mc.setBlock(x-1,y,z-1,46)
mc.setBlock(x+1,y,z-1,46)
