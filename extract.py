import pytesseract

IMAGE_MODE = 'RGB'

def extract(image, lang):
    converted_image = image.convert(IMAGE_MODE)
    text = pytesseract.image_to_string(converted_image, lang=lang)

    return text
