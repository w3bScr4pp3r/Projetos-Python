import os
import shutil

path = "C:/Users/seu_usuario/Downloads"

# List all files in the directory
files = os.listdir(path)

# Define the extensions and their corresponding folders
extensions = {
    "pdf": "PDF Files",
    "doc": "Word Files",
    "docx": "Word Files",
    "exe": "Programs",
    "xls": "Excel Files",
    "xlsx": "Excel Files",
    "ppt": "PowerPoint Files",
    "pptx": "PowerPoint Files",
    "jpg": "Images",
    "jpeg": "Images",
    "png": "Images",
    "txt": "Text Files",
    "zip": "Archives",
    "rar": "Archives"
}

# Create the folders
for folder in extensions.values():
    if not os.path.exists(path + "/" + folder):
        os.makedirs(path + "/" + folder)

# Move the files to the corresponding folders
for file in files:
    name, ext = os.path.splitext(file)
    ext = ext[1:] # remove the dot (.)
    if ext in extensions:
        shutil.move(path + "/" + file, path + "/" + extensions[ext] + "/" + file)
