class VoiceHandler:
    api_key: str
    base_tts_url = "https://api.elevenlabs.io/v1"

    def __init__(self, api_key: str):
        self.api_key = api_key

    def tts(self, voice_id: str, text: str, chuck_size: int = 1024, output_path: str = "output.mp3"):
        pass
