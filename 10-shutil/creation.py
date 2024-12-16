import os

import os

# Set the current root path
root_path = os.getcwd() + f"/data"  # Replace with your desired path
os.chdir(root_path)

# Verify the current working directory
print("Current working directory:", os.getcwd())


# Setup for `source_folder` and `destination_folder`
os.makedirs("source_folder", exist_ok=True)
os.makedirs("destination_folder", exist_ok=True)

# Create example `.txt` files in `source_folder`
with open("source_folder/file1.txt", "w") as f:
    f.write("This is file 1.")
with open("source_folder/file2.txt", "w") as f:
    f.write("This is file 2.")

# Setup for `unsorted_files` directory
os.makedirs("unsorted_files", exist_ok=True)

# Create example files with different extensions in `unsorted_files`
with open("unsorted_files/document.pdf", "w") as f:
    f.write("This is a PDF file.")
with open("unsorted_files/image.jpg", "w") as f:
    f.write("This is an image file.")
with open("unsorted_files/readme.txt", "w") as f:
    f.write("This is a text file.")

# Setup for `folder_to_backup`
os.makedirs("folder_to_backup", exist_ok=True)

# Create files in `folder_to_backup`
with open("folder_to_backup/data1.txt", "w") as f:
    f.write("Backup data 1.")
with open("folder_to_backup/data2.txt", "w") as f:
    f.write("Backup data 2.")

# Setup for `temporary_directory`
os.makedirs("temporary_directory", exist_ok=True)

# Create a placeholder file in `temporary_directory`
with open("temporary_directory/tempfile.txt", "w") as f:
    f.write("Temporary data.")
