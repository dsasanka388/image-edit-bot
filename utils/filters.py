from PIL import Image, ImageFilter, ImageEnhance

def black_white(input_path, output_path):
    img = Image.open(input_path).convert("L")
    img.save(output_path)

def blur(input_path, output_path):
    img = Image.open(input_path)
    img = img.filter(ImageFilter.BLUR)
    img.save(output_path)

def sharpen(input_path, output_path):
    img = Image.open(input_path)
    img = img.filter(ImageFilter.SHARPEN)
    img.save(output_path)

def rotate(input_path, output_path, angle=90):
    img = Image.open(input_path)
    img = img.rotate(angle, expand=True)
    img.save(output_path)

def brightness(input_path, output_path, factor=1.5):
    img = Image.open(input_path)
    enhancer = ImageEnhance.Brightness(img)
    img = enhancer.enhance(factor)
    img.save(output_path)

def contrast(input_path, output_path, factor=1.5):
    img = Image.open(input_path)
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(factor)
    img.save(output_path)
