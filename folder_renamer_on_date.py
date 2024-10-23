import os
import sys
from datetime import datetime
from collections import Counter
from PIL import Image
from PIL.ExifTags import TAGS

def get_image_taken_date(file_path):
    try:
        image = Image.open(file_path)
        exif_data = image._getexif()
        if exif_data:
            for tag, value in exif_data.items():
                tag_name = TAGS.get(tag, tag)
                if tag_name == 'DateTimeOriginal':
                    return datetime.strptime(value, '%Y:%m:%d %H:%M:%S').strftime('%Y%m%d')
    except Exception as e:
        print(f"Error reading EXIF data from {file_path}: {e}")
    return None

def get_most_common_date(folder_path):
    deepest_dirs = []
    for root, dirs, files in os.walk(folder_path):
        if not dirs:  # If there are no subdirectories, it's a deepest directory
            deepest_dirs.append(root)
    
    if not deepest_dirs:
        return None
    
    file_dates = []
    for dir_path in deepest_dirs:
        for file_name in os.listdir(dir_path):
            file_path = os.path.join(dir_path, file_name)
            if os.path.isfile(file_path):
                taken_date = get_image_taken_date(file_path)
                if taken_date:
                    file_dates.append(taken_date)
    
    if not file_dates:
        return None
    
    most_common_date = Counter(file_dates).most_common(1)[0][0]
    return most_common_date

def rename_folder(folder_path):
    if not os.path.exists(folder_path):
        print(f"Folder '{folder_path}' does not exist.")
        return
    
    most_common_date = get_most_common_date(folder_path)
    if not most_common_date:
        print("Could not determine the most common creation date.")
        return
    
    folder_name = os.path.basename(folder_path)
    new_folder_name = f"{most_common_date}_{folder_name.replace(' ', '_')}"
    new_folder_path = os.path.join(os.path.dirname(folder_path), new_folder_name)
    
    if os.path.exists(new_folder_path):
        print(f"Folder '{new_folder_path}' already exists.")
        return
    
    print(f"Old folder name: {folder_path}")
    print(f"New folder name: {new_folder_path}")
    confirm = input("Do you want to rename the folder? (yes/no): ").strip().lower()
    
    if confirm == 'yes':
        os.rename(folder_path, new_folder_path)
        print(f"Folder renamed to '{new_folder_path}'")
    else:
        print("Folder renaming cancelled.")

if __name__ == "__main__":
    # Loop through directories and confirm renaming with Enter
    base_folder_path = r"D:\Pictures_and_Videos"
    
    for folder_name in os.listdir(base_folder_path):
        folder_path = os.path.join(base_folder_path, folder_name)
        if os.path.isdir(folder_path):
            # Check if the folder name already contains a timestamp
            if not folder_name[:8].isdigit():
                most_common_date = get_most_common_date(folder_path)
                if most_common_date:
                    new_folder_name = f"{most_common_date}_{folder_name.replace(' ', '_')}"
                    new_folder_path = os.path.join(os.path.dirname(folder_path), new_folder_name)
                    print(f"Processing folder: {folder_path}")
                    print(f"Future folder name: {new_folder_path}")
                    user_input = input("Press Enter to confirm renaming this folder or type 's' to skip...").strip().lower()
                    if user_input != 's':
                        rename_folder(folder_path)
                    else:
                        print(f"Skipping folder: {folder_path}")
            else:
                print(f"Folder '{folder_name}' already has a timestamp. Skipping...")