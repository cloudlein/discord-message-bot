# core/config.py
from dotenv import load_dotenv
import os

load_dotenv()

DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")

API_HOST = os.getenv("API_HOST", "http://127.0.0.1")
API_PORT = os.getenv("API_PORT", "8000")

# Base API URL
API_BASE = f"{API_HOST}:{API_PORT}"

# Specific endpoints
SEND_MESSAGE_ENDPOINT = f"{API_BASE}/send-message"

# Mongo Config
MONGO_USERNAME = os.getenv("MONGO_USERNAME")
MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")
MONGO_PORT = os.getenv("MONGO_PORT", "27017")
MONGO_EXPRESS_PORT = os.getenv("MONGO_EXPRESS_PORT", "8081")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME")
MONGO_URI=f"mongodb://${MONGO_USERNAME}:${MONGO_PASSWORD}@mongo:27017/"
