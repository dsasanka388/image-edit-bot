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
@app.on_message(filters.command("bw"))
async def bw_command(client, message: Message):
    user_id = message.from_user.id

    if user_id not in user_images:
        return await message.reply_text("❌ Pehle ek photo bhejo.")

    input_file = user_images[user_id]
    output_file = f"{OUTPUT_PATH}/{user_id}_bw.jpg"

    black_white(input_file, output_file)

    await message.reply_photo(output_file)


@app.on_message(filters.command("blur"))
async def blur_command(client, message: Message):
    user_id = message.from_user.id

    if user_id not in user_images:
        return await message.reply_text("❌ Pehle ek photo bhejo.")

    input_file = user_images[user_id]
    output_file = f"{OUTPUT_PATH}/{user_id}_blur.jpg"

    blur(input_file, output_file)

    await message.reply_photo(output_file)


@app.on_message(filters.command("sharpen"))
async def sharpen_command(client, message: Message):
    user_id = message.from_user.id

    if user_id not in user_images:
        return await message.reply_text("❌ Pehle ek photo bhejo.")

    input_file = user_images[user_id]
    output_file = f"{OUTPUT_PATH}/{user_id}_sharp.jpg"

    sharpen(input_file, output_file)

    await message.reply_photo(output_file)
@app.on_message(filters.command("rotate"))
async def rotate_command(client, message: Message):
    user_id = message.from_user.id

    if user_id not in user_images:
        return await message.reply_text("❌ Pehle ek photo bhejo.")

    input_file = user_images[user_id]
    output_file = f"{OUTPUT_PATH}/{user_id}_rotate.jpg"

    rotate(input_file, output_file)

    await message.reply_photo(output_file)


@app.on_message(filters.command("resize"))
async def resize_command(client, message: Message):
    user_id = message.from_user.id

    if user_id not in user_images:
        return await message.reply_text("❌ Pehle ek photo bhejo.")

    input_file = user_images[user_id]
    output_file = f"{OUTPUT_PATH}/{user_id}_resize.jpg"

    resize_image(input_file, output_file)

    await message.reply_photo(output_file)


@app.on_message(filters.command("crop"))
async def crop_command(client, message: Message):
    user_id = message.from_user.id

    if user_id not in user_images:
        return await message.reply_text("❌ Pehle ek photo bhejo.")

    input_file = user_images[user_id]
    output_file = f"{OUTPUT_PATH}/{user_id}_crop.jpg"

    crop_center(input_file, output_file)

    await message.reply_photo(output_file)
@app.on_message(filters.command("removebg"))
async def removebg_command(client, message: Message):
    user_id = message.from_user.id

    if user_id not in user_images:
        return await message.reply_text("❌ Pehle ek photo bhejo.")

    input_file = user_images[user_id]
    output_file = f"{OUTPUT_PATH}/{user_id}_nobg.png"

    try:
        remove_background(input_file, output_file)
        await message.reply_photo(output_file)
    except Exception as e:
        await message.reply_text(f"❌ Error: {e}")


@app.on_message(filters.command("help"))
async def help_command(client, message: Message):
    await message.reply_text(
        "📷 Image Edit Bot\n\n"
        "1. Send a photo\n"
        "2. Then use any command:\n\n"
        "/bw\n"
        "/blur\n"
        "/sharpen\n"
        "/rotate\n"
        "/resize\n"
        "/crop\n"
        "/removebg"
    )


if __name__ == "__main__":
    print("Bot Started...")
    app.run()
