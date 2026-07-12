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
from PIL import Image

@app.on_message(filters.command("crop"))
async def crop_image(client, message: Message):
    user_id = message.from_user.id

    if user_id not in user_images:
        return await message.reply_text("❌ Pehle photo bhejo.")

    input_file = user_images[user_id]
    output_file = f"{DOWNLOAD_PATH}/{user_id}_crop.jpg"

    img = Image.open(input_file)

    width, height = img.size
    size = min(width, height)

    left = (width - size) // 2
    top = (height - size) // 2
    right = left + size
    bottom = top + size

    img = img.crop((left, top, right, bottom))
    img.save(output_file)

    await message.reply_photo(output_file)

if __name__ == "__main__":
    print("Bot Started...")
    app.run()