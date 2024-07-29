#!/usr/bin/python3

from PIL import Image
import pytesseract


def test_example_function():
    """
        for mor information:
        visit: https://pypi.org/project/pytesseract/
        *tole
    """

    # Load the image
    image_path = '/home/OCR/ocr.png'
    image = Image.open(image_path)

    # Use pytesseract to do OCR on the image
    text = pytesseract.image_to_string(image, config='--psm 6', lang='eng')

    # List of available languages
    print(pytesseract.get_languages(config=''))

    # Strip whitespace and print the result
    print(text.strip())


# Call the function to execute the code inside it
test_example_function()
