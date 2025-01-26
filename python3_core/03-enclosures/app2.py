import os
os.chdir("/home/tourist/DIY/LearnPy/04-python3_core/03-enclosures/")

def make_filter(keep):
    def the_filter(file_name):
        print(file_name)
        file = open(file_name)
        lines = file.readlines()
        file.close()
        return [line for line in lines if keep in line]
    
    return the_filter

filter = make_filter("163.com")
print(filter("mbox.txt"))
