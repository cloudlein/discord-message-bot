from pymongo import AsyncMongoClient
from core.config import MONGO_URI, MONGO_DB_NAME
from core.logger import  logger

client: AsyncMongoClient | None = None
db = None

async def connect_db():
    global client, db
    client = await AsyncMongoClient(MONGO_URI)
    db = client[MONGO_DB_NAME]
    logger.info(f"Connected to {MONGO_DB_NAME}")

async def close_db():
    global client
    if client:
        await client.close()
        logger.info(f"Closed connection {MONGO_DB_NAME}")