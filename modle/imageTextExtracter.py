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

    
def extract_ram(data):
    match = re.search(r'Installed\s+RAM\s+(.*?)\s+', data)
    if match:
        return match.group(1)
    match = re.search(r'Installed\s+memory\s+\(RAM\)\s+(.*?)\s+', data)
    if match:
        return match.group(1)
    return None


def extract_device_name(data):
    match = re.search(r'Device name ?\s+(.*)', data)
    if match:
        return match.group(1)
    
    match = re.search(r'Computer name ?\s+(.*)', data)
    if match:
        return match.group(1)
    return None
   
"""
    'https://drive.google.com/file/d/1xxbtmSSrxO0-ZIpSgYRPAr-m1L9MQ2Lu/view?usp=share_link',
    'https://drive.google.com/file/d/1YERKgFTc7Ru8UJUrWk19Fm1VUhSaPgz4/view?usp=share_link',
    'https://drive.google.com/file/d/1J72Ep1ZW47HSf0s1yVyFYDzntwR2eHld/view?usp=share_link',
    'https://drive.google.com/file/d/1VxzudZpD6av5GBFJc7cm2KLdw7CfgEgW/view?usp=share_link'

"""
    
#'55 - Copy.png'

urls = [
    
   
    'https://drive.google.com/file/d/1xxbtmSSrxO0-ZIpSgYRPAr-m1L9MQ2Lu/view?usp=share_link',
    'https://drive.google.com/file/d/1Ex0cVMl_I5P2IX9Cj-nlG70p-jl6x5Iy/view?usp=share_link',
    'https://drive.google.com/file/d/1VxzudZpD6av5GBFJc7cm2KLdw7CfgEgW/view?usp=share_link'

    
]
for url in urls:
    url=f'https://drive.google.com/uc?export=download&id={get_drive_file_id(url)}'
    response = requests.get(url)
    
    ##image = Image.open(url)

    with open('.\\images\\test', 'wb') as f:
        f.write(response.content)

        
    time.sleep(2)
    #image = Image.open(f'.\\images\\{url}')
    image = Image.open('.\\images\\test')
    

    # Perform text extraction
    data = pytesseract.image_to_string(image,lang = 'eng',config='--psm 6')
    
    fields = {
    'Device name': '',
    'Processor': '',
    'RAM': '',
    'System type': '',
}

    
    if(extract_device_name(data)!=None):
        fields['Device name'] =extract_device_name(data)

    match = re.search(r'(Intel.*|Core.*|AMD.*).*', data)
    if match:
        fields['Processor'] = match.group(1)


    if(extract_ram(data)!=None):
        fields['RAM'] = extract_ram(data)
    

    match = re.search(r'System type?\s+(.*)', data)
    if match:
        fields['System type'] = match.group(1)
        
    print(data)
    print(fields)
