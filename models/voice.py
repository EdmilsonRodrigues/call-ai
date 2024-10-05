import io
import multiprocessing
import numpy as np
import soundfile as sf
import time
from TTS.api import TTS


class VoiceHandler:
    tts: TTS

    def __init__(self):
        self.tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False)

    def text_to_speech(self, text: str):
        manager = multiprocessing.Manager()
        shared_audio = manager.list()  # Shared list for audio waveforms
        is_done = manager.Value("b", False)  # Shared boolean initialized to False
        lock = manager.Lock()

        process = multiprocessing.Process(target=self._text_to_numpy_generator, args=(text, shared_audio, lock, is_done))
        process.start()

        yield from self._chunk_audio_generator(shared_audio, is_done, lock)

    def _text_to_numpy_generator(self, text: str, shared_audio, lock, is_done):
        sentences = text.split(". ")
        for sentence in sentences:
            if not sentence.strip():
                continue
            waveform = self.tts.tts(sentence)

            # Append the waveform to the shared_audio
            with lock:  # Ensure only one process modifies it at a time
                shared_audio.append(waveform)

        # Indicate completion by setting is_done to True
        is_done.value = True  # Set the shared boolean to True when done

    def _chunk_audio_generator(
        self,
        shared_audio,
        is_done,
        lock,
        chunk_duration: float = 0.5,
        samplerate: int = 22050,
    ):
        chunk_size = int(chunk_duration * samplerate)

        while True:
            with lock:
                if len(shared_audio) == 0:
                    if is_done.value:
                        break  # Exit if processing is done and no more audio is available
                    time.sleep(0.1)  # Wait until there's audio available
                    continue

                # Create a single array from all waveforms in shared_audio
                all_audio = np.concatenate(list(shared_audio))

                if len(all_audio) < chunk_size:
                    if is_done.value:
                        break  # Exit if processing is done and no more audio is available
                    chunk = all_audio[:]
                    remaining_audio = []
                else:
                    chunk = all_audio[:chunk_size]
                    remaining_audio = all_audio[chunk_size:]

                # Update shared_audio
                shared_audio[:] = list(remaining_audio)

                buffer = io.BytesIO()
                sf.write(buffer, chunk, samplerate=samplerate, format="WAV")
                yield buffer.getvalue()

    def test_output(self, text: str, output_file: str = "output.wav"):
        all_chuks = []
        for chunk in self.text_to_speech(text):
            all_chuks.append(chunk)

        concatenated_chunks = b"".join(all_chuks)
        with open(output_file, "wb") as f:
            f.write(concatenated_chunks)

    def text_to_speech_test(self):
        self.test_output(
            text="As the sun began to set over the horizon, casting a warm golden glow across the landscape, I took a moment to reflect on the day. The gentle breeze rustled the leaves of the trees, creating a soothing symphony of nature that wrapped around me like a comforting blanket. I remembered the laughter shared with friends, the moments of joy that filled the air, and the beauty of the world around me. Each sound, each sight, was a reminder of the simple pleasures in life that often go unnoticed. As the colors of the sky transformed from vibrant oranges to soft purples, I felt a sense of peace wash over me, a reminder to cherish each fleeting moment as it comes.",
            output_file="output4.wav",
        )


if __name__ == "__main__":
    voice = VoiceHandler()
    voice.text_to_speech_test()
