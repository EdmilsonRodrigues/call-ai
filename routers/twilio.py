from _typeshed import TraceFunction
from config import BASE_API_URL
from fastapi import APIRouter, WebSocket, exceptions
from fastapi.responses import PlainTextResponse
from starlette.types import ExceptionHandler
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


async def send_audio_chunks(websocket: WebSocket):
    while True:
        try:
            customer_audio = await websocket.receive_bytes()
            if customer_audio:
                return customer_audio

        except Exception as e:
            print(f"Error receiving audio: {e}")


async def generate_audio_chunks():
    audio_data = [b"audio_chunk_1", b"audio_chunk_2", b"audio_chunk_3"]
    for chunk in audio_data:
        yield chunk


async def handle_customer_input(customer_audio):
    print(f"Processing customer input: {customer_audio}")


@router.post("/receive-audio/")
async def twilio_voice():
    response = VoiceResponse()
    response.say("Say something")
    response.start().stream(url=f"wss://{BASE_API_URL}/media-stream")
    return PlainTextResponse(str(response), media_type="application/xml")

def generate_response_audio():
    return b""

