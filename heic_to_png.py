import os
from PIL import Image
import pillow_heif

def conv(heic_file, image_dir_path):
    heic_path = os.path.join(image_dir_path, heic_file)
    png_file = os.path.splitext(heic_file)[0] + '.png'
    png_path = os.path.join(image_dir_path, png_file)

    heif_file = pillow_heif.read_heif(heic_path)

    image = Image.frombytes(
        heif_file.mode,
        heif_file.size,
        heif_file.data,
        "raw",
        heif_file.mode,
        heif_file.stride,
    )
    image.save(png_path, 'PNG')

    return png_file
