from api.schemas.message_schema import MessageRequest
from bot.dispatcher import MessageDispatcher
from fastapi import APIRouter

router = APIRouter()

@router.post("/send-message")
async def send_message(request: MessageRequest):
    await MessageDispatcher.send_message(request.server, request.channel, request.message)
    return {
        "status": "sent message!",
    }

