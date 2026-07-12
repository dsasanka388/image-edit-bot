from PIL import Image

def resize_image(input_path, output_path, width=1024, height=1024):
    img = Image.open(input_path)
    img = img.resize((width, height))
    img.save(output_path)

def crop_center(input_path, output_path, width=512, height=512):
    img = Image.open(input_path)
    img_width, img_height = img.size

    left = (img_width - width) / 2
    top = (img_height - height) / 2
    right = (img_width + width) / 2
    bottom = (img_height + height) / 2

    img = img.crop((left, top, right, bottom))
    img.save(output_path)
