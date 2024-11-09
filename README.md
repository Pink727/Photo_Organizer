# Photo Organizer

![License](https://img.shields.io/badge/license-MIT-blue.svg)

## Description
This repository contains two Python scripts to help organize photos into a structured folder hierarchy based on the year and month. The scripts are:

1. `organize_photos.py`
2. `folder_organizer.py`

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)
- [Questions](#questions)

## Installation
1. Clone the repository:

```sh
git clone https://github.com/yourusername/Photo_Organizer.git
```

## Usage

### organize_photos.py

This script organizes photos in a given folder by their date. It creates year and month subfolders and moves the photos into the appropriate subfolders based on their date.

#### How to Use

1. Set the `folder_path` variable to the path of the folder containing your photos.
2. Run the script.

#### Example

```python
folder_path = r'C:\Users\doc72\OneDrive\Pictures\Google Drive Backup\Photos-001 (1)'
organize_folder_by_date(folder_path)
```

#### Functions

##### `create_month_folders(year_folder)`

Creates 12 month folders in the given year folder.

##### `organize_folder_by_date(folder_path)`

Organizes photos in the given folder by their date. It creates year and month subfolders and moves the photos into the appropriate subfolders based on their date.

### folder_organizer.py

This script ensures that the folder structure for each year from 2013 to 2024 contains exactly 12 month folders. It moves any incorrectly named folders into the correct month folders and deletes the empty incorrect folders.

#### How to Use

1. Set the `base_dir` variable to the path of the base directory containing your year folders.
2. Run the script.

#### Example

```python
base_dir = r'C:\Users\doc72\OneDrive\Pictures\Google Drive Backup\Photos-001 (1)'
```

#### Functions

##### `move_files_and_cleanup(base_dir, year_path, processed_folders)`

Moves files from incorrectly named folders into the correct month folders and deletes the empty incorrect folders.

##### `verify_and_cleanup_year_folders(year_path)`

Verifies that the year folder contains exactly 12 month folders and moves any incorrectly named folders into the correct month folders.

### Running the Scripts

To run the scripts, use the following commands:

```bash
python organize_photos.py
python folder_organizer.py
```

## License
This project is licensed under the [MIT License](https://opensource.org/license/mit).

## Questions
For any questions, please contact me with the information below:

GitHub: [Pink727](https://github.com/Pink727)

Email: doc72789@gmail.com
© 2024 Pink727. All Rights Reserved.
