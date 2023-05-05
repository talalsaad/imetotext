from typing import List, Dict
from modle.connect import GoogleSheet

class ImageGetter:
        
    def __init__(self, spreadsheet_id: str, api_key: str):
        self.sheet = GoogleSheet(spreadsheet_id, api_key)
        
        with open('C:\\Users\\talal\\Desktop\\imetotext\\\modle\\counter.txt', 'r') as file:
            self.id = int(file.readline().strip())

    def lists(self) -> List[Dict[str, str]]:
        values = self.sheet.get_values('Sheet!D2:D')
        images = []
        

        for row in values:
            
            image = {"id":self.id, "url":row[0]}
            images.append(image)
            self.id += 1
        with open('C:\\Users\\talal\\Desktop\\imetotext\\\modle\\counter.txt', 'w') as file:
            file.write(str(self.id))

        return images
