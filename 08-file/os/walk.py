import os

path = os.getcwd()
list_files = os.walk(path)

for root, dirs, files in list_files:
    print("{}***{}***{}: ".format(root, dirs, files))