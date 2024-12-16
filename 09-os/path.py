import os

path = os.getcwd()
print(path)

file_list = os.listdir(path)
for filename in file_list:
    print(filename)