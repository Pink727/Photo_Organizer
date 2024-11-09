import os
import shutil
from datetime import datetime

def create_month_folders(year_folder):
    """Create 12 month folders in the given year folder."""
    for month in range(1, 13):
        month_name = datetime(1900, month, 1).strftime('%B')
        month_folder_name = f"{month:02d}_{month_name}"
        month_folder_path = os.path.join(year_folder, month_folder_name)
        if not os.path.exists(month_folder_path):
            os.makedirs(month_folder_path)
            print(f"Created folder: {month_folder_path}")

def organize_folder_by_date(folder_path):
    """Organize photos in the given folder by their date."""
    # Walk through all subdirectories and files
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            
            # Extract year and month from the filename
            try:
                if file.startswith("IMG_"):
                    date_str = file[4:12]  # Extract the date part after 'IMG_'
                    date_obj = datetime.strptime(date_str, '%Y%m%d')
                elif file.startswith("Screenshot_"):
                    date_str = file[11:19]  # Extract the date part after 'Screenshot_'
                    date_obj = datetime.strptime(date_str, '%Y%m%d')
                else:
                    date_str = file.split('(')[0].strip()  # Extract the date part before the parenthesis and strip any whitespace
                    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
                
                year = date_obj.year
                month_number = date_obj.strftime('%m')
                month_name = date_obj.strftime('%B')
                month_folder_name = f"{month_number}_{month_name}"
                print(f"Processing file: {file}, Year: {year}, Month: {month_folder_name}")
            except ValueError:
                print(f"Skipping file {file}: unable to extract date")
                continue
            
            # Create subfolder names based on year and month
            year_folder = os.path.join(folder_path, str(year))
            month_folder = os.path.join(year_folder, month_folder_name)
            
            # Create the year folder if it doesn't exist
            if not os.path.exists(year_folder):
                os.makedirs(year_folder)
                print(f"Created folder: {year_folder}")
                create_month_folders(year_folder)
            elif not os.path.exists(month_folder):
                create_month_folders(year_folder)
            
            # Move the file to the appropriate subfolder
            destination_path = os.path.join(month_folder, file)
            shutil.move(file_path, destination_path)
            print(f"Moved file {file} to {destination_path}")

# Example usage
folder_path = r'C:\Users\doc72\OneDrive\Pictures\Google Drive Backup\Photos-001 (1)'
organize_folder_by_date(folder_path)