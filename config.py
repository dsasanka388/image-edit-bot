import os

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

DOWNLOAD_PATH = "downloads"
OUTPUT_PATH = "output"

os.makedirs(DOWNLOAD_PATH, exist_ok=True)
os.makedirs(OUTPUT_PATH, exist_ok=True)
