from PIL import Image
import pytesseract

#image = 'caffeinemark.png'
image = 'geekbench.png'
text = pytesseract.image_to_string(Image.open(image), lang="eng")
print(text)

