import os
import shutil

# Define the base directory
base_dir = r'C:\Users\doc72\OneDrive\Pictures\Google Drive Backup\Photos-001 (1)'

# Define the years and months
years = range(2013, 2024 + 1)
months = [
    '01_January', '02_February', '03_March', '04_April', '05_May', '06_June',
    '07_July', '08_August', '09_September', '10_October', '11_November', '12_December'
]

# Create a mapping of month names to their corresponding folder names
month_mapping = {
    'jan': '01_January', 'Jan': '01_January', 'january': '01_January', 'January': '01_January',
    'feb': '02_February', 'Feb': '02_February', 'february': '02_February', 'February': '02_February',
    'mar': '03_March', 'Mar': '03_March', 'march': '03_March', 'March': '03_March',
    'apr': '04_April', 'Apr': '04_April', 'april': '04_April', 'April': '04_April',
    'may': '05_May', 'May': '05_May',
    'jun': '06_June', 'Jun': '06_June', 'june': '06_June', 'June': '06_June',
    'jul': '07_July', 'Jul': '07_July', 'july': '07_July', 'July': '07_July',
    'aug': '08_August', 'Aug': '08_August', 'august': '08_August', 'August': '08_August',
    'sep': '09_September', 'Sep': '09_September', 'september': '09_September', 'September': '09_September',
    'oct': '10_October', 'Oct': '10_October', 'october': '10_October', 'October': '10_October',
    'nov': '11_November', 'Nov': '11_November', 'november': '11_November', 'November': '11_November',
    'dec': '12_December', 'Dec': '12_December', 'december': '12_December', 'December': '12_December'
}

# Create the year and month folders
for year in years:
    year_path = os.path.join(base_dir, str(year))
    os.makedirs(year_path, exist_ok=True)
    for month in months:
        month_path = os.path.join(year_path, month)
        os.makedirs(month_path, exist_ok=True)

def move_files_and_cleanup(base_dir, year_path, processed_folders):
    """Move files from incorrectly named folders into the correct month folders and delete the empty incorrect folders."""
    changes_made = False
    for item in os.listdir(base_dir):
        item_path = os.path.join(base_dir, item)
        if os.path.isdir(item_path) and item_path not in processed_folders:
            item_lower = item.lower()
            print(f"Processing folder: {item_path} (lowercase: {item_lower})")
            if item_lower in month_mapping:
                month_folder = month_mapping[item_lower]
                dest_path = os.path.join(year_path, month_folder)
                print(f"Moving files from {item_path} to {dest_path}")
                # Ensure the destination directory exists
                os.makedirs(dest_path, exist_ok=True)
                # Move files from the old folder to the new folder
                for file_name in os.listdir(item_path):
                    src_file = os.path.join(item_path, file_name)
                    dest_file = os.path.join(dest_path, file_name)
                    print(f"Moving {src_file} to {dest_file}")
                    shutil.move(src_file, dest_file)
                    print(f"Moved {file_name} to {dest_path}")
                    changes_made = True
                # Remove the old empty folder
                try:
                    os.rmdir(item_path)
                    print(f"Removed empty folder {item_path}")
                except OSError as e:
                    print(f"Error removing folder {item_path}: {e}")
                processed_folders.add(item_path)
            else:
                print(f"Folder {item_path} does not match any month name.")
    return changes_made

def verify_and_cleanup_year_folders(year_path):
    """Verify that the year folder contains exactly 12 month folders and move any incorrectly named folders into the correct month folders."""
    existing_month_folders = os.listdir(year_path)
    if len(existing_month_folders) != 12:
        print(f"Year {year_path} does not have 12 month folders. Verifying...")
        for folder in existing_month_folders:
            folder_path = os.path.join(year_path, folder)
            folder_lower = folder.lower()
            if folder_lower not in month_mapping.values():
                print(f"Folder {folder_path} does not match the correct month structure.")
                move_files_and_cleanup(folder_path, year_path, set())
                try:
                    os.rmdir(folder_path)
                    print(f"Removed incorrect folder {folder_path}")
                except OSError as e:
                    print(f"Error removing folder {folder_path}: {e}")

# Verify the structure and move existing folders into the new structure
for year in years:
    year_path = os.path.join(base_dir, str(year))
    processed_folders = set()
    
    while True:
        existing_month_folders = os.listdir(year_path)
        if len(existing_month_folders) == 12:
            break
        print(f"Year {year} does not have 12 month folders. Verifying...")
        changes_made = move_files_and_cleanup(year_path, year_path, processed_folders)
        if not changes_made:
            print(f"No changes made in this pass for year {year}. Exiting loop.")
            break
        verify_and_cleanup_year_folders(year_path)

print("Folders rearranged successfully.")