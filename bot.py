@app.on_message(filters.command("crop"))
async def crop_image(client, message: Message):
    await message.reply_text("Crop command received")

    user_id = message.from_user.id

    if user_id not in user_images:
        await message.reply_text("❌ Pehle photo bhejo.")
        return
from pyrogram import Client, filters
from pyrogram.types import Message
from PIL import Image

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
        "👋 Welcome!\n\n📷 Send me a photo."
    )


@app.on_message(filters.photo)
async def save_photo(client, message: Message):
    user_id = message.from_user.id

    file_path = await message.download(
        file_name=f"{DOWNLOAD_PATH}/{user_id}.jpg"
    )

    user_images[user_id] = file_path

    await message.reply_text("✅ Photo saved successfully!")
@app.on_message(filters.command("crop"))
async def crop_image(client, message: Message):
    user_id = message.from_user.id

    if user_id not in user_images:
        await message.reply_text("❌ Pehle photo bhejo.")
        return

    input_file = user_images[user_id]
    output_file = f"{DOWNLOAD_PATH}/{user_id}_crop.jpg"

    try:
        img = Image.open(input_file)

        width, height = img.size
        crop_size = min(width, height)

        left = (width - crop_size) // 2
        top = (height - crop_size) // 2
        right = left + crop_size
        bottom = top + crop_size

        cropped = img.crop((left, top, right, bottom))
        cropped.save(output_file, "JPEG", quality=95)

        await message.reply_photo(
            photo=output_file,
            caption="✅ Image cropped successfully!"
        )

    except Exception as e:
        await message.reply_text(f"❌ Crop failed:\n{e}")
if __name__ == "__main__":
    print("Bot Started...")
    app.run()