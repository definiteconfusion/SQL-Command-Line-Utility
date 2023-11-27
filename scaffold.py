import os
import json

def databaseLocator(folder_path):
    files_with_extension = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".db"):
                files_with_extension.append(os.path.join(root, file))
    return files_with_extension

def datachache(data):
    data = {
        "path":data
    }
    with open("data.json", 'w') as json_file:
        json.dump(data, json_file)
        
def initsetup():
    with open("data.json", 'r') as json_file:
        data = json.load(json_file)
    return data