from rembg import remove
from PIL import Image

def remove_background(input_path, output_path):
    with open(input_path, "rb") as input_file:
        input_data = input_file.read()

    output_data = remove(input_data)

    with open(output_path, "wb") as output_file:
        output_file.write(output_data)

    img = Image.open(output_path)
    img.save(output_path)
