#!/usr/bin/python

from common import utils
from PIL import Image
import pytesseract
import sys
import os

def GetScore():
    image = os.path.join(os.getcwd(),"results","caffeinemark.png")
    result = {
            "Overall score" : None,
    }

    text = pytesseract.image_to_string(Image.open(image), lang="eng")
    for line in text.splitlines():
        for key in result:
            if key in line:
                result[key] = (line.split("=")[1]).strip()
            

    print(result)
    return result

