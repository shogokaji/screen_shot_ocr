from PIL import Image
import pyperclip
import os
from pathlib import Path
import sys
import heic_to_png
import extract

ALLOWED_EXTENSIONS = ['.png', '.jpg', '.jpeg', '.heic']

# デスクトップ上の最後に作成されたファイルのパスを取得
def get_latest_image_on_desktop():
    desktop_path = Path.home() / "Desktop"

    try:
        files = sorted(desktop_path.glob("*"), key=os.path.getmtime, reverse=True)
    except:
        print("Failed to retrieve files from desktop.")
        return None

    for file in files:
        if file.is_dir() or file.name.startswith("."):
            continue

        if file.suffix.upper() == '.HEIC':
            return heic_to_png.conv(file, desktop_path)

        if any(file.name.endswith(extension) for extension in ALLOWED_EXTENSIONS):
            return file

    print("No suitable image found on desktop.")
    return None

def main(lang):
    image_path = get_latest_image_on_desktop()

    try:
        with Image.open(image_path) as image:
            text = extract.extract(image, lang)
    except Exception as e:
        print("fail to extract")
        return
    print(text)
    pyperclip.copy(text)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        lang = sys.argv[1]
    else:
        lang = "eng"

main(lang)
