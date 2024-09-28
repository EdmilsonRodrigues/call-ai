class VoiceHandler:
    api_key: str
    base_tts_url = "https://api.elevenlabs.io/v1"

    def __init__(self, api_key: str):
        self.api_key = api_key

    def tts(self, voice_id: str, text: str, chuck_size: int = 1024, output_path: str = "output.mp3"):
        url = self.base_tts_url + "/text-to-speech/{}"
        headers = {
                "Accept": "application/json",
                "xi-api-key": self.api_key
            }

        data = {
              "text": text,
              "model_id": "eleven_multilingual_v2"
              "voice_settings": {
                    "stability": 0.5,
                    "similarity_boost": 0.8,
                    "style": 0.0,
                    "use_speaker_boost": True
                  }
            }
