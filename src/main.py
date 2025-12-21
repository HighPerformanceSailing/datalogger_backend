#!/usr/bin/python3

from api import API
from logger.MockLogger import MockLogger
from logger.ReadCSVLogger import ReadCSVLogger
try:
    from logger.RaspberryPiLogger import RaspberryPiLogger
except:
    print("Could not import the Raspberry Pi Logger.")

import asyncio
import threading

def loggingThread(logger, interval):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    asyncio.run(logger.loggingLoop(interval=interval))

async def main():
    # logger = RaspberryPiLogger()
    # logger = MockLogger()
    logger = ReadCSVLogger()
    interval = 0.1
    thread = threading.Thread(target=loggingThread, args=(logger, interval))
    thread.start()
    # await asyncio.gather(runAPI(logger))
    API().runAPI(logger)

if __name__=="__main__":
    asyncio.run(main())
