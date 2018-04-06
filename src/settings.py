import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.') / '.env'


def setup():
    print("Setting up bot...")
    load_dotenv(dotenv_path=env_path)
    print(os.getenv("DISCORD_TOKEN"))
