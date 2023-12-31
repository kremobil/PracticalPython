import zipfile, os
from pathlib import Path

def backup_to_zip(folder):
    folder = os.path.abspath(folder)

    number = 1
    while True:
        zip_filename = os.path.basename(folder) + "_" + str(number) + ".zip"
        if not os.path.exists(zip_filename):
            break
        number += 1

    print(f"Tworzenie archiwum {zip_filename}...")
    backup_zip = zipfile.ZipFile(zip_filename, "w")



    for folder_name, subfolders, files in os.walk(folder):
        print(f"Dodawanie plików w {folder_name}...")
        for file_name in files:
            newBase = os.path.basename(folder) + "_"
            if file_name.startswith(newBase) and file_name.endswith(".zip"):
                continue
            backup_zip.write(os.path.curdir ,os.path.relpath(os.path.join(folder, file_name)))
    backup_zip.close()

    print('Gotowe')

backup_to_zip(".venv/Scripts")
