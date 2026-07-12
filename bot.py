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
@app.on_message(filters.command("start"))
async def start(client, message: Message):
    await message.reply_text(
        "👋 Welcome to Image Edit Bot!\n\n"
        "📷 Send me a photo first.\n\n"
        "Commands:\n"
        "/bw - Black & White\n"
        "/blur - Blur\n"
        "/sharpen - Sharpen\n"
        "/rotate - Rotate\n"
        "/resize - Resize (1024x1024)\n"
        "/removebg - Remove Background"
    )


@app.on_message(filters.photo)
async def save_photo(client, message: Message):
    user_id = message.from_user.id

    file_path = await message.download(
        file_name=f"{DOWNLOAD_PATH}/{user_id}.jpg"
    )

    user_images[user_id] = file_path

    await message.reply_text(
        "✅ Image received successfully!\n\n"
        "Now send one of these commands:\n"
        "/bw\n"
        "/blur\n"
        "/sharpen\n"
        "/rotate\n"
        "/resize\n"
        "/removebg"
    )
