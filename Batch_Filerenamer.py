import os 
import shutil
folder_path=r"D:\C programming codes 3rd sem lab"
prefix=input("Enter a prefix for the renamed files: ")
files=os.listdir(folder_path)
for i, file in enumerate(files, start=1):
    if file.endswith((".jpg", ".jpeg", ".png")) and os.path.isfile(os.path.join(folder_path, file)):
        old=os.path.join(folder_path, file)
        name,extension=os.path.splitext(file)
        new_name=f"{prefix}_{i}{extension}"
        new=os.path.join(folder_path, new_name)
        os.rename(old, new) 
print("All files have been renamed successfully.")  

