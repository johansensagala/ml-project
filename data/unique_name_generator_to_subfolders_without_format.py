import os
import random
import string

def generate_random_name(length=20):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def rename_files_recursively(directory_path):
    for foldername, subfolders, filenames in os.walk(directory_path):
        for filename in filenames:
            file_name, file_extension = os.path.splitext(filename)
            new_name = generate_random_name() + file_extension
            file_path = os.path.join(foldername, filename)
            new_path = os.path.join(foldername, new_name)
            os.rename(file_path, new_path)
            print(f'Renamed: {filename} to {new_name}')

# Ganti 'path_to_your_directory' dengan path ke direktori Anda
directory_path = 'raw'
rename_files_recursively(directory_path)
