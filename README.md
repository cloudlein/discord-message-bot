# Discord Message Bot Architecture (Python)

## 🧩 1. Problem Analysis
The goal is to build a system that allows sending messages to Discord servers via a bot account.  
The system must support **two control modes**:
- Command Line Interface (CLI)
- REST API (HTTP-based)

This allows the user to choose which server (guild) and channel to send a message to through either interface.

---

## ⚙️ 2. Core Requirements

### Technologies & Libraries

| Component | Recommended Technology |
|------------|-------------------------|
| Language | Python 3.10+ |
| Discord Bot | discord.py / nextcord |
| REST API | FastAPI |
| CLI | Typer or argparse |
| Auth | API Key or JWT |
| Logging | loguru or logging |
| Config | python-dotenv |
| Deployment | Docker (optional) |

---

## 🏗️ 3. System Architecture

```
                    +---------------------+
                    |  Discord Bot (Python)|
                    |  using discord.py    |
                    +----------+-----------+
                               |
                               v
               +------------------------------+
               |     Message Dispatcher       |
               | (Abstraction Layer)          |
               | - Send message               |
               | - Fetch servers/channels     |
               +------------------------------+
                     ^                 ^
                     |                 |
          +----------+                 +-------------+
          |                                        |
+------------------------+        +-----------------------------+
| Command Line Interface |        |      REST API (FastAPI)     |
| - Select server/channel|        | - POST /send-message        |
| - Send message text    |        | - GET /servers, /channels   |
+------------------------+        +-----------------------------+
          |                                        |
          +--------------> Shared Service Layer <---+
                              (Bot Core)
```

### Explanation
- **Bot Core (discord.py)**: Manages the Discord client and connection.
- **Message Dispatcher**: Unified interface for sending messages.
- **CLI**: Allows manual interaction from terminal.
- **REST API**: Exposes endpoints for programmatic access.
- **Shared Service Layer**: Ensures CLI and API communicate with the same bot instance.

---

## 🔐 4. Configuration (.env)
```
DISCORD_BOT_TOKEN=your_discord_bot_token
API_PORT=8000
```

---

## 📁 5. Folder Structure

```
discord-message-bot/
├── bot/
│   ├── __init__.py
│   ├── client.py           # Discord client setup
│   ├── dispatcher.py       # Message sending abstraction
│   ├── events.py           # on_ready, etc.
├── api/
│   ├── __init__.py
│   ├── main.py             # FastAPI app & routes
│   ├── routes/
│   │   ├── message.py
│   │   ├── guild.py
├── cli/
│   ├── main.py             # Typer CLI entrypoint
├── core/
│   ├── config.py
│   ├── logger.py
├── requirements.txt
├── .env
└── run.py                  # entrypoint script
```

---

## 🧠 6. Workflow Overview

### CLI Mode
```
python -m cli.main send --server "My Server" --channel "general" --message "Hello World!"
```
Steps:
1. CLI parses arguments.
2. Calls MessageDispatcher.
3. Dispatcher resolves server & channel IDs.
4. Bot sends the message.

### REST API Mode
**Endpoint:**
```
POST /send-message
```
**Body:**
```json
{
  "server": "My Server",
  "channel": "general",
  "message": "Hello from API!"
}
```

Steps:
1. API receives request.
2. Calls MessageDispatcher.
3. Sends message via bot client.
4. Returns success or failure response.

---

## ⚖️ 7. Architectural Considerations

| Challenge | Solution |
|------------|-----------|
| Bot must stay connected | Run bot in background (async thread) |
| Shared event loop with API | Use FastAPI with asyncio |
| Server/channel access | Cache guild/channel list on startup |
| Discord rate limits | Add message delay or queue |
| API security | Use API key validation |

---

## 🚀 8. Future Extensions

| Feature | Description |
|----------|-------------|
| 🔄 Scheduler | Send scheduled messages |
| 🧩 Template | Markdown message templates |
| 🗃️ Database | Store message history |
| 📊 Dashboard | Web UI for logs |
| 🧠 Command Registry | CLI autocomplete |
| 📡 WebSocket | Real-time updates |

---

## 🧩 9. Next Steps
1. Initialize project repo.
2. Implement Discord bot client (`client.py`).
3. Add MessageDispatcher abstraction.
4. Implement CLI commands.
5. Build REST API endpoints.
6. Add authentication and logging.

---
