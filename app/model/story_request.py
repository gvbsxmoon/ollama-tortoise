from pydantic import BaseModel

class StoryRequest(BaseModel):
    character: str
    environment: str
    voice: str = "emma"
    model: str = "llama3.2"