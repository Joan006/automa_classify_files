import os 
import time 

# Directorio que sera monitoreado
directory = "/Users/mac/Downloads"

# Categorias 
categories = {
    'Images': ['jpeg', 'jpg', 'png'],
    'PDFs': ['pdf'],
    'Datasets': ['csv', 'xlsx', 'json'],
    'Videos': ['mp4']
}

for category in ["Images", "PDFs", "Datasets", "Videos"]:
    os.makedirs(os.path.join(directory,category), exist_ok=True)


def clasify_file(filename):
    extension = filename.split(".")[-1]

    for category, extensions in categories.items():
        if extension in extensions:
            source_path = os.path.join(directory, filename)
            dest_path = os.path.join(directory, category, filename)

            os.rename(source_path, dest_path)
            print(f"Moved {filename} to {category}")

for filename in os.listdir(directory):
    clasify_file(filename)

initial_files = os.listdir(directory)

while True:
    time.sleep(5)
    courrent_files = os.listdir(directory)

    new_files = list(set(courrent_files) - set(initial_files))

    for filename in new_files:
        clasify_file(filename)

    initial_files = courrent_files


