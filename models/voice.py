from fastapi import WebSocket


class VoiceHandler:
    websocket: WebSocket
    tts 
    stt 

    def __init__(self, websocket: WebSocket):
        self.websocket = websocket
        self.tts = ...
        self.stt = ...

    async def send_audio_chunks(self):
        async for audio_chunk in self.generate_audio_chunks():
            try:
               await self.websocket.send_bytes(audio_chunk)
            except Exception as e:
                print(f"Error sending audio: {e}")
                break


    async def receive_customer_audio(self):
        while True:
            try:
                customer_audio = await self.websocket.receive_bytes()
                if customer_audio:
                    return customer_audio

            except Exception as e:
                print(f"Error receiving audio: {e}")

    async def generate_audio_chunks(self):
        audio_data = [b"audio_chunk_1", b"audio_chunk_2", b"audio_chunk_3"]
        for chunk in audio_data:
            yield chunk


    async def handle_customer_input(self, customer_audio: bytes):
        pass

