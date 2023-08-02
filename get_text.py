from pytesseract import pytesseract


def get_text(img):
    text = ""
    try:
        text = pytesseract.image_to_string(img).strip()
        parsing_successful = True
    except Exception as e:
        parsing_successful = False
    return parsing_successful, text