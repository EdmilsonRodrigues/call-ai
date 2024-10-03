from TTS.api import TTS


class VoiceHandler:
    tts: TTS

    def __init__(self):
        self.tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False)

    def tts(self):
        pass

    def text_to_numpy_generator(self):
        pass

    def chunk_audio_generator(self):
        pass

    def test_output(self):
        pass

    def text_to_speech_test(self):
        self.tts.tts_to_file(text="Hello, welcome to the world of open source text to speech.", file_path="output.wav")
        self.tts.tts_to_file(text="This is a test of speed", file_path="output2.wav")
        self.tts.tts_to_file(text="As the sun began to set over the horizon, casting a warm golden glow across the landscape, I took a moment to reflect on the day. The gentle breeze rustled the leaves of the trees, creating a soothing symphony of nature that wrapped around me like a comforting blanket. I remembered the laughter shared with friends, the moments of joy that filled the air, and the beauty of the world around me. Each sound, each sight, was a reminder of the simple pleasures in life that often go unnoticed. As the colors of the sky transformed from vibrant oranges to soft purples, I felt a sense of peace wash over me, a reminder to cherish each fleeting moment as it comes.", file_path="output3.wav")

if __name__ == "__main__":
    voice = VoiceHandler()
    voice.text_to_speech_test()
