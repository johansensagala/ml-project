import os

def add_jpg_extension_recursively(directory_path):
    for foldername, subfolders, filenames in os.walk(directory_path):
        for filename in filenames:
            if not filename.endswith('.jpg'):
                file_path = os.path.join(foldername, filename)
                new_name = filename + '.jpg'
                new_path = os.path.join(foldername, new_name)
                os.rename(file_path, new_path)
                print(f'Added .jpg extension to: {filename}')

# Ganti 'path_to_your_directory' dengan path ke direktori Anda
directory_path = 'raw'
add_jpg_extension_recursively(directory_path)
