import os

all_files = []

def get_all_files(path, level):
    child_files = os.listdir(path)
    for file in child_files:
        file_path = os.path.join(path, file)
        if os.path.isfile(file_path):
            all_files.append("\t" * level + file_path)
        else:
            get_all_files(file_path, level + 1)
    
get_all_files(os.getcwd(), 0)

for file in reversed(all_files):
    print(file)