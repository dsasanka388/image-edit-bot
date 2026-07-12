from pyrogram import Client, filters
from pyrogram.types import Message

from config import (
    API_ID,
    API_HASH,
    BOT_TOKEN,
    DOWNLOAD_PATH,
)

app = Client(
    "ImageEditBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
)

user_images = {}


@app.on_message(filters.command("start"))
async def start(client, message: Message):
    await message.reply_text(
        "👋 Welcome!\n\n"
        "📷 Send me a photo."
    )


@app.on_message(filters.photo)
async def save_photo(client, message: Message):
    user_id = message.from_user.id

    file_path = await message.download(
        file_name=f"{DOWNLOAD_PATH}/{user_id}.jpg"
    )

    user_images[user_id] = file_path

    await message.reply_text(
        "✅ Photo saved successfully!"
    )


if __name__ == "__main__":
    print("Bot Started...")
    app.run()