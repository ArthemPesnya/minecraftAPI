import sys
import os
from collections import namedtuple

from pathlib import Path
from time import sleep

sys.path.append("..\\Minecraft_Tools_1_19_Python_3_10\\Minecraft_Tools_1_19_Python_3_10\\minecraftPythonAPI\\py3minepi-master")

import mcpi.minecraft as minecraft
import mcpi.block as block
craft = minecraft.Minecraft.create(address="minecraft-server.hcloud")

craft.setBlock(-3, -3, 9, block.DIAMOND_BLOCK.id)