import os
import sys
import pytesseract
from PIL import Image
from common import utils

def GetScore():
    image = os.path.join(os.getcwd(), "results", "geekbench.png")
    result = {
            'Single-Core Score': None,
            'Multi-Core Score': None,
    }

    text = pytesseract.image_to_string(Image.open(image), lang="eng")
    lines = text.splitlines()
    for index in range(0, len(lines)):
        line = lines[index]
        for key in result:
            if key in line:
                result[key] = lines[index - 2].strip()


    print(result)
    return result

