from fastapi import FastAPI, HTTPException

from app.model.story_request import StoryRequest
from app.model.story_response import StoryResponse
from app.plugin.ollama import generate_story

app = FastAPI()

@app.post("/story/")
async def story(request: StoryRequest):
    # At the moment this will return just the story text from ollama plugin
    # go to /app/plugin/tortoise to see the TTS implementation
    
    try:
        story = await generate_story(request)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error during story generation: {str(e)}")
    
    return StoryResponse(story=story)

    # Save audio to a temporary file
    # audio_filename = f"{uuid.uuid4()}.wav"
    # audio = generate_audio(story, request.voice)
    # save(audio_filename, audio.squeeze(0).cpu(), 24000)

    # Return the audio file as a response
    # Cappellata below: this is not gonna work
    # return FileResponse(audio_filename, media_type="audio/wav", filename=audio_filename)
