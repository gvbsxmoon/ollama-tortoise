from pydantic import BaseModel

class StoryResponse(BaseModel):
    story: str