from config import BASE_API_URL
from fastapi import APIRouter, WebSocket
from fastapi.responses import PlainTextResponse
import websockets
import asyncio
from twilio.twiml.voice_response import VoiceResponse
from models.voice import VoiceHandler


router = APIRouter(tags=["Twilio"])


@router.websocket("/media-stream/")
async def media_stream(websocket: WebSocket):
    await websocket.accept()
    voice_handler = VoiceHandler(websocket)

    try:
        while True:
            send_task  = asyncio.create_task(voice_handler.send_audio_chunks())
            receive_task = asyncio.create_task(voice_handler.receive_customer_audio())

            done, pending = await asyncio.wait(
                    {send_task, receive_task}, return_when=asyncio.FIRST_COMPLETED
                    )

            for task in pending:
                task.cancel()

            if receive_task in done:
                customer_data = await receive_task

                await voice_handler.handle_customer_input(customer_data)
                
    except websockets.ConnectionClosedError:
        print("Connection Closed")

    finally:
        await websocket.close()


@router.post("/receive-audio/")
async def twilio_voice():
    response = VoiceResponse()
    response.start().stream(url=f"wss://{BASE_API_URL}/media-stream")
    return PlainTextResponse(str(response), media_type="application/xml")


