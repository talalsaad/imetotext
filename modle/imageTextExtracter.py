import easyocr


url = 'https://drive.google.com/uc?id=1RDTkOnkfSSD3qTAgkIGOMUpbz0BLrX4X'


reader = easyocr.Reader(['en'],gpu=True) # Set the language here
results = reader.readtext(url) # Replace with your image's path




for result in results:
    print(result[1])

