import os 
import shutil
folder_path=r"D:\C programming codes 3rd sem lab"
files=os.listdir(folder_path)
for i, file in enumerate(files, start=1):
    old=os.path.join(folder_path, file)
    name,extension=os.path.splitext(file)
    new_name=f"{i}{extension}"
    new=os.path.join(folder_path, new_name)
    os.rename(old, new) 
print("All files have been renamed successfully.")  
