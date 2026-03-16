import os 
import shutil
folder_path=r"C:\Users\HP\Desktop\New folder (2)"
files=os.listdir(folder_path)
for i, file in enumerate(files, start=1):
    old=os.path.join(folder_path, file)
    name,extension=os.path.splitext(file)
    new_name=f"{i}{extension}"
