from pydantic import BaseModel

class MessageRequest(BaseModel):
    server: str
    channel: str
    message: str
