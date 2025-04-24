#Same functionality as image_converter, but minimal qad implementation. 
from PIL import Image

OUTPUT_FORMAT = "PNG" # "WEBP", "JPEG"
INPUT_FILE = "your_image.webp" #your path to the image - can be relative or absolute path.
OUTPUT_FILE = "your_new_image.png" #! update ending too

with Image.open(INPUT_FILE) as img:
    img.save(OUTPUT_FILE, format=OUTPUT_FORMAT)


print(f"Converted {INPUT_FILE} to {OUTPUT_FILE}")