# python file detection

import os

# Relative path
file_path  = "File Detection/templates"

if os.path.exists(file_path):
    print(f"The location {file_path} exists.")
    
    if os.path.isfile(file_path):
        print("That is a file.")
    elif os.path.isdir(file_path):
        print("This is a directory.")
else:
    print("The location doesn't exists.")