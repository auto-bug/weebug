import robot
import asyncio
import time
import walk
import board
import ir


def calibrate():
    for leg in robot.LEGS:
        leg.move()
        time.sleep(0.25)

    while True:
        time.sleep(1)

async def main():
    gait = walk.Walk()
    walk_task = asyncio.create_task(gait.walk())
    ir_task = asyncio.create_task(ir.ir_remote(board.GP29, gait))
    await asyncio.gather(walk_task, ir_task)


#calibrate()

asyncio.run(main())
