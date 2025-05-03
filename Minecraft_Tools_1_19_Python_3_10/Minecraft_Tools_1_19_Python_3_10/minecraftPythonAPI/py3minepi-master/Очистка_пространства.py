import mcpi.minecraft as minecraft
import mcpi.block as block

import time
mc = minecraft.Minecraft.create()

pos = mc.player.getTilePos()


x=pos.x
y=pos.y
z=pos.z
#while True:
    #pos = mc.player.getTilePos()
    #x=pos.x
    #y=pos.y
    #z=pos.z
    #mc.setBlocks(x-50,y-1,z-50,x+50, y-1, z+50, 2)
    #time.sleep(3)
mc.setBlocks(x-50,y,z-50,x+50, y+50, z+50, 0)
