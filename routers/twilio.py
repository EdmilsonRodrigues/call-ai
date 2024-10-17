from fastapi import APIRouter, WebSocket, exceptions
from fastapi.responses import PlainTextResponse
import websockets
import asyncio
import io


router = APIRouter(tags=["Twilio"])


@router.websocket("/media-stream/")
async def media_stream(websocket: WebSocket):
    await websocket.accept()

    try:
        while True:
            send_task  = asyncio.create_task(send_audio_chunks(websocket))
            receive_task = asyncio.create_task(receive_customer_audio(websocket))

            done, pending = await asyncio.wait(
                    {send_task, receive_task}, return_when=asyncio.FIRST_COMPLETED
                    )

            for task in pending:
                task.cancel()

            if receive_task in done:
                customer_data = await receive_task

                await handle_customer_input(customer_data)
                
    except websockets.ConnectionClosedError:
        print("Connection Closed")

    finally:
        await websocket.close()


@router.post("/receive-audio/")
async def twilio_voice():
    response = VoiceResponse()
    response.say("Say something")
    response.start().stream(url=f"wss://{BASE_API_URL}/media-stream")
    return PlainTextResponse(str(response), media_type="application/xml")

def generate_response_audio():
    return b""

