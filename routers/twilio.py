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
            data = await websocket.receive_text()
            
            response_audio = generate_response_audio()
            
            await websocket.send_bytes(response_audio)

    except websockets.ConnectionClosedError:
        print("Connection Closed")


@app.post("/receive-audio/")
async def twilio_voice():
    response = VoiceResponse()
    response.say("Say something")
    response.start().stram(url=f"wss://{BASE_API_URL}/media-stream")
    return PlainTextResponse(str(response), media_type="application/xml")

def generate_response_audio():
    return b""

