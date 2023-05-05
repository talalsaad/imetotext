import os
import shutil
import easyocr

# Create an EasyOCR reader object
reader = easyocr.Reader(['en'])


# Set paths for input and output folders
input_folder = 'x'
output_folder = 'y'

# Create output folder if it does not exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Loop through files in input folder
for file_name in os.listdir(input_folder):
    # Check if file is an image
    if file_name.endswith('.png') or file_name.endswith('.jpg') or file_name.endswith('.jpeg'):
        # Construct full path for input and output files
        input_path = os.path.join(input_folder, file_name)
        output_path = os.path.join(output_folder, file_name)
        # Read image using EasyOCR
        results = reader.readtext(input_path)
        # Define keywords to search for in the text
        keywords = ['Device name', 'Processor', 'Installed RAM', 'Device ID', 'System type']
        # Create a dictionary to store the extracted information
        info = {}
        # Loop through the results and extract relevant information
        for i, result in enumerate(results):
            for keyword in keywords:
                if keyword in result[1]:
                    # Extract value after the keyword and store in dictionary
                    value = results[i+1][1].strip()
                    info[keyword] = value
        # Print extracted information

        if info=={}:
            shutil.move(input_path, 'delete')
            continue

        with open('data.txt', 'a') as f:
            f.write(f'File: {file_name}\n'
            f'Device Name: {info.get("Device name", "")}\n'
            f'Processor: {info.get("Processor", "")}\n'
            f'Installed RAM: {info.get("Installed RAM", "")}\n'
            f'Device ID: {info.get("Device ID", "")}\n'
            f'System Type: {info.get("System type", "")}\n'
            f'//////////////////////////////////////////////////////////////////////\n\n')

        print(info)

        # Move input file to output folder
        
        
        shutil.move(input_path, output_path)
            


        
