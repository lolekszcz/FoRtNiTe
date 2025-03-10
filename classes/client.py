# client.py
import asyncio
import websockets

# Define the WebSocket client handler
async def connect_to_server(port):
    async with websockets.connect(f"ws://localhost:{port}") as websocket:
        # Send a message to the server
        await websocket.send("Hello, server!")

        # Wait for a response from the server
        response = await websocket.recv()
        print(f"Received from server: {response}")
