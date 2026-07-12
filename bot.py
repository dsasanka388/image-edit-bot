import os
import logging

logging.basicConfig(level=logging.INFO)

from pyrogram import Client, filters
from pyrogram.types import Message
from PIL import Image
app = Client(
    "ImageEditBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
)

os.makedirs("downloads", exist_ok=True)

user_images = {}
@app.on_message(filters.photo)
async def save_photo(client, message: Message):
    user_id = message.from_user.id

    file_path = await message.download(
        file_name=f"downloads/{user_id}.jpg"
    )

    user_images[user_id] = file_path

    await message.reply_text("✅ Photo Saved Successfully!")
