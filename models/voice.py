from TTS.api import TTS


class VoiceHandler:
    tts: TTS

    def __init__(self):
        self.tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False)

    def text_to_speech(self):
        self.tts.tts_to_file(text="Hello, welcome to the world of open-source text to speech.", file_path="output.wav")


if __name__ == "__main__":
    voice = VoiceHandler()

    voice.text_to_speech()
