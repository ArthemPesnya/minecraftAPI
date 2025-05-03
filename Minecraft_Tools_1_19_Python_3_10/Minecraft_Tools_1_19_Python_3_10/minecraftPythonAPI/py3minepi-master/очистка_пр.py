import mcpi.minecraft as minecraft
import mcpi.block as block
import time
craft=minecraft.Minecraft.create()
cor=craft.player.getTilePos()

x = cor.x
y = cor.y
z = cor.z


#while True:
craft.setBlocks(x-50,y,z-50, x+50,y+50, z+50, 0) #очистка пространства
    
#craft.setBlocks(x-50,y-1,z-50, x+50,y-1, z+50, 2) #создание пола 

#craft.setBlocks(x-50,y,z-50, x+50,y, z+50, 78)
