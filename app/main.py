import os
from dotenv import load_dotenv
from app.bot import start_bot

if __name__ == "__main__":
    load_dotenv()
    start_bot()
