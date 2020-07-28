from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z=mc.player.getTilePos()
blockid=int(input("the blockid that you want to put:"))
mc.setBlock(x+1,y,z,blockid)

