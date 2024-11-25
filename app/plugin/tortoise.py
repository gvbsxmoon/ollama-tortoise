
from tortoise.api import TextToSpeech
from tortoise.utils.audio import load_voice

def generate_audio(text, voice):
    tts = TextToSpeech()

    voice_samples, conditioning_latents = load_voice(voice)

    return tts.tts_with_preset(
        text,
        voice_samples=voice_samples,
        conditioning_latents=conditioning_latents,
        preset="fast"
        )