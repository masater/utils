import argparse
import os
from PIL import Image
from tkinter import Tk, filedialog

def select_file(title="select image", filetypes=(("All Files", "*.*"),)):
    """
    Open file dialog to select a file
    """
    root = Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title=title, filetypes=filetypes)
    root.destroy()
    return file_path

def select_save_location(default_name):
    """
    Open file dialog to select save location
    """
    root = Tk()
    root.withdraw()
    save_path = filedialog.asksaveasfilename(
        title="Save To",
        initialfile=default_name,
        filetypes=[("PNG Image", "*.png"), ("JPEG Image", "*.jpg"), ("WEBP Image", "*.webp"), ("All Files", "*.*")]
    )
    root.destroy()
    return save_path

def convert_image(input_file, output_file, output_format):
    """
    Convert an image file to a specified format.
    """
    with Image.open(input_file) as img:
        img.save(output_file, format=output_format)
    print(f"Converted {input_file} to {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert images between formats.")
    parser.add_argument("--input", "-i", type=str, help="Input image file path")
    parser.add_argument("--output", "-o", type=str, help="Output image file path")
    parser.add_argument("--format", "-f", type=str, default="PNG", help="Output format (default: PNG), ")

    args = parser.parse_args()

    input_file = args.input or select_file(title="Select Image", filetypes=[("Images", "*.png;*.jpg;*.jpeg;*.webp;*.bmp;*.gif")])
    if not input_file:
        print("No file selected. Exiting.")
        exit(1)

    
    output_format = args.format.upper()

    
    if not args.output:
        base, _ = os.path.splitext(input_file)
        output_file = f"{base}.{output_format.lower()}"
    else:
        output_file = args.output

    if not output_file:
        output_file = select_save_location(default_name=os.path.basename(input_file))

    if not output_file:
        print("No save location selected. Exiting.")
        exit(1)

    convert_image(input_file, output_file, output_format)
