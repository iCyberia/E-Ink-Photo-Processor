from PIL import Image, ImageOps
import os
import tkinter as tk
from tkinter import filedialog

def browse_and_process_image():
    # Open a file dialog to browse and select a photo
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    file_path = filedialog.askopenfilename(title="Select a photo", filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp;*.gif")])
    
    if not file_path:
        print("No file selected.")
        return

    # Open the image
    img = Image.open(file_path)

    # Convert to grayscale
    img = img.convert("L")

    # Resize to 280 on the short side
    aspect_ratio = img.width / img.height
    if img.width < img.height:
        new_width = 280
        new_height = int(new_width / aspect_ratio)
    else:
        new_height = 280
        new_width = int(new_height * aspect_ratio)
    img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)

    # Crop the longer side to 480
    if new_width < new_height:
        top = (new_height - 480) / 2
        bottom = top + 480
        img = img.crop((0, top, new_width, bottom))
    else:
        left = (new_width - 480) / 2
        right = left + 480
        img = img.crop((left, 0, right, new_height))

    # Rotate clockwise
    img = img.rotate(-90, expand=True)

    # Save the modified photo as a copy in the same directory
    base, ext = os.path.splitext(file_path)
    new_file_path = f"{base}_processed{ext}"
    img.save(new_file_path)
    print(f"Processed image saved as {new_file_path}")

if __name__ == "__main__":
    browse_and_process_image()
