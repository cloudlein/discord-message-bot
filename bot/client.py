import nextcord as discord
from core.logger import logger
from core import config

intents = discord.Intents.default()
intents.message_content = True # bot can read the message
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    logger.info(f"Bot connected as {client.user}")

def run_bot():
    client.run(config.DISCORD_BOT_TOKEN)


if __name__ == "__main__":
    run_bot()
