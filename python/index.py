import asyncio
import websockets
import csv
from datetime import datetime

async def process_data(data):
    # Here you'll parse and process the received data
    # Split the data for each instrument (Nifty, Banknifty, Finnifty)
    # Calculate OLHC for each instrument for 1-minute intervals
    # Store OLHC data for 1 hour in a CSV file

async def connect_to_websocket():
    url = "wss://functionup.fintarget.in/ws?id=fintarget-functionup"
    async with websockets.connect(url) as websocket:
        while True:
            data = await websocket.recv()
            # Call your function to process data asynchronously
            asyncio.create_task(process_data(data))

if __name__ == "__main__":
    asyncio.run(connect_to_websocket())


def calculate_sma(data_points):
    # Calculate Simple Moving Average with window size 3
    if len(data_points) < 3:
        return None  # Ignore for the first 2 minutes

    return sum(data_points[-3:]) / 3

import pandas as pd

def calculate_ema(data_points):
    # Calculate Exponential Moving Average
    if len(data_points) < 3:
        return None  # Ignore for the first 2 minutes

    df = pd.DataFrame(data_points, columns=['Close'])
    return df['Close'].ewm(span=3, adjust=False).mean().iloc[-1]

