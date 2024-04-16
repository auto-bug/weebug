import robot
import asyncio
import time
import walk
import pulseio
import board
import adafruit_irremote
import digitalio

def calibrate():
    for leg in robot.LEGS:
        leg.move()
        time.sleep(0.25)

    while True:
        time.sleep(1)


async def main():
    gait = walk.Walk()
    walk_task = asyncio.create_task(gait.walk())
    await asyncio.gather(walk_task)


#calibrate()

asyncio.run(main())
