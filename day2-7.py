# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 15:21:03 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
name=input("your name")
massage=input("what you want to say")
mc.postToChat("("+name+")"+massage)
