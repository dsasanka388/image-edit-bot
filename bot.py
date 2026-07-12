from pyrogram import Client, filters
from pyrogram.types import Message
import os

from config import (
    API_ID,
    API_HASH,
    BOT_TOKEN,
    DOWNLOAD_PATH,
    OUTPUT_PATH,
)

from utils.filters import (
    black_white,
    blur,
    sharpen,
    rotate,
    brightness,
    contrast,
)

from utils.resize import resize_image, crop_center
from utils.removebg import remove_background

app = Client(
    "ImageEditBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
)

user_images = {}

@app.on_message(filters.photo)
async def photo(client, message):
    await message.reply_text("✅ Image received successfully!")

app.run()
