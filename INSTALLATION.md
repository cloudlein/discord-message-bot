# Discord Message Bot

A simple Discord bot that can send messages via both **FastAPI** and **CLI**.

---

## Installation

### 1. Create Virtual Environment
```bash
  python -m venv venv
```
### 2. Activate Environment
Linux/macOS:
```bash
    source venv/bin/activate
```
Windows: 
```bash
  venv\Scripts\activate
```

### 3. Install Dependencies
```bash
  pip install -r requirements.txt
```

## Running the App
### Run the Discord Bot
```bash
    python run.py bot
```

### Run the FastAPI Server
```bash
    python run.py api
```
### Send message via CLI
```bash
    python run.py cli send "Server Name" "Channel Name" "Hello World!"
```

## Environment Variables
Create a .env file in the project root:
```dotenv
DISCORD_BOT_TOKEN=your_discord_bot_token_here
API_PORT=8000
API_URL=http://127.0.0.1:8000/send-message
```
