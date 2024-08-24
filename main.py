import asyncio
import websockets
import os
from dotenv import load_dotenv
import escapade_pb2  # Import your generated protobuf classes

# Load environment variables
load_dotenv()
print("TOKEN:", os.getenv('TOKEN'))
TOKEN = os.getenv('TOKEN')  # Ensure your .env file has a line like TOKEN='your_token_here'

# Define the WebSocket URI
URI = "wss://escapade.fun:2053/ws"

async def send_message(websocket, message):
    """Serialize and send a message to the WebSocket server."""
    serialized_message = message.SerializeToString()
    await websocket.send(serialized_message)
    print("Message sent.")

async def receive_message(websocket):
    """Receive and deserialize a message from the WebSocket server."""
    try:
        serialized_message = await websocket.recv()
        message = escapade_pb2.WorldEvent()
        message.ParseFromString(serialized_message)
        return message
    except websockets.exceptions.ConnectionClosedOK:
        print("Connection closed normally.")
        return None
    except websockets.exceptions.ConnectionClosedError as e:
        print(f"WebSocket connection closed unexpectedly: {e}")
        return None
    except websockets.exceptions.InvalidMessage as e:
        print(f"Received invalid WebSocket message: {e}")
        return None
    except Exception as e:
        print(f"Error receiving message: {e}")
        return None

async def handle_commands(websocket):
    """Handle incoming commands."""
    while True:
        world_event = await receive_message(websocket)
        if world_event:
            event_type = world_event.event_type
            print(f"Received WorldEvent: {event_type}")
            if event_type == escapade_pb2.WorldEventType.Block:
                block_args = world_event.block_args
                print(f"Block ID: {block_args.blockId}")
        else:
            print("No event received, closing connection.")
            break

async def main():
    # Ensure TOKEN is not None
    if TOKEN is None:
        print("Error: TOKEN environment variable not set.")
        return

    async with websockets.connect(URI, extra_headers={"Authorization": f"Bearer {TOKEN}"}, timeout=60) as websocket:
        print("Connected to WebSocket server")

        # Send JoinWorld message
        join_world_message = escapade_pb2.JoinWorld(
            auth_token=TOKEN,
            world_id="k7HdPPpVDXsY"  # Ensure this is a valid world ID
        )
        await send_message(websocket, join_world_message)
        print("Sent JoinWorld message")

        # Send Sync WorldEvent message
        sync_event = escapade_pb2.WorldEvent()
        sync_event.event_type = escapade_pb2.WorldEventType.Sync
        await send_message(websocket, sync_event)
        print("Sent Sync message")

        # Handle incoming messages and commands
        await handle_commands(websocket)

if __name__ == "__main__":
    asyncio.run(main())
