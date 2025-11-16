import asyncio
from contextlib import asynccontextmanager

from api.routers.send_message import router as send_message_router

from core.logger import logger
from fastapi import FastAPI

from bot.client import client
from core import config

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    discord_task = asyncio.create_task(
        client.start(config.DISCORD_BOT_TOKEN)
    )
    logger.info("Discord bot starting...")

    # Pass control back to FastAPI
    yield

    # Shutdown
    try:
        logger.info("Shutting down Discord bot...")
        await client.close()
        discord_task.cancel()
        logger.info("Discord bot stopped.")
    except Exception as e:
        logger.exception("Error shutting down Discord bot: ", e)

app = FastAPI(
    title="Discord message bot",
    lifespan=lifespan
)

app.include_router(send_message_router)
