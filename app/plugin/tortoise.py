# from torchaudio import save
from tortoise.api import TextToSpeech
from tortoise.utils.audio import load_voice

# If you want to test standalone tortoise
# you can do something like this

# audio = generate_audio("hello friends, i'm simona", "emma")
# save("test.wav", audio.squeeze(0).cpu(), 24000)

def generate_audio(text, voice):
    tts = TextToSpeech()

    voice_samples, conditioning_latents = load_voice(voice)

    return tts.tts_with_preset(
            text,
            voice_samples=voice_samples,
            conditioning_latents=conditioning_latents,
            preset="fast"
        )