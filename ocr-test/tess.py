#!/usr/bin/python

from PIL import Image
import pytesseract

#image = 'caffeinemark.png'
image = 'geekbench.png'
text = pytesseract.image_to_string(Image.open(image), lang="eng")
lines = text.splitlines()

result = {
    'Single-Core Score': None,
    'Multi-Core Score': None,
}

for index in range(0, len(lines)):
    line = lines[index]
    for key in result:
        if key in line:
            result[key] = lines[index - 2].strip()

print (result)

