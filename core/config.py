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
