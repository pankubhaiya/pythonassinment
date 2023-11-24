import asyncio
import websockets
import csv
from datetime import datetime

async def process_data(data):
  

async def connect_to_websocket():
    url = "wss://functionup.fintarget.in/ws?id=fintarget-functionup"
    async with websockets.connect(url) as websocket:
        while True:
            data = await websocket.recv()
          
            asyncio.create_task(process_data(data))

if __name__ == "__main__":
    asyncio.run(connect_to_websocket())


def calculate_sma(data_points):
  
    if len(data_points) < 3:
        return None  

    return sum(data_points[-3:]) / 3

import pandas as pd

def calculate_ema(data_points):
   
    if len(data_points) < 3:
        return None  

    df = pd.DataFrame(data_points, columns=['Close'])
    return df['Close'].ewm(span=3, adjust=False).mean().iloc[-1]

