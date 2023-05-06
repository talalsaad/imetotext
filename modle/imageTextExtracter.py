import pytesseract
from PIL import Image
import re


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Grayscale, Gaussian blur, Otsu's threshold
image = Image.open('test.jpg')



# Perform text extraction
data = pytesseract.image_to_string(image, lang='eng', config='--psm 6')

fields = {
    'Device name': '',
    'Processor': '',
    'Installed RAM': '',
    'System type': '',
}

for field in fields:
    pattern = field + r'\s+(.*)'
    match = re.search(pattern, data)
    if match:
        fields[field] = match.group(1)

print(fields)