import sys
print(sys.path)
import asyncio
import websockets
import logging
from escapade_pb2 import JoinWorld, WorldEvent, WorldEventType

# Configure logging
logging.basicConfig(level=logging.DEBUG)


async def connect():
    uri = "wss://escapade.fun:2053/ws"  # WebSocket URL

    # Replace these with actual values
    auth_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJkaXNjb3JkIiwic3ViIjoidTc5dHRUeW5GemRiIiwiZXhwIjoxNzI0Mzk5NzEwLCJpYXQiOjE3MjQzOTkxMTB9.pMTIAjUpCxsSAEfJnGXtUgKcsUZrSY3SLX8YpYfkFeQ"
    world_id = "k7HdPPpVDXsY"

    try:
        logging.info(f"Connecting to {uri}")
        async with websockets.connect(uri) as websocket:
            logging.info("WebSocket connection established.")

            # Create and populate the JoinWorld message
            join_world_message = JoinWorld()
            join_world_message.auth_token = auth_token
            join_world_message.world_id = world_id

            try:
                # Serialize the message
                serialized_message = join_world_message.SerializeToString()
                logging.debug(f"Serialized JoinWorld message: {serialized_message.hex()}")

                # Send the message
                await websocket.send(serialized_message)
                logging.info("Sent JoinWorld message.")
            except Exception as e:
                logging.error(f"Error serializing or sending JoinWorld message: {e}")
                return

            # Handle incoming messages
            async for message in websocket:
                try:
                    # Deserialize the incoming message
                    logging.debug(f"Received message: {message.hex()}")
                    world_event = WorldEvent()
                    world_event.ParseFromString(message)
                    logging.info(f"Received WorldEvent: {world_event}")

                    # Create and send a WorldEvent with event_type Sync
                    sync_event = WorldEvent()
                    sync_event.event_type = WorldEventType.Sync

                    # Serialize the Sync event
                    serialized_sync_message = sync_event.SerializeToString()
                    logging.debug(f"Serialized Sync event message: {serialized_sync_message.hex()}")

                    # Send the Sync event message
                    await websocket.send(serialized_sync_message)
                    logging.info("Sent WorldEvent with Sync event_type.")
                except Exception as e:
                    logging.error(f"Error processing message: {e}")
                    break

    except websockets.ConnectionClosedError as e:
        logging.error(f"WebSocket connection closed with error: {e.code} - {e.reason}")
    except websockets.InvalidMessage as e:
        logging.error(f"Received an invalid message: {e}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")


if __name__ == "__main__":
    try:
        asyncio.run(connect())
    except Exception as e:
        logging.error(f"Failed to run asyncio event loop: {e}")
