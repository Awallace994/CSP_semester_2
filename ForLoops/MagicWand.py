from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import time



hits = mc.events.pollBlockHits()
block = 103

for hit in hits:
    x, y, z = hit.pos.x, hit.pos.y, hit.pos.z
    mc.setBlock(103)
    time.sleep(5)