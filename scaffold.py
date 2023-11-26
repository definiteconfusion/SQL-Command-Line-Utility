import os
import json

def databaseLocator(folder_path):
    files_with_extension = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".db"):
                files_with_extension.append(os.path.join(root, file))
    return files_with_extension

def initsetup(data):
    with open("data.json", 'w') as json_file:
        json.dump(data, json_file)