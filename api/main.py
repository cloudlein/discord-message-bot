from fastapi import FastAPI
from pydantic import BaseModel
import  asyncio
from bot.dispatcher import MessageDispatcher
from bot.client import client
from core import config


app = FastAPI(title="Discord Message Bot")

class MessageRequest(BaseModel):
    server: str
    channel: str
    message: str

@app.on_event("startup")
async def startup_event():
    loop = asyncio.get_event_loop()
    loop.create_task(run_discord_bot())

async def run_discord_bot():
    try:
        await client.start(config.DISCORD_BOT_TOKEN)
    except Exception as e:
        print(f"Failed to start Discord bot: {e}")


@app.post("/send-message")
async def send_message(request: MessageRequest):
    await MessageDispatcher.send_message(request.server, request.channel, request.message)
    return {
        "status": "sent message!",
    }