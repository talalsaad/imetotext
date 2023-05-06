import re
import pytesseract
import requests
from PIL import Image
import io
import time

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def get_drive_file_id(link):
    # Extract file ID from Google Drive link
    file_id_match = re.search(r'/d/([a-zA-Z0-9-_]+)', link)
    if file_id_match:
        return file_id_match.group(1)
    else:
        return None

    


urls = [
    
    'https://drive.google.com/file/d/1aGXDN6ILD1qKPggpD80QHjIPuytpfDqV/view?usp=share_link',
    'https://drive.google.com/file/d/1RDTkOnkfSSD3qTAgkIGOMUpbz0BLrX4X/view?usp=share_link'
    
    
]
for url in urls:
    url=f'https://drive.google.com/uc?export=download&id={get_drive_file_id(url)}'
    response = requests.get(url)
    
    #image = Image.open(io.BytesIO(response.content))

    with open('.\\images\\test.png', 'wb') as f:
        f.write(response.content)
    time.sleep(2)
    image = Image.open('.\\images\\test.png')
    

    # Perform text extraction
    data = pytesseract.image_to_string(image, lang='eng', config='--psm 6')
    print(data)
    fields = {
    'Device name': '',
    'Processor': '',
    'Installed': '',
    'System type': '',
}

for field in fields:
    pattern = field + r':?\s+(.*)'
    match = re.search(pattern, data)
    if match:
        fields[field] = match.group(1)
        # Get the entire line of text containing the match
        match_line = re.search(r'.*{}.*'.format(match.group(1)), data)
        if match_line:
            fields[field] = match_line.group(0)

    
    print(fields)
