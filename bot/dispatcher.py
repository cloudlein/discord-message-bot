import nextcord as discord
from bot.client import client
from core.logger import logger

class MessageDispatcher:
    @staticmethod
    async def send_message(server_name: str, channel_name: str, message: str):
        guild = discord.utils.get(client.guilds, name=server_name)
        if not guild:
            logger.error(f"Guild '{server_name}' not found.")
            return {"error": f"Guild '{server_name}' not found."}

        channel = discord.utils.get(guild.text_channels, name=channel_name)
        if not channel:
            logger.error(f"Channel '{channel_name}' not found.")
            return {"error": f"Channel '{channel_name}' not found."}

        await channel.send(message)
        logger.info(f"Message sent to #{channel_name} in {server_name}")
        return {"success": True, "server": server_name, "channel": channel_name}
