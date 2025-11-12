import typer
import httpx
from core import config

app = typer.Typer(help="Discord Message Bot CLI")


@app.command()
def send(server: str, channel: str, message: str):
    """Send message via FastAPI bot backend"""
    payload = {"server": server, "channel": channel, "message": message}
    try:
        response = httpx.post(config.SEND_MESSAGE_ENDPOINT, json=payload, timeout=10)
        if response.status_code == 200:
            typer.echo("Message sent successfully")
        else:
            typer.echo(f"Failed to send message: {response.text}")
    except Exception as e:
        typer.echo(f"Error: {e}")

if __name__ == "__main__":
    app()
