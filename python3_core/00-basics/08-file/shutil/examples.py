# Step-by-Step Guide to Learning `shutil` in Python

# Importing the Module
import shutil
import os

# Set the current root path
root_path = os.getcwd() + f"/data"  # Replace with your desired path
os.chdir(root_path)

# Verify the current working directory
print("Current working directory:", os.getcwd())

# Step 3: Explore `shutil` Functions

# Copying Files
shutil.copy("source.txt", "destination.txt")  # Copies the content
shutil.copy2("source.txt", "destination.txt")  # Copies the content and metadata

# Moving Files and Directories
shutil.move("source.txt", "new_directory/")

# Deleting Directories
shutil.rmtree("directory_to_delete")

# Creating Archives
shutil.make_archive("archive_name", "zip", "directory_to_archive")

# Extracting Archives
shutil.unpack_archive("archive_name.zip", "output_directory")

# Disk Usage
# Get total, used, and free space on the filesystem
usage = shutil.disk_usage("/")
print(f"Total: {usage.total}, Used: {usage.used}, Free: {usage.free}")

# Step 4: Comparing `shutil` with `os`


# os.rename vs. shutil.move
os.rename("source.txt", "destination.txt")  # Only renames
shutil.move("source.txt", "destination_folder/")  # Moves or renames

# os.remove vs. shutil.rmtree
os.remove("file_to_delete.txt")  # Deletes a single file
shutil.rmtree("directory_to_delete")  # Deletes a directory tree

# Step 5: Practice Common Use Cases

# 1. Batch Copy Files
import os
source_directory = "source_folder"
destination_directory = "destination_folder"

for file_name in os.listdir(source_directory):
    if file_name.endswith(".txt"):
        full_source_path = os.path.join(source_directory, file_name)
        full_destination_path = os.path.join(destination_directory, file_name)
        shutil.copy(full_source_path, full_destination_path)

# 2. Organize Files by Type
import os
source_directory = "unsorted_files"

for file_name in os.listdir(source_directory):
    file_extension = file_name.split(".")[-1]
    folder_name = os.path.join(source_directory, file_extension)

    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    
    shutil.move(
        os.path.join(source_directory, file_name),
        os.path.join(folder_name, file_name)
    )

# 3. Create Backups
shutil.make_archive("backup", "zip", "folder_to_backup")

# 4. Clean Up Old Directories
try:
    shutil.rmtree("temporary_directory")
except FileNotFoundError:
    print("The directory does not exist!")

# Step 6: Error Handling
try:
    shutil.copy("nonexistent.txt", "destination.txt")
except FileNotFoundError:
    print("File not found!")
except PermissionError:
    print("Permission denied!")

# Step 9: Mini Project - File Manager Script
import os

def organize_files_by_type(directory):
    for file_name in os.listdir(directory):
        file_extension = file_name.split(".")[-1]
        folder_name = os.path.join(directory, file_extension)

        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        shutil.move(
            os.path.join(directory, file_name),
            os.path.join(folder_name, file_name)
        )

# Usage
organize_files_by_type("my_folder")

# Step 10: Practice and Experiment
# Modify and expand the examples above to handle edge cases or new requirements.
