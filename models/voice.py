import io
import math
import numpy as np
import soundfile as sf
import time
from TTS.api import TTS


class VoiceHandler:
    tts: TTS
    global_audio: np.array | None = None

    def __init__(self):
        self.tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False)

    def text_to_speech(self):
        pass

    def text_to_numpy_generator(self, text: str):
        sentences = text.split(". ")

        for sentence in sentences:
            if not sentence.strip():
                continue
            waveform = self.tts.tts(sentence)

            if self.global_audio is None:
                self.global_audio = waveform
            else:
                self.global_audio = np.concatenate((self.global_audio, waveform))

    def chunk_audio_generator(self, chunk_duration=0.5, samplerate=22050):
        chunk_size = int(chunk_duration * samplerate)

        for chunk in self.chunk_generator(chunk_size):
            buffer = io.BytesIO()
            sf.write(buffer, chunk, samplerate=samplerate, format="WAV")
            yield buffer.getvalue()
            

    def chunk_generator(self, chunk_size):
        c = 0
        while self.global_audio is None:
            time.sleep(0.1)
            c += 0.1
            if c > 10:
                raise ValueError("Global Audio not initialized")
        chunk = self.global_audio[:chunk_size]
        self.global_audio = self.global_audio[chunk_size:]
        yield chunk



    def test_output(self, output_file="output.wav"):
        all_chuks = []
        for chunk in self.chunk_audio_generator():
            all_chuks.append(chunk)

        concatenated_chunks = b"".join(all_chuks)
        with open (output_file, "wb") as f:
            f.write(concatenated_chunks)

    def text_to_speech_test(self):
        self.tts.tts_to_file(text="As the sun began to set over the horizon, casting a warm golden glow across the landscape, I took a moment to reflect on the day. The gentle breeze rustled the leaves of the trees, creating a soothing symphony of nature that wrapped around me like a comforting blanket. I remembered the laughter shared with friends, the moments of joy that filled the air, and the beauty of the world around me. Each sound, each sight, was a reminder of the simple pleasures in life that often go unnoticed. As the colors of the sky transformed from vibrant oranges to soft purples, I felt a sense of peace wash over me, a reminder to cherish each fleeting moment as it comes.", file_path="output3.wav")

if __name__ == "__main__":
    voice = VoiceHandler()
    voice.text_to_speech_test()
