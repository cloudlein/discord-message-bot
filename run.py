import subprocess
import typer
from cli.main import app as cli_app
from core import config

app = typer.Typer(help="Main entry for Discord bot")

@app.command()
def bot():
    """Run discord bot only"""
    subprocess.run(["python", "-m", "bot.client"])

@app.command()
def api():
    """Run FastAPI server"""
    port = config.API_PORT
    subprocess.run(["uvicorn", "api.main:app", "--reload", "--port", port])

# integrasi CLI langsung
app.add_typer(cli_app, name="cli")

if __name__ == "__main__":
    app()
