from datetime import datetime
from pydantic import BaseModel

class MessageDb(BaseModel):
    message_id: str
    content: str
    author: str
    channel_id: str
    server_id: str
    created_at: datetime
    updated_at: datetime